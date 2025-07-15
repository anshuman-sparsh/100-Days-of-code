from collections import deque

# Created an empty queue
queue = deque()

def enqueue(item):
    queue.append(item)
    print(f"Enqueued: {item}")

def dequeue():
    if queue:
        removed = queue.popleft()
        print(f"Dequeued: {removed}")
    else:
        print("Queue is empty")

def show():
    print("Current Queue:", list(queue))

enqueue("A")
enqueue("B")
show()        # Output: ['A', 'B']
dequeue()     # Removes 'A'
show()        # Output: ['B']