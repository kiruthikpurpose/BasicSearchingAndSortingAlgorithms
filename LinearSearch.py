def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


n = int(input("Enter the number of values: "))
arr = []
for i in range(n):
    j = int(input(f"Enter value {i+1}: "))
    arr.append(j)

target = int(input("Enter the target: "))
result = linear_search(arr, target)
print(f'Target found at index: {result}' if result != -1 else 'Target not found')