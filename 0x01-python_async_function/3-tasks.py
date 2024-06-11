#!/usr/bin/env python3
""" Module for a randomly delayed task
"""
import asyncio as aio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """ Create a task with a random delay
    """
    return aio.create_task(wait_random(max_delay))


if __name__ == '__main__':
    import asyncio

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
