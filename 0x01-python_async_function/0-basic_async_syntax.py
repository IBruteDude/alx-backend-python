#!/usr/bin/env python3
""" Module experimenting with async io operations
"""
import asyncio
import random as rd
from typing import Coroutine


async def wait_random(max_delay: int = 10) -> float:
    """ Wait for a random period of time with upper limit
    """
    period = rd.uniform(0, max_delay)
    await asyncio.sleep(period)
    return period


if __name__ == '__main__':

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
