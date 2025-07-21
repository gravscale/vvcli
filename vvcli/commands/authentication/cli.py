import asyncclick as click

from ... import CliConfiguration
from .usecase import ConfigureAuthenticateCommand, AuthenticateInfoCommand


@click.group(name="auth")
async def authentication_group():
    """Authentication"""
    pass


@authentication_group.command("configure", help="Authenticate user by api token")
@click.option(
    "--config-file",
    "-c",
    type=click.Path(exists=True),
    default=None,
    help="Configuration file",
)
@click.option("--token", "-t", required=False, type=str, help="API token")
@click.pass_obj
async def configure(obj, token: str, config_file: str):
    cli_config: CliConfiguration = obj["config"]
    await ConfigureAuthenticateCommand(token, config_file, cli_config).execute()


@authentication_group.command(
    "info", help="Gets information from the user who is authenticated"
)
@click.pass_obj
async def auth_info(obj: dict):
    cli_config: CliConfiguration = obj["config"]
    await AuthenticateInfoCommand(cli_config.load_sdk_configuration()).execute()
