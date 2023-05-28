import re

class Solution:
    mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    
    def romanToInt(self, s: str) -> int:
        if (1 <= len(s) and len(s) <= 15 and re.match("^[IVXLCDM]*$", s)):
            result = 0
            for i in range(0, len(s)):
                number = Solution.mapping[s[i]]
                if (i == len(s) - 1):
                    result += number
                    continue

                if (number < Solution.mapping[s[i+1]]):
                    result -= number
                else:
                    result += number
            return result

if __name__ == "__main__":
    sol = Solution()
    sol.romanToInt("III")
