class Solution:
    def max_number_of_words(self, s: str) -> int:
        letters = { letter : 0 for letter in 'sherif'}

        for char in s:
            letters[char] += 1

        letters['f'] //= 2
    
        return min(letters.values())
    
input_str = input()
solution = Solution()

print(solution.max_number_of_words(input_str))
