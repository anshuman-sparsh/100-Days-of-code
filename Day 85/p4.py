import asyncio
import time

async def producer(queue: asyncio.Queue, num_items: int):
    for i in range(1, num_items + 1):
        await asyncio.sleep(0.5)
        print(f"Produced: item {i}")
        await queue.put(i)
    
    await queue.put(None) # Sentinel value to signal completion

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        
        print(f"Consuming: item {item}...")
        await asyncio.sleep(1)
        print(f"...Consumed: item {item}")
        queue.task_done()

async def main():
    q = asyncio.Queue()
    start_time = time.time()

    await asyncio.gather(
        producer(q, 5),
        consumer(q)
    )

    end_time = time.time()
    print(f"\nProducer-Consumer system finished in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())