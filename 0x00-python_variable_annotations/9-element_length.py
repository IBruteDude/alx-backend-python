#!/usr/bin/env python3
"""Typed lengths computer function Module
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Typed lengths computer function
    """
    return [(i, len(i)) for i in lst]
