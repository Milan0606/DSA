#Remove duplicates while preserving order
# [1, 2, 2, 3, 1, 4] → [1, 2, 3, 4]

# approach 1

number = [1, 2, 2, 3, 1, 4]

unique_numbers = []

for num in number:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)

# approach 2

number = [1, 2, 2, 3, 1, 4, 7, 9, 13, 12, 11, 5 ,12, 11]

unique_numbers = []
seen = set()

for num in number:
    if num not in seen:
        unique_numbers.append(num)
        seen.add(num)

print(unique_numbers)