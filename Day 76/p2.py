import time

class Timer:
    def __enter__(self):
        print("Starting timer...")
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        duration = end_time - self.start_time
        print(f"Block executed in: {duration:.4f} seconds.")
        print("Timer finished.")




print("--- Running a task with the Timer context manager ---")
with Timer():
    total = sum(n for n in range(10_000_000))
    print("... task completed.")

print("\n--- Another example using time.sleep ---")
with Timer():
    time.sleep(0.5)
    print("... task completed.")