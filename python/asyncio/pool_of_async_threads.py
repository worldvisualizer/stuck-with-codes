import asyncio
import threading
from asyncio import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from typing import Dict, Set

import _asyncio

event_loops_for_each_thread: Dict[int, AbstractEventLoop] = {}


def run(corofn, *args):
    curr_thread_id = threading.current_thread().ident

    if curr_thread_id not in event_loops_for_each_thread:
        event_loops_for_each_thread[curr_thread_id] = asyncio.new_event_loop()

    thread_loop = event_loops_for_each_thread[curr_thread_id]
    coro = corofn(*args)
    return thread_loop.create_task(coro)


async def async_gather_tasks(all_tasks: Set[_asyncio.Task]):
    return await asyncio.gather(*all_tasks)


def wait_loops():
    # each thread will block waiting all async calls of its specific async loop
    curr_thread_id = threading.current_thread().ident
    threads_event_loop = event_loops_for_each_thread[curr_thread_id]
    
    # I print the following to prove that each thread is waiting its loop
    print(f'Thread {curr_thread_id} will wait its tasks.')
    return threads_event_loop.run_until_complete(async_gather_tasks(asyncio.all_tasks(threads_event_loop)))


async def main():
    loop = asyncio.get_event_loop()
    max_workers = 5
    executor = ThreadPoolExecutor(max_workers=max_workers)

    # dispatching async tasks for each thread.
    futures = [
        loop.run_in_executor(executor, run, asyncio.sleep, 1, x)
        for x in range(10)]

    # waiting the threads finish dispatching the async executions to its own event loops
    await asyncio.wait(futures)

    # at this point the async events were dispatched to each thread event loop

    # in the lines below, you tell each worker thread to wait all its async tasks completion.
    futures = [
        loop.run_in_executor(executor, wait_loops)
        for _ in range(max_workers)
    ]
    
    print(await asyncio.gather(*futures))
    # it will print something like:
    # [[1, 8], [0], [6, 3, 9, 7], [4], [2, 5]]
    # each sub-set is the result of the tasks of a thread
    # it is non-deterministic, so it will return a diferent array of arrays each time you run.


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start = perf_counter()
    loop.run_until_complete(main())
    end = perf_counter()
    duration_s = end - start
    # the print below proves that all threads are waiting its tasks asynchronously
    print(f'duration_s={duration_s:.3f}')
