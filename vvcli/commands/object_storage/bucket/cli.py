import asyncclick as click

from .... import CliConfiguration
from . import usecase


@click.group(name="bucket")
async def obj_bucket_group():
    """Buckets
    Comandos para gerenciar buckets de armazenamento de objetos

    Exemplos de uso:

    Adicionar bucket:
        vvcli bucket add --client-id 123 --bucket-name meu-bucket --size-quota 1000 --max-objects 500 --json

    Listar buckets:
        vvcli bucket list --client-id 123 --json

    Remover bucket:
        vvcli bucket rm --client-id 123 --name meu-bucke
    """
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
    await usecase.CreateBucketCommand(
        client_id,
        bucket_name,
        size_quota,
        max_objects,
        cli_config.load_sdk_configuration(),
    ).execute(json)


@obj_bucket_group.command("list", help="Listar buckets de armazenamento de objetos")
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
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
    await usecase.ListBucketsCommand(
        client_id, cli_config.load_sdk_configuration()
    ).execute(json)


@obj_bucket_group.command("rm", help="Apagar bucket de armazenamento de objetos")
@click.option("--client-id", "-c", required=False, type=int, help="Client ID")
@click.option("--name", "-n", required=False, type=str, help="Nome do bucket")
@click.pass_obj
async def remove_bucket(obj, client_id: int, name: str):
    cli_config: CliConfiguration = obj["config"]
    await usecase.DeleteBucketCommand(
        client_id, name, cli_config.load_sdk_configuration()
    ).execute()
