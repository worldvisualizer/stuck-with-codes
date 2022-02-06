import asyncio
import time
import argparse

async def say_after(delay, what):
    print(f"before saying {what}")
    await asyncio.sleep(delay)
    print(what)


async def simple():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, "hello")
    await say_after(2, "world")
    print(f"finished at {time.strftime('%X')}")


async def nonblocking():
    print(f"started at {time.strftime('%X')}")
    loop = asyncio.get_event_loop()
    future1 = loop.create_task(say_after(1, "hello"))
    future2 = loop.create_task(say_after(3, "world"))
    print("created tasks for both future1 and 2")
    await asyncio.gather(future1, future2)
    print(f"finished at {time.strftime('%X')}")


def get_args():
    parser = argparse.ArgumentParser(description="option")
    parser.add_argument('option', default=0, type=int, help='integer option')
    return parser.parse_args()


if __name__ == "__main__":
    funcs = {
        0: simple,
        1: nonblocking
    }
    func = funcs[get_args().option]
    asyncio.run(func())

