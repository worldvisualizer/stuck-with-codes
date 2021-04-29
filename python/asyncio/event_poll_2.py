import asyncio

count = 0

async def run():
    global count
    while True:
        await asyncio.sleep(1)
        count += 1

async def print_func():
    global count
    while True:
        await asyncio.sleep(0.3)
        print(count)

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(run())
    asyncio.ensure_future(print_func())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("closing loop")
    loop.close()
