from typing import List
class Solution:
    def best_combination(self, cards: List[int], combination: List[int]):
        # def left_exp_search(left: int) -> int:
        #     while left < len(cards) and cards[left] == combination[left]:
        #         left <<=  1
        #     left >>= 1
        #     return left
    
        # def right_exp_search(right: int) -> int:
        #     while right > 1 and cards[right] == combination[right]:
        #         right >>=  1
        #     right <<= 1
        #     return right
        
        i = 0 #left_exp_search(1)
        j = len(cards) - 1 #right_exp_search(len(cards) - 1)

        while cards[i] == combination[i]:
            i += 1

        while cards[j] == combination[j]:
            j -= 1
        cards[i: j + 1] = sorted(cards[i: j + 1])

        if cards == combination:
            return 'YES'
        else:
            return 'NO'

solution = Solution()
_ = int(input())
cards = list(map(int, input().split(' ')))
combination = list(map(int, input().split(' ')))

print(solution.best_combination(cards, combination))
