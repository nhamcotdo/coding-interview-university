class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        key = 0
        for i in range(n):
            if number[i] == digit:
                if i < n - 1 and number[i] < number[i + 1]:
                    return number[:i] + number[i + 1:]
                key = i
        
        return number[:key] + number[key + 1:]