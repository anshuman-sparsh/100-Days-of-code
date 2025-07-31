import random

def retry(func):
    def wrapper(*args, **kwargs):
        attempts = 3
        for i in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {i+1} failed: {e}")
        print("All attempts failed.")
    return wrapper

@retry
def might_fail():
    if random.choice([True, False]):
        raise ValueError("Random Failure")
    return "Success!"

print(might_fail())
