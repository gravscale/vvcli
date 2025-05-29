import click

from ..enum import EnumAuthenticationPrintableAttributes
from ...abstract import AbstractReadInputValue
from ....config import CliConfiguration


class ConfigureAuthenticateCommand(AbstractReadInputValue):
    _printable_attributes = EnumAuthenticationPrintableAttributes

    def __init__(self, token: str, config_file: str, cli_config: CliConfiguration):
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
        self._cli_config.save_authorization(self._token)
        click.echo("Credential successfully saved!")
