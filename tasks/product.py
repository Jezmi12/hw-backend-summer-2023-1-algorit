from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    product = [(a, b) for a in arr1 for b in arr2]
    return product

