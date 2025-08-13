import asyncclick as click

from .usecase import GetUserObjectStorageCommand
from ..enum import EnumQuotaSize
from .... import CliConfiguration

from .usecase.create_user import CreateObjectStorageUserCommand


@click.group(name="user")
async def obj_user_group():
    """User Object Storage"""
    pass


@obj_user_group.command("add", help="Create new user for object storage")
@click.option("--client-id", "-c", required=False, type=str, help="Client ID")
@click.option(
    "--size-quota",
    "-s",
    required=False,
    type=click.Choice([f"{m.value}" for m in EnumQuotaSize]),
    help=f"User quota in gigabyte (GB) options: {', '.join([f'{m.value}GB' for m in EnumQuotaSize])}",
)
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Returned result as JSON",
)
@click.pass_obj
async def add_user(obj, client_id: str, size_quota: int, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await CreateObjectStorageUserCommand(
        client_id, size_quota, cli_config.load_sdk_configuration()
    ).execute(json)


@obj_user_group.command("get", help="Get client user for object storage")
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
async def get_user(obj, client_id: str, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await GetUserObjectStorageCommand(
        client_id, cli_config.load_sdk_configuration()
    ).execute(json)
