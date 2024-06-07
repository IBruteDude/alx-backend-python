#!/usr/bin/env python3
"""Typed key-value pairer function Module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Typed key-value pairer function
    """
    return (k, v ** 2)
