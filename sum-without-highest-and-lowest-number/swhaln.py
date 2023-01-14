def sum_array(arr: list):
    if arr is None or len(arr) < 3:
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)

def sum_array(arr: list):
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - (min(arr) + max(arr))

def sum_array(arr: list):
    if (arr is None or len(arr) < 3):
        return 0
    arr = sorted(arr)
    return sum(arr[1:len(arr)-1])

def sum_array(arr: list):
    