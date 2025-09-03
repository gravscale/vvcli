import json
from abc import ABCMeta, abstractmethod
from typing import List, Callable, Any, Tuple

import click

import vvcli_sdk
from .exceptions import ReadInputValueException, PrintableTableException
from .utils import get_columns_size, get_max_size_columns


class AbstractPrintableTable(metaclass=ABCMeta):
    @property
    @abstractmethod
    def _table_headers(self) -> List[str]:
        pass

    @abstractmethod
    def _gen_table_rows(self, data: List[dict]) -> List[tuple]:
        pass

    @classmethod
    async def _calculate_columns_width(cls, headers: List[str], rows: List[tuple]):
        try:
            size_items = await get_columns_size(headers, rows)
            column_widths = await get_max_size_columns(headers, size_items)
            return column_widths
        except Exception as exc:
            raise PrintableTableException(exc)

    @classmethod
    async def _generate_line(cls, *args):
        header = "|"
        for i in range(len(args)):
            value, size = args[i]
            if not value:
                value = ""
            header += " {:^{}} |".format(value, size)
        return header

    @classmethod
    async def _echo_table(cls, width: List[dict], headers: [str], data: [tuple]):
        header = await cls._generate_line(
            *[
                (headers[i], width[i][i] if len(width) > 0 else len(headers[i]))
                for i in range(len(headers))
            ]
        )

        click.echo("-" * len(header))
        click.echo(header)
        click.echo("-" * len(header))
        for item in data:
            line = await cls._generate_line(
                *[(item[i], width[i][i]) for i in range(len(item))]
            )
            click.echo(line)
        click.echo("-" * len(header))


class AbstractPrintableJSON(metaclass=ABCMeta):
    @classmethod
    async def _echo_json(cls, data: dict):
        formatted_json = json.dumps(data, indent=2)
        click.echo(formatted_json)


class AbstractPrintableTask(metaclass=ABCMeta):
    @classmethod
    async def _echo_task_info(cls, task):
        click.echo(f"Status: {task.status}") if task.status else None
        click.echo(f"Resultado: {str(task.result)}") if task.result else None


class AbstractReadInputValue(metaclass=ABCMeta):
    @classmethod
    async def _read_prompt_input(
        cls,
        text: str,
        variable,
        validators: List[Tuple[Callable, str]] = None,
        **kwargs,
    ):
        error = None
        try:
            value = click.prompt(text, **kwargs) if not variable else variable
            if validators:
                for validator, msg_error in validators:
                    error = msg_error
                    validator(value)
            return value
        except (ValueError, click.exceptions.BadParameter) as exc:
            error = error if error else exc.args[0]
            click.echo(error)
            return await cls._read_prompt_input(
                text, None, validators=validators, **kwargs
            )
        except click.exceptions.Abort:
            raise ReadInputValueException("Entrada abortada")


class AbstractPrintException(metaclass=ABCMeta):
    @classmethod
    def is_json(cls, valor):
        if not isinstance(valor, str):
            return False
        try:
            json.loads(valor)
            return True
        except json.JSONDecodeError:
            return False

    async def print_exception(self, exc: vvcli_sdk.exceptions.ApiException):
        message = ""
        if self.is_json(exc.body):
            data = json.loads(exc.body)
            message = data.get("detail") if "detail" in data.keys() else data

        click.echo(f"Erro: [{exc.status}] [{exc.reason}] {message}")
