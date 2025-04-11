import asyncclick as click

from .commands.authentication.cli import authentication_group
from .commands.account.cli import account_group
from .commands.object_storage.cli import obj_storage_group
from .config import CliConfiguration


@click.group()
@click.pass_context
def vvcli(ctx: click.Context) -> None:
    ctx.ensure_object(CliConfiguration)
    ctx.obj = {"config": CliConfiguration()}


vvcli.add_command(authentication_group)
vvcli.add_command(account_group)
vvcli.add_command(obj_storage_group)


if __name__ == "__main__":
    vvcli(obj={})
