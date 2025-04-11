import asyncclick as click

from .... import CliConfiguration
from .usecase.create_user import CreateObjectStorageUserCommand

@click.group(name="user")
async def obj_user_group():
    """User Object Storage"""
    pass


@obj_user_group.command("add", help="Create new user for object storage")
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
async def add_user(obj, client_id: str, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await CreateObjectStorageUserCommand(client_id, cli_config.load_sdk_configuration()).execute(json)
