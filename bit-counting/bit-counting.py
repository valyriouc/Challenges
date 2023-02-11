def count_bits(n):
    c = 0
    for i in bin(n).replace("0b", ""):
        if i == '1':
            c += 1
    return c

def count_bits(n):
    return sum([int(i) for i in bin(n).replace("0b", "") if i == '1'])
