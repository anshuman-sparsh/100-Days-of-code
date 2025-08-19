import asyncio
import time

async def fetch_user():
    print("Fetching user data...")
    await asyncio.sleep(2)
    print("...User data fetched.")
    return {"id": 1, "name": "Anshu"}

async def fetch_orders():
    print("Fetching user orders...")
    await asyncio.sleep(3)
    print("...Orders fetched.")
    return [{"order_id": 101, "item": "Book"}, {"order_id": 102, "item": "Laptop"}]

async def main():
    start_time = time.time()
    
    user_data, orders_data = await asyncio.gather(
        fetch_user(),
        fetch_orders()
    )
    
    end_time = time.time()
    
    print(f"\n--- Results ---")
    print(f"User: {user_data}")
    print(f"Orders: {orders_data}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds.")
    print("Note: Total time is ~3s, not 5s, because tasks ran concurrently.")

if __name__ == "__main__":
    asyncio.run(main())