from typing import List

import click

import vvcli_sdk
from ...enum import EnumObjectStoragePrintableAttributes
from ....abstract import (
    AbstractReadInputValue,
    AbstractPrintableJSON,
    AbstractPrintableTable,
    AbstractPrintException,
)
from ....utils import format_storage_size


class DeleteBucketCommand(
    AbstractPrintException,
    # AbstractPrintableTable,
    AbstractReadInputValue,
    # bstractPrintableJSON,
):
    _printable_attributes = EnumObjectStoragePrintableAttributes
    # _table_headers = ["Nome", "Quota", "Uso", "Criado em"]

    def __init__(
        self,
        client_id: int,
        bucket_name: str,
        configuration: vvcli_sdk.Configuration,
    ):
        self._configuration = configuration
        self._client_id = client_id
        self._bucket_name = bucket_name

    # async def _gen_table_rows(self, list_obj: List[dict]):
    #     info = []
    #     for obj_u in list_obj:
    #         quota = obj_u["quota"]
    #         info.append(
    #             (
    #                 obj_u["name"],
    #                 (
    #                     format_storage_size(quota["maxSizeBytes"])
    #                     if quota["enabled"]
    #                     else "Não habilitada"
    #                 ),
    #                 format_storage_size(obj_u["usage"]["sizeUtilizedBytes"]),
    #                 obj_u["createdAt"].strftime("%d/%m/%Y %H:%M"),
    #             )
    #         )
    #     return info

    async def _validate(self):

        self._client_id = await self._read_prompt_input(
            self._printable_attributes.CLIENT_ID.value, self._client_id, type=int
        )
        self._bucket_name = await self._read_prompt_input(
            self._printable_attributes.NAME.value, self._bucket_name, type=str
        )

        click.echo(
            f"\nConfirmação para apagar bucket.\nCliente ID: {self._client_id} \nNome: {self._bucket_name}"
        )
        value = click.prompt(
            "Pressione `S` para continuar, qualquer outra tecla para cancelar"
        )
        if str(value).lower() != "s":
            return False
        return True

    async def execute(self):
        if not await self._validate():
            return
        try:
            with vvcli_sdk.ApiClient(self._configuration) as api_client:
                api_instance = vvcli_sdk.ObjectStorageApi(api_client)
                api_instance.delete_bucket(
                    client_id=self._client_id, bucket_name=self._bucket_name
                )
        except vvcli_sdk.exceptions.ApiException as exc:
            await self.print_exception(exc)
            return

        # if return_json:
        #     await self._echo_json(buckets.to_dict().get("items"))
        #     return

        # obj_user_info = await self._gen_table_rows(buckets.to_dict().get("items"))
        # column_widths = await self._calculate_columns_width(
        #     self._table_headers, obj_user_info
        # )
        # await self._echo_table(column_widths, self._table_headers, obj_user_info)
