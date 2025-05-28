import asyncclick as click

from vvcli_sdk import AccessPermissions
from .usecase import GetSubUserObjectStorageCommand
from .... import CliConfiguration
from .usecase.create_subuser import CreateObjectStorageSubUserCommand

@click.group(name="subuser")
async def obj_subuser_group():
    """Subuser Object Storage"""
    pass


@obj_subuser_group.command("add", help="Create new subuser for object storage")
@click.option("--client-id", "-c", required=False, type=str, help="Client ID")
@click.option("--display-name", "-d", required=False, type=str, help="Display Name")
@click.option("--access", "-a", required=False, type=AccessPermissions, help="Access")
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Returned result as JSON",
)
@click.pass_obj
async def add_subuser(obj, client_id: str, display_name: str, access: str, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await CreateObjectStorageSubUserCommand(client_id, display_name, access, cli_config.load_sdk_configuration()).execute(json)



@obj_subuser_group.command("list", help="List subusers for object storage")
@click.option("--client-id", "-c", required=False, type=str, help="Client ID")
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Returned result as JSON",
)
@click.pass_obj
async def list_subuser(obj, client_id: str, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await GetSubUserObjectStorageCommand(client_id, cli_config.load_sdk_configuration()).execute(json)


