#!/usr/bin/env python3
""" Module for trying actual coroutines
"""
import asyncio as aio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int):
    """ Wait for n random delays
    """
    tasks = [aio.create_task(wait_random(max_delay)) for _ in range(n)]

    results = []

    for task in tasks:
        task.add_done_callback(lambda task: results.append(task.result()))

    await aio.gather(*tasks)
    return results


if __name__ == '__main__':
    import asyncio

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
