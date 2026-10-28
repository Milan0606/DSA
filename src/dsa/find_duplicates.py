# Find all duplicate elements

# [1, 2, 3, 2, 4, 1] → [1, 2]

number = [1, 2, 3, 2, 4, 1]

duplicates = []
seen = []

for num in number:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)

print(duplicates)