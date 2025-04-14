#  Count Even and Odd Numbers

lst = [1, 2, 3, 4, 5, 6]
even_count = sum(1 for num in lst if num % 2 == 0)
odd_count = len(lst) - even_count
print(f"Even: {even_count}, Odd: {odd_count}")
