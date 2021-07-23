def counting_sort(arr):
    mem = [0] * 255
    for i in arr:
        mem[i] += 1

    res = []
    for number, times in enumerate(mem):
        if times == 0:
            continue
        for _ in range(times):
            res.append(number)
    return res
