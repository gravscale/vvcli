import json
import csv
from typing import List, Dict, Any
import typer
from tabulate import tabulate


def format_output(data: List[Dict[str, Any]], output_format: str) -> str:
    """
    Formats the output in the specified format (table, json, csv).

    :param data: List of dictionaries representing the data.
    :param output_format: Desired output format ('table', 'json', 'csv').
    :return: Formatted string.
    """
    if output_format == "json":
        return json.dumps(data, indent=4)
    elif output_format == "csv":
        if not data:
            return ""
        csv_data = [",".join(data[0].keys())]  # Header
        csv_data += [",".join(str(row[k]) for k in row.keys()) for row in data]  # Rows
        return "\n".join(csv_data)
    elif output_format == "table":
        return tabulate(data, headers="keys", tablefmt="grid")
    else:
        raise ValueError(f"Unsupported output format: {output_format}")


def display_output(ctx: typer.Context, data: List[Dict[str, Any]]):
    """
    Format and display output based on the global output format.

    :param ctx: Typer context object to get the global output format.
    :param data: List of dictionaries to be formatted and displayed.
    """
    output_format = ctx.obj.get("output", "table")
    formatted_data = format_output(data, output_format)
    typer.echo(formatted_data)
