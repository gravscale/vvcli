from typing import List

import vvcli_sdk
from ...enum import EnumObjectStoragePrintableAttributes
from ....abstract import (
    AbstractReadInputValue,
    AbstractPrintableJSON,
    AbstractPrintableTable,
    AbstractPrintException,
)


class GetUserObjectStorageCommand(
    AbstractPrintException,
    AbstractPrintableTable,
    AbstractReadInputValue,
    AbstractPrintableJSON,
):
    _printable_attributes = EnumObjectStoragePrintableAttributes
    _table_headers = ["Client Id", "Chave do Contrato"]

    def __init__(self, client_id: str, configuration: vvcli_sdk.Configuration):
        self._configuration = configuration
        self._client_id = client_id

    async def _gen_table_rows(self, obj_users: List[dict]):
        obj_users_info = []
        for obj_u in obj_users:
            obj_users_info.append((obj_u["clientId"], obj_u["contractKey"]))
        return obj_users_info

    async def _validate(self):

        self._client_id = await self._read_prompt_input(
            self._printable_attributes.CLIENT_ID.value, self._client_id, type=str
        )

    async def execute(self, return_json=False):
        await self._validate()

        try:
            with vvcli_sdk.ApiClient(self._configuration) as api_client:
                api_instance = vvcli_sdk.ObjectStorageApi(api_client)
                obj_user = api_instance.get_client_user(self._client_id)
        except vvcli_sdk.exceptions.ApiException as exc:
            await self.print_exception(exc)
            return

        if return_json:
            await self._echo_json(obj_user.to_dict())
            return

        obj_user_info = await self._gen_table_rows([obj_user.to_dict()])
        column_widths = await self._calculate_columns_width(
            self._table_headers, obj_user_info
        )
        await self._echo_table(column_widths, self._table_headers, obj_user_info)
