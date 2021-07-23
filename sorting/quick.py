def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [a for a in arr if a < pivot]
    middle = [a for a in arr if a == pivot]
    right = [a for a in arr if a > pivot]

    return quick_sort(left) + middle + quick_sort(right)
