def array_diff(a: list, b: list):
    # your code here
    # Problem: we get two lists. All numbers that are present in a and b should be removed from a
    # Input: a -> lst; b -> lst
    # Output: a minus all elements contained in b
    return [i for i in a if not i in b]
