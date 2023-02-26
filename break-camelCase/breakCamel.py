def solution(s: str):
    newStr = ""
    for i in range(0, len(s)):
        if (s[i].isupper()):
            newStr += " " + s[i]
        else:
            newStr += s[i]
    return newStr
