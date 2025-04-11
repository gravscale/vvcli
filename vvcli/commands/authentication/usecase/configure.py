import click

import vvcli_sdk
from ...abstract import AbstractReadInputValue
from ....config import CliConfiguration
from ..enum import EnumAuthenticationPrintableAttributes


class ConfigureAuthenticateCommand(AbstractReadInputValue):
    _printable_attributes = EnumAuthenticationPrintableAttributes

    def __init__(
        self, token: str, config_file: str, cli_config: CliConfiguration
    ):
        self._token = token
        self._config_file = config_file
        self._cli_config = cli_config

    async def _validate(self):
        if self._config_file:
            data = self._cli_config.read_user_config(self._config_file)
            self._token = data["vvcli"]["token"]
            return

        self._token = await self._read_prompt_input(
            self._printable_attributes.API_TOKEN.value, self._token, type=str
        )


    async def execute(self):
        await self._validate()
        with vvcli_sdk.ApiClient(
            self._cli_config.load_sdk_configuration()
        ) as api_client:
            api_instance = vvcli_sdk.AuthenticationApi(api_client)
            authorization = api_instance.api_token(self._token)
        self._cli_config.save_authorization(authorization)
        click.echo("User successfully authenticated!")
