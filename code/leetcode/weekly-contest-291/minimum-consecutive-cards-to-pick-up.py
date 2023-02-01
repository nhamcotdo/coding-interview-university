class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        _dict = dict()
        min = 10e6 + 2
        for i,j in enumerate(cards):
            if  _dict.get(j) ==  None:
                _dict[j] = i
            else:
                if i - _dict[j] < min:
                    min = i - _dict[j] + 1
                _dict[j] = i
        
        return -1 if min == 10e6 + 2 else min