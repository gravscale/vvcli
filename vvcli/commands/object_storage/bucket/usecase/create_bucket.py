from typing import List

import vvcli_sdk
from ...enum import EnumObjectStoragePrintableAttributes
from ....abstract import (
    AbstractReadInputValue,
    AbstractPrintableJSON,
    AbstractPrintableTable,
    AbstractPrintException,
)
from ....utils import format_storage_size


class CreateBucketCommand(
    AbstractPrintException,
    AbstractPrintableTable,
    AbstractReadInputValue,
    AbstractPrintableJSON,
):
    _printable_attributes = EnumObjectStoragePrintableAttributes
    _table_headers = ["Nome", "Quota", "Uso", "Criado em"]

    def __init__(
        self,
        client_id: int,
        bucket_name: str,
        size_quota_mb: int,
        max_objects: int,
        configuration: vvcli_sdk.Configuration,
    ):
        self._configuration = configuration
        self._client_id = client_id
        self._bucket_name = bucket_name
        self._size_quota = size_quota_mb
        self._max_objects = max_objects

    async def _gen_table_rows(self, list_obj: List[dict]):
        info = []
        for obj_u in list_obj:
            quota = obj_u["quota"]
            info.append(
                (
                    obj_u["name"],
                    (
                        format_storage_size(quota["maxSizeBytes"])
                        if quota["enabled"]
                        else "Não habilitada"
                    ),
                    format_storage_size(obj_u["usage"]["sizeUtilizedBytes"]),
                    obj_u["createdAt"].strftime("%d/%m/%Y %H:%M"),
                )
            )
        return info

    async def _validate(self):

        self._client_id = await self._read_prompt_input(
            self._printable_attributes.CLIENT_ID.value, self._client_id, type=int
        )

        self._bucket_name = await self._read_prompt_input(
            self._printable_attributes.NAME.value, self._bucket_name, type=str
        )

    async def execute(self, return_json=False):
        await self._validate()
        try:
            with vvcli_sdk.ApiClient(self._configuration) as api_client:
                api_instance = vvcli_sdk.ObjectStorageApi(api_client)

                bucket = api_instance.create_bucket(
                    self._client_id,
                    vvcli_sdk.CreateBucketObjStorageSchema(
                        bucket_name=self._bucket_name,
                        quota=vvcli_sdk.AddBucketQuotaSchema(
                            max_size_mb=self._size_quota, max_objects=self._max_objects
                        ),
                    ),
                )
        except vvcli_sdk.exceptions.ApiException as exc:
            await self.print_exception(exc)
            return

        if return_json:
            await self._echo_json(bucket.to_dict())
            return

        obj_user_info = await self._gen_table_rows([bucket.to_dict()])
        column_widths = await self._calculate_columns_width(
            self._table_headers, obj_user_info
        )
        await self._echo_table(column_widths, self._table_headers, obj_user_info)
