import typer
from vvcli.obj.bucket import bucket_app

# Main CLI app
app = typer.Typer(help="CLI to manage buckets using S3 API", no_args_is_help=True)

# Add a global option for output format
@app.callback()
def main(ctx: typer.Context, output: str = typer.Option("table", help="Output format: table (default), json, or csv")):
    """
    Main callback to manage global options.
    """
    ctx.obj = {"output": output}

# Subapp for 'obj'
obj_app = typer.Typer(help="Object storage commands", no_args_is_help=True)
app.add_typer(obj_app, name="obj", help="Object storage buckets")

# Adding 'bucket' subcommands under 'obj'
obj_app.add_typer(bucket_app, name="bucket", help="Bucket commands", no_args_is_help=True)

if __name__ == "__main__":
    app()
