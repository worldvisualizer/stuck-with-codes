class Ticker:
    """Yield numbers from 0 to `to` every `delay` seconds."""

    def __init__(self, delay, to):
        self.delay = delay
        self.i = 0
        self.to = to

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        if i >= self.to:
            raise StopAsyncIteration
        self.i += 1
        if i:
            await asyncio.sleep(self.delay)
        return i

def ticker_iterative(delay, to):
    return Ticker(delay, to)

# The same can be implemented as a much simpler asynchronous generator:
async def ticker(delay, to):
    """Yield numbers from 0 to `to` every `delay` seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

async def ticker_wrapper(func, delay, to):
    response = [elem async for elem in func(delay, to)]
    print(func.__name__)
    print(response)

import asyncio
fut1 = asyncio.ensure_future(ticker_wrapper(ticker, 1, 10))
fut2 = asyncio.ensure_future(ticker_wrapper(ticker_iterative, 1, 10))
loop = asyncio.get_event_loop()
loop.run_until_complete(fut1)
loop.run_until_complete(fut2)
