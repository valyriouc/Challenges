def same_structure_as(original, other):
    if (type(original) is not list or type(other) is not list):
        return False
    if len(original) != len(other):
        return False
    state = True
    for i in range(0, len(original)):
        if type(original[i]) is int and type(other[i]) is not int:
            state = False
        if type(original[i]) is str and type(other[i]) is int:
            state = True
        if type(original[i]) is list and type(other[i]) is not list:
            state = False
        elif type(original[i]) is list and type(other[i]) is list:
            state = same_structure_as(original[i], other[i])
        else:
            state = False
    return state