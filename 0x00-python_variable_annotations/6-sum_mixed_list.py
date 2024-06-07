#!/usr/bin/env python3
"""Typed list summation function Module
"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """Typed list summation function
    """
    return sum(input_list)
