from typing import Any


def to_list(var: dict) -> list[Any]:
    return list(var.values())


def to_tuple(var: dict) -> tuple[Any]:
    return (*list(var.values()), )
