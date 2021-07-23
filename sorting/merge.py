def merge_sort(arr):
    if len(arr) <= 1:
        return

    m = len(arr) // 2

    left = arr[:m]
    right = arr[m:]

    merge_sort(left)
    merge_sort(right)

    l, r, i = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[i] = left[l]
            l += 1
            i += 1
        else:
            arr[i] = right[r]
            r += 1
            i += 1

    while l < len(left):
        arr[i] = left[l]
        l += 1
        i += 1

    while r < len(right):
        arr[i] = right[r]
        r += 1
        i += 1

    return arr
