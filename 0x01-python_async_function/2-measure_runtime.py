#!/usr/bin/env python3
""" Module for a time measuring function
"""
import time
import asyncio as aio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int):
    """ Measure the running time for tasks
    """
    start = time.time()
    aio.run(wait_n(n, max_delay))
    end = time.time()
    return end - start


if __name__ == '__main__':
    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
