import asyncio

count = 0
def counter():
    global count
    count += 1

async def run():
    while True:
        await asyncio.sleep(1)
        counter()

async def print_func():
    while True:
        await asyncio.sleep(0.4)
        print(count)

loop = asyncio.get_event_loop()
# future = asyncio.run_coroutine_threadsafe(run(), loop)
# future2 = asyncio.run_coroutine_threadsafe(print_func(), loop)

# result = future.result()
# result2 = future2.result()
cors = asyncio.wait([run(), print_func()])
loop.run_until_complete(cors)
