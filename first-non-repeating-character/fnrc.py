def first_non_repeating_letter(string: str):
    # Problem: This function takes a string.
    # The goal is to get the first character that only exists one time in the string
    # Also the function should be able to handle lower and uppercase
    #
    # Input: string -> str
    # Ouput: characterString -> str or empty string
    for c in string:
        if (string.lower().count(c.lower()) == 1):
            return c
    return ""
