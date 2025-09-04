from typing import List

import click

import vvcli_sdk
from ..enum import EnumAccountPrintableAttributes
from ...abstract import (
    AbstractPrintableTable,
    AbstractPrintableJSON,
    AbstractReadInputValue,
    AbstractPrintException,
)


class ListContractsCommand(
    AbstractPrintException,
    AbstractPrintableTable,
    AbstractReadInputValue,
    AbstractPrintableJSON,
):
    _printable_attributes = EnumAccountPrintableAttributes
    _table_headers = ["Key", "Apelido", "Produto Label", "Status"]

    def __init__(
        self,
        uuid: str,
        client_id: str,
        product: str,
        key: str,
        configuration: vvcli_sdk.Configuration,
    ):
        self._configuration = configuration
        self._uuid = uuid
        self._client_id = client_id
        self._product = product
        self._key = key

    async def _gen_table_rows(self, accounts: List[dict]):
        accounts_info = []
        for acc in accounts:
            accounts_info.append(
                (
                    acc["key"],
                    acc["surname"],
                    acc["productLabel"],
                    acc["status"],
                )
            )
        return accounts_info

    async def _validate(self):
        if not self._uuid and not self._client_id:
            self._client_id = await self._read_prompt_input(
                self._printable_attributes.CLIENT_ID.value, self._client_id, type=str
            )

    async def execute(self, return_json=False):
        try:
            await self._validate()
            with vvcli_sdk.ApiClient(self._configuration) as api_client:
                api_instance = vvcli_sdk.AccountApi(api_client)
                contracts = api_instance.list_contracts(
                    uuid=self._uuid,
                    client_id=self._client_id,
                    product=self._product,
                    contract_key=self._key,
                )
        except vvcli_sdk.exceptions.ApiException as exc:
            await self.print_exception(exc)
            return

        if return_json:
            await self._echo_json(contracts.to_dict())
            return

        contract_info = await self._gen_table_rows(contracts.to_dict()["items"])
        column_widths = await self._calculate_columns_width(
            self._table_headers, contract_info
        )
        await self._echo_table(column_widths, self._table_headers, contract_info)
