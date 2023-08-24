__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    if len(arr) == 0 or sum([i for i in arr if i % 2 != 0]) == 0:
        return 0.0
    return sum([i for i in arr if i % 2 == 0]) / sum([i for i in arr if i % 2 != 0])

