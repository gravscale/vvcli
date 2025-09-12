import asyncclick as click

from .usecase.create_bucket import CreateObjectStorageBucketCommand
from .usecase.list_buckets import ListObjectStorageBucketsCommand
from .... import CliConfiguration


@click.group(name="bucket")
async def obj_bucket_group():
    """Buckets Object Storage"""
    pass


@obj_bucket_group.command("add", help="Criar novo bucket para armazenamento de objetos")
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option("--bucket-name", "-b", required=False, type=str, help="Nome do bucket")
@click.option(
    "--size-quota",
    "-s",
    required=False,
    type=click.IntRange(min=1, max=50000000),
    help="Quota do bucket em megabyte(MB).",
)
@click.option(
    "--max-objects",
    "-m",
    required=False,
    type=int,
    help="Máximo de objetos permitidos no bucket.",
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
async def add_bucket(
    obj, client_id: int, bucket_name: str, size_quota: int, max_objects: int, json: bool
):
    cli_config: CliConfiguration = obj["config"]
    await CreateObjectStorageBucketCommand(
        client_id,
        bucket_name,
        size_quota,
        max_objects,
        cli_config.load_sdk_configuration(),
    ).execute(json)


@obj_bucket_group.command("get", help="Listar buckets de armazenamento de objetos")
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
async def list_buckets(obj, client_id: int, json: bool):
    cli_config: CliConfiguration = obj["config"]
    await ListObjectStorageBucketsCommand(
        client_id, cli_config.load_sdk_configuration()
    ).execute(json)
