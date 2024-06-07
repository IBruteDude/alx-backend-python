#!/usr/bin/env python3
"""Typed adder function factory Module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Typed adder function factory
    """
    return lambda x: x * multiplier
