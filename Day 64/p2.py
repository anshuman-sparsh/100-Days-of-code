def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

for even in even_numbers(10):
    print(even)
