# "EBG13 rknzcyr." -> "ROT13 example."

def rot13(message):
    source = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 
    result = ""
    for m in message:
        if (str.isalpha(m)):
            index = source.index(m)
            destIndex = 0;
            if (index <= 12 or (index > 25 and index <=38)):
                destIndex += index + 13
                print(m)
            else:
                destIndex += (index + 13 + 26) - len(source)
            
            result += source[destIndex]
        else:
            result += m
    return result

if __name__ == "__main__":
    print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"))