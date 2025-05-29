from typing import List

import click
from pydantic_core import ValidationError

import vvcli_sdk
from vvcli_sdk import AccessPermissions
from ....abstract import (
    AbstractReadInputValue,
    AbstractPrintableJSON,
    AbstractPrintableTable,
)
from ...enum import EnumObjectStoragePrintableAttributes


class CreateObjectStorageSubUserCommand(
    AbstractPrintableTable, AbstractReadInputValue, AbstractPrintableJSON
):
    _printable_attributes = EnumObjectStoragePrintableAttributes
    _table_headers = ["Display Name", "Client Id", "Access Key", "Secret Key"]

    def __init__(
        self,
        client_id: str,
        display_name: str,
        access: str,
        configuration: vvcli_sdk.Configuration,
    ):
        self._configuration = configuration
        self._display_name = display_name
        self._access = access
        self._client_id = client_id

    async def _gen_table_rows(self, obj_users: List[dict]):
        obj_users_info = []
        for obj_u in obj_users:
            key = obj_u["keys"].pop()
            obj_users_info.append(
                (
                    obj_u["displayName"],
                    obj_u["clientId"],
                    key["accessKey"],
                    key["secretKey"],
                )
            )
        return obj_users_info

    async def _validate(self):

        def validate_access_permission(value):
            AccessPermissions(value)

        self._client_id = await self._read_prompt_input(
            self._printable_attributes.CLIENT_ID.value, self._client_id, type=str
        )
        self._display_name = await self._read_prompt_input(
            self._printable_attributes.DISPLAY_NAME.value, self._display_name, type=str
        )
        self._access = await self._read_prompt_input(
            self._printable_attributes.ACCESS.value,
            self._access,
            [(validate_access_permission, "Invalid access permission value. Try: read, write, readwrite")],
            type=str,
        )


    async def execute(self, return_json=False):
        await self._validate()

        try:
            with vvcli_sdk.ApiClient(self._configuration) as api_client:
                api_instance = vvcli_sdk.ObjectStorageApi(api_client)
                new_subuser = vvcli_sdk.CreateSubUserObjStorageSchema(
                    client_id=self._client_id,
                    display_name=self._display_name,
                    access=self._access,
                )
                obj_user = api_instance.create_subuser(new_subuser)
        except vvcli_sdk.exceptions.ApiException as exc:
            click.echo(f"Error: [{exc.status}] [{exc.reason}] {exc.body}")
            return

        if return_json:
            await self._echo_json(obj_user.to_dict())
            return

        obj_user_info = await self._gen_table_rows([obj_user.to_dict()])
        column_widths = await self._calculate_columns_width(
            self._table_headers, obj_user_info
        )
        await self._echo_table(column_widths, self._table_headers, obj_user_info)
