import asyncio
import time

async def say_hello():
    await asyncio.sleep(1)
    print("Hello, Async World!")

async def main():
    start_time = time.time()
    print("Running async function...")
    await say_hello()
    end_time = time.time()
    print(f"Finished in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())