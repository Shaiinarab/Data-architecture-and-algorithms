def find_min_max(arr):
    if not arr:
        raise ValueError("Array must not be empty")
    return min(arr), max(arr)