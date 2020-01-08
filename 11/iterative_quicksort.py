def sort(arr):
    low = 0
    high = len(arr) - 1

    size = high - low + 1
    stack = [0] * size

    top = -1
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        p = partition(arr, low, high)

        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high


def partition(arr, low, high):
    i = (low - 1)
    mid_element = arr[high]

    for j in range(low, high):
        if arr[j] <= mid_element:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
