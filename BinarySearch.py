def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [1, 3, 5, 7, 8]
target = 7
result = binary_search(arr, target)
print(f'Target found at index: {result}' if result != -1 else 'Target not found')

# Done