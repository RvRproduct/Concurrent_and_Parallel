import asyncio

"""
Synchronous Programming: In programming, we can simplify the definition of synchronous code as 'a bunch
of statements in sequence'; so each statement in your code is executed one after the other. This means
each statement has to wait for the previous one to finish executing.
"""


def foo():
    return


foo()
print("tim")

"""
Asynchronous Programming: Asynchrony, in computer programming, refers to the occurence of events
independent of the main program flow and ways to deal with such events.
"""
"""
Coroutines: coroutines are computer program components that generalize subroutines for non-preemptive
multitasking, by allowing execution to be suspended and resumed.
"""
"""
Async Event-Loop: In computer science, the event loop is a programming construct or design pattern that waits
for and dispatches events or messages in a program.
"""


async def main():
    print("tim")
    task = asyncio.create_task(foo("text"))
    await asyncio.sleep(2)  # 0.5
    # await task
    # await foo("text")
    print("finished")


async def foo(text):
    print(text)
    await asyncio.sleep(1)  # 10

asyncio.run(main())

# Example


async def fetch_data():
    print("start fetching")
    # as soon as our task is delayed another task is allowed to run
    await asyncio.sleep(2)
    print("done fetching")
    return {"data": 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2

asyncio.run(main())
