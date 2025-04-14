# Sum and Average of Tuple

t = tuple(map(int, input("Enter numbers separated by space: ").split()))
print("Sum:", sum(t))
print("Average:", sum(t) / len(t))