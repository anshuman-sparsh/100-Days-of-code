# Formatted Summary Table


entries = []
for i in range(3):
    name = input(f"Enter name #{i+1}: ")
    score = int(input(f"Enter score for {name}: "))
    entries.append((name, score))


print("\nLeaderboard:")
print(f"{'Name':<12} {'Score':>5}")
print("-" * 20)
for name, score in entries:
    print(f"{name:<12} {score:>5}")
