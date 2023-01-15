def dig_pow(n: int, p: int):
    # your code
    digits = []
    number = n

    # 1. Get each digit of n 
    while (n > 0):
        tmp = n % 10
        digits.insert(0,tmp)
        n = n // 10
    
    # get the power of the digit
    sum = 0
    for i in digits:
        sum += i ** p
        p += 1

    return sum // number if sum % number == 0 else -1

if __name__ == '__main__':
    print(dig_pow(2427, 1))
    print (dig_pow(1306, 1))
    

