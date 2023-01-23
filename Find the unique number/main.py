def find_uniq(array):
    a, b = set(array)
    return a if array.count(a) == 1 else b
