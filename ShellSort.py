def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Start with a large gap, then reduce the gap
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until the correct location is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Example usage
arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print("Sorted array:", arr)
