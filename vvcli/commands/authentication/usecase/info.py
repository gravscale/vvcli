import click

import vvcli_sdk
from ...abstract import AbstractPrintException


class AuthenticateInfoCommand(AbstractPrintException):
    def __init__(self, configuration: vvcli_sdk.Configuration):
        self._configuration = configuration

    async def execute(self):
        try:
            click.echo(f"Host: {self._configuration.host}")
            with vvcli_sdk.ApiClient(self._configuration) as api_client:
                api_instance = vvcli_sdk.AuthenticationApi(api_client)
                authenticated_user_info = api_instance.info()
        except vvcli_sdk.exceptions.ApiException as exc:
            await self.print_exception(exc)
            return
        click.echo(f"Usuário autenticado: {authenticated_user_info.email}")
