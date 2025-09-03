from typing import List, Optional

import click

import vvcli_sdk
from ...enum import EnumObjectStoragePrintableAttributes, EnumQuotaSize
from ....abstract import (
    AbstractReadInputValue,
    AbstractPrintableJSON,
    AbstractPrintableTable,
    AbstractPrintException,
)


class CreateObjectStorageUserCommand(
    AbstractPrintException,
    AbstractPrintableTable,
    AbstractReadInputValue,
    AbstractPrintableJSON,
):
    _printable_attributes = EnumObjectStoragePrintableAttributes
    _table_headers = ["Cliente Id", "Contract Key", "Access Key", "Secret Key"]

    def __init__(
        self, client_id: str, size_quota: int, configuration: vvcli_sdk.Configuration
    ):
        self._configuration = configuration
        self._client_id = client_id
        self._size_quota = size_quota

    async def _gen_table_rows(self, obj_users: List[dict]):
        obj_users_info = []
        for obj_u in obj_users:
            key = obj_u["keys"].pop()
            obj_users_info.append(
                (
                    obj_u["clientId"],
                    obj_u["contractKey"],
                    key["accessKey"],
                    key["secretKey"],
                )
            )
        return obj_users_info

    async def _validate(self):

        def validate_user_quota(value):
            if value < 100 or value > 50000:
                raise click.BadParameter("Informe um valor entre 100 e 50000")



        self._client_id = await self._read_prompt_input(
            self._printable_attributes.CLIENT_ID.value, self._client_id, type=str
        )

        self._size_quota = await self._read_prompt_input(
            self._printable_attributes.QUOTA.value,
            self._size_quota,
            [
                (
                    validate_user_quota,
                    "Informe um valor entre 100 e 50000" ,
                )
            ],
            type=int,
        )
        click.echo("\nConfirmação para contratação de armazenamento de objetos.")
        click.echo(f"Cliente ID: {self._client_id}")
        click.echo(f"Tamanho da cota: {self._size_quota}GB")
        value = click.prompt("Pressione `S` para continuar, qualquer outra tecla para cancelar")
        if str(value).lower() != "s":
            return False
        return True

    async def execute(self, return_json=False):
        if not await self._validate():
            return
        try:
            with vvcli_sdk.ApiClient(self._configuration) as api_client:
                api_instance = vvcli_sdk.ObjectStorageApi(api_client)
                obj_user = api_instance.create_client_user(
                    self._client_id, self._size_quota
                )
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
