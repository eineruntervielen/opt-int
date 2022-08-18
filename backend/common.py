"""General purpose helper and common methods"""
from typing import Iterable


def list_bool_to_int(l: list) -> list:
    for e in l:
        if isinstance(e, Iterable) and not isinstance(e, str):
            for x in list_bool_to_int(e):
                yield x



print(list(list_bool_to_int([[True], False])))
