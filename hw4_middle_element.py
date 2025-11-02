def middle_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    mid = (len(lst) - 1) // 2
    return lst[mid]