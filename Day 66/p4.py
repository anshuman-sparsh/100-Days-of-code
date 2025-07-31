def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

@bold
@uppercase
def greet():
    return "hello world"

print(greet()) 

@uppercase
@bold
def greet():
    return "hello world"

print(greet())