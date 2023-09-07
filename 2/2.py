letters = { letter : 0 for letter in 'sherif'}
input_str = input()

for char in input_str:
    letters[char] += 1

letters['f'] //= 2

print(min(letters.values()))
