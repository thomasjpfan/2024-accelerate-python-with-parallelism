import sys
import time
import asyncio
from asyncio import get_running_loop, to_thread, TaskGroup
from concurrent.futures import ThreadPoolExecutor


def cpu_bound_task(n):
    return sum(i * i for i in range(n))


async def main():
    N_THREADS, TASKS, SIZE = 4, 10, 5000000

    get_running_loop().set_default_executor(ThreadPoolExecutor(max_workers=N_THREADS))

    start = time.time()

    async with TaskGroup() as tg:
        for _ in range(TASKS):
            tg.create_task(to_thread(cpu_bound_task, SIZE))

    print(f"Elapsed time: {time.time() - start}")


if __name__ == "__main__":
    print(f"GIL {sys._is_gil_enabled()}")
    asyncio.run(main())

# GIL False
# Elapsed time: 0.455121040344238

# GIL True
# Elapsed time: 1.625643014907837
