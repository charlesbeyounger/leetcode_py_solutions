class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        index = 0
        result = 0
        while index < len(s):
            if index + 1 < len(s) and d[s[index]] < d[s[index + 1]]:
                result += d[s[index + 1]] - d[s[index]]
                index += 2
            else:
                result += d[s[index]]
                index += 1

        return result