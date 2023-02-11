
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

if __name__ == '__main__':
    print (move_zeros([]))