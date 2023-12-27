from typing import Any


def to_list(var: dict) -> list[list[Any]]:
    keys = list(var.keys())
    values = list(var.values())
    return [keys, values]


def to_tuple(var: dict) -> tuple[list[Any], list[Any]]:
    keys = list(var.keys())
    values = list(var.values())
    return keys, values
