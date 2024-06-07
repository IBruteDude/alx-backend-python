#!/usr/bin/env python3
""" Var typed Module
"""
from typing import Mapping, Any, Union, TypeVar
from types import NoneType


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, NoneType] = None) -> Union[Any, T]:
    """ Var typed util
    """
    if key in dct:
        return dct[key]
    else:
        return default
