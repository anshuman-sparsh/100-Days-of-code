def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "info":
                print(f"[INFO] Calling {func.__name__} with {args} {kwargs}")
            elif level == "debug":
                print(f"[DEBUG] Executing {func.__name__}...")
            result = func(*args, **kwargs)
            if level == "debug":
                print(f"[DEBUG] {func.__name__} returned {result}")
            return result
        return wrapper
    return decorator

@log("info")
def add(a, b):
    return a + b

@log("debug")
def multiply(x, y):
    return x * y

print(add(3, 4))
print(multiply(5, 6))
