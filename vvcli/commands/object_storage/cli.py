import asyncclick as click

from .user.cli import obj_user_group

@click.group(name="obj")
async def obj_storage_group():
    """Object Storage"""
    pass

obj_storage_group.add_command(obj_user_group)

