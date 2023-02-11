
def move_zeros(lst: list):
    i = 0
    nulls = []
    while (i <= (len(lst) - 1)):
        if (lst[i] == 0):
            lst.pop(i)
            nulls.append(0)
        else:
            i += 1
    lst.extend(nulls)
    return lst

def move_zeros(lst: list):
    l = [i for i in lst if i != 0]
    l.extend([0 for i in range(0, len(lst) - len(l))])
    return l
