class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        ans = []

        def isPalindrome(s):
            if not s or len(s) == 1:
                 return True
            return s[0] == s[len(s) - 1] and isPalindrome(s[1:-1])
        
        def numChar(_list):
            return sum([len(_) for _ in _list])

        def solve(_ans = [], k = 0, _s = s):
            l = len(_s)
            if not _s:
                if k == length:
                    ans.append(_ans)
                return

            if l == 1:
                _ans.append(_s)
                if k + 1 == length:
                    ans.append(_ans)
                return

            for i in range(1, l + 1):
                if isPalindrome(_s[: i]):
                    solve(_ans + [_s[: i]], k + i, _s[i:])

        solve()

        return ans