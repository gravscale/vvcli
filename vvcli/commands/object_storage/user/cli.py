import asyncclick as click

from .usecase import GetUserObjectStorageCommand
from ..enum import EnumQuotaSize
from .... import CliConfiguration

from .usecase.create_user import CreateObjectStorageUserCommand


@click.group(name="user")
async def obj_user_group():
    """Usuário Object Storage"""
    pass


@obj_user_group.command("add", help="Criar novo usuário para armazenamento de objetos")
@click.option("--client-id", "-c", required=False, type=str, help="Client ID")
@click.option(
    "--size-quota",
    "-s",
    required=False,
    type=click.IntRange(min=100, max=50000),
    help="Quota do usuário em gigabyte(GB). Valor entre 100GB e 50000GB",
)
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Resultado retornado como JSON",
)
@click.pass_obj
async def add_user(obj, client_id: str, size_quota: int, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await CreateObjectStorageUserCommand(
        client_id, size_quota, cli_config.load_sdk_configuration()
    ).execute(json)


@obj_user_group.command("get", help="Obter usuário cliente para armazenamento de objetos")
@click.option("--client-id", "-c", required=False, type=str, help="Client ID")
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Resultado retornado como JSON",
)
@click.pass_obj
async def get_user(obj, client_id: str, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await GetUserObjectStorageCommand(
        client_id, cli_config.load_sdk_configuration()
    ).execute(json)
