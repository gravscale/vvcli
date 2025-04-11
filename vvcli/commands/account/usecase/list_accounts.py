from typing import List

import vvcli_sdk
from ...abstract import AbstractPrintableTable, AbstractPrintableJSON


class ListAccountsCommand(AbstractPrintableTable, AbstractPrintableJSON):
    _table_headers = ["Account ID", "Client ID", "Client Status"]

    def __init__(self, configuration: vvcli_sdk.Configuration):
        self._configuration = configuration

    async def _gen_table_rows(self, accounts: List[dict]):
        accounts_info = []
        for acc in accounts:
            accounts_info.append((acc["uuid"], acc["clientId"], acc["clientStatus"]))
        return accounts_info

    async def execute(self, return_json=False):
        with vvcli_sdk.ApiClient(self._configuration) as api_client:
            api_instance = vvcli_sdk.AccountApi(api_client)
            accounts = api_instance.list_accounts()

        if return_json:
            await self._echo_json(accounts.to_dict())
            return

        acc_info = await self._gen_table_rows(accounts.to_dict()["items"])
        column_widths = await self._calculate_columns_width(
            self._table_headers, acc_info
        )
        await self._echo_table(column_widths, self._table_headers, acc_info)
