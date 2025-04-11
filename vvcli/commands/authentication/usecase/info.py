import click

import vvcli_sdk


class AuthenticateInfoCommand:
    def __init__(self, configuration: vvcli_sdk.Configuration):
        self._configuration = configuration

    async def execute(self):
        with vvcli_sdk.ApiClient(self._configuration) as api_client:
            api_instance = vvcli_sdk.AuthenticationApi(api_client)
            authenticated_user_info = api_instance.info()
        click.echo(
            f"Authenticated user: {authenticated_user_info.email} {authenticated_user_info.nickname}"
        )
