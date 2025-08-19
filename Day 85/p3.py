import asyncio
import time

async def fetch_page(url: str):
    print(f"Fetching {url}...")
    await asyncio.sleep(1)
    print(f"...Done fetching {url}")
    return f"Content of {url}"

async def run_sequentially():
    start_time = time.time()
    await fetch_page("page 1")
    await fetch_page("page 2")
    await fetch_page("page 3")
    end_time = time.time()
    print(f"Total time (Sequential): {end_time - start_time:.2f} seconds")

async def run_concurrently():
    start_time = time.time()
    await asyncio.gather(
        fetch_page("page 1"),
        fetch_page("page 2"),
        fetch_page("page 3")
    )
    end_time = time.time()
    print(f"Total time (Concurrent): {end_time - start_time:.2f} seconds")

async def main():
    print("--- Sequential Execution ---")
    await run_sequentially()
    
    print("\n--- Concurrent Execution ---")
    await run_concurrently()

if __name__ == "__main__":
    asyncio.run(main())