class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a = [str(_ + 1) for _ in range(n)]
        fact = [1 for _ in range(n)]
        for i in range(1, n):
            fact[i] = i * fact[i - 1]

        ans = []
        i = 1
        k -= 1
        while a:
            index = k // fact[n - i]
            ans.append(a[index])
            a.remove(a[index])

            k %= fact[n - i]
            i += 1
        
        return ''.join(ans)
