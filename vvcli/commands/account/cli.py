import asyncclick as click

from ... import CliConfiguration
from .usecase import ListAccountsCommand, ListContractsCommand


@click.group(name="account")
async def account_group():
    """Client Accounts"""
    pass


@account_group.command("list")
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Returned result as JSON",
)
@click.pass_obj
async def list_accounts(obj, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await ListAccountsCommand(cli_config.load_sdk_configuration()).execute(
        return_json=json
    )


@account_group.command("contracts")
@click.option("--uuid", "-u", required=False, type=str, help="Account uuid")
@click.option("--client-id", "-ci", required=False, type=str, help="Account client id")
@click.option("--product", "-p", required=False, type=str, help="Contract product")
@click.option("--key", "-k", required=False, type=str, help="Contract key")
@click.option(
    "--json",
    "-j",
    is_flag=True,
    default=False,
    type=bool,
    help="Returned result as JSON",
)
@click.pass_obj
async def account_contracts(
    obj,
    uuid: str,
    client_id: str,
    product: str,
    key: str,
    json: bool,
):
    cli_config: CliConfiguration = obj["config"]
    await ListContractsCommand(
        uuid,
        client_id,
        product,
        key,
        cli_config.load_sdk_configuration(),
    ).execute(return_json=json)
