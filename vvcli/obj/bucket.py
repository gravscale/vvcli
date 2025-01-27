import typer
from vvcli.obj.config import get_api_s3
from vvcli.utils.outputs import display_output
from icecream import ic
import json
from datetime import datetime

# turn off ic
ic.disable()


bucket_app = typer.Typer(help="Bucket management commands")


@bucket_app.command("create", no_args_is_help=True)
def create_bucket(ctx: typer.Context, bucket_name: str):
    """
    Create a new bucket using S3 API.
    """
    try:
        s3_client = get_api_s3()
        s3_client.create_bucket(Bucket=bucket_name)
        bucket_data = {"bucket": bucket_name, "status": "Created"}
        display_output(ctx, [bucket_data])
    except Exception as e:
        display_output(ctx, [{"error": f"Error creating bucket '{bucket_name}': {e}"}])


@bucket_app.command("delete", no_args_is_help=True)
def delete_bucket(ctx: typer.Context, bucket_name: str):
    """
    Delete a bucket using S3 API.
    """
    try:
        s3_client = get_api_s3()
        s3_client.delete_bucket(Bucket=bucket_name)
        bucket_data = {"bucket": bucket_name, "status": "Deleted"}
        display_output(ctx, [bucket_data])
    except Exception as e:
        display_output(ctx, [{"error": f"Error deleting bucket '{bucket_name}': {e}"}])


@bucket_app.command("ls")
def list_buckets(ctx: typer.Context):
    """
    List all buckets using S3 API.
    """
    try:
        s3_client = get_api_s3()
        response = s3_client.list_buckets()
        buckets = response.get("Buckets", [])

        if not buckets:
            display_output(ctx, [{"message": "No buckets found."}])
            return

        bucket_data = [{"bucket": bucket["Name"]} for bucket in buckets]
        display_output(ctx, bucket_data)
    except Exception as e:
        display_output(ctx, [{"error": f"Error listing buckets: {e}"}])

@bucket_app.command("ls-objects", no_args_is_help=True)
def list_objects(ctx: typer.Context, bucket_name: str):
    """
    List all objects in a specific bucket using S3 API with path-style addressing.
    """
    try:
        s3_client = get_api_s3()
        response = s3_client.list_objects_v2(Bucket=bucket_name)  # Use ListObjectsV2 para melhor compatibilidade

        objects = response.get("Contents", [])
        if not objects:
            display_output(ctx, [{"message": f"No objects found in bucket '{bucket_name}'."}])
            return

        object_data = [{"object": obj["Key"], "size": obj["Size"]} for obj in objects]
        display_output(ctx, object_data)
    except Exception as e:
        display_output(ctx, [{"error": f"Error listing objects in bucket '{bucket_name}': {e}"}])


@bucket_app.command("get", no_args_is_help=True)
def get_bucket(ctx: typer.Context, bucket_name: str):
    """
    Fetch detailed information about a specific bucket.
    """
    try:
        s3_client = get_api_s3()
        response = s3_client.get_bucket_acl(Bucket=bucket_name)

        grants = response.get("Grants", [])
        if not grants:
            display_output(ctx, [{"message": f"No ACLs found for bucket '{bucket_name}'."}])
            return

        acl_data = [
            {"permission": grant["Permission"], "grantee": grant["Grantee"].get("ID", "Unknown")}
            for grant in grants
        ]
        display_output(ctx, acl_data)
    except Exception as e:
        display_output(ctx, [{"error": f"Error fetching details for bucket '{bucket_name}': {e}"}])
