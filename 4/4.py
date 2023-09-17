from typing import List

class Solution:
    def best_combination(self, required_amount: int, vals: List[int]) -> List[int]:
        def rbinsearch(l: int, r: int, current_sum) -> int:
            while l < r:
                m = (l + r + 1) // 2
                if current_sum + vals[m] <= required_amount:
                    l = m
                else:
                    r = m - 1
            return l

        for left in range(len(vals)):
            cur_sum = 0
            suggestion = []
            right = len(vals)
            while left < right:
                right = rbinsearch(left, right - 1, cur_sum)
                cur_sum += vals[right]
                suggestion.append(vals[right])
                if required_amount == cur_sum:
                    return suggestion
        return []

required_amount, _ = map(int, input().split(' '))
vals = sorted(list(map(int, input().split(' '))) * 2)

solution = Solution()

resulting_combination = solution.best_combination(required_amount, vals)

if resulting_combination:
    print(len(resulting_combination))
    print(' '.join(map(str, resulting_combination)))
else:
    print(-1)
