#!/usr/bin/env python3
""" Module experimenting with async io operations
"""
import asyncio as aio
import random as rd


async def wait_random(max_delay: int = 10):
    """ Wait for a random period of time with upper limit
    """
    period = rd.uniform(0, max_delay)
    await aio.sleep(period)
    return period


if __name__ == '__main__':
    import asyncio

    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
