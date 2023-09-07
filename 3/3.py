count = int(input())
cards = list(map(int, input().split(' ')))
combination = list(map(int, input().split(' ')))

i = 0
j = len(cards) - 1

while cards[i] == combination[i]:
    i += 1

while cards[j] == combination[j]:
    j -= 1

cards[i:j + 1].sort()
if cards == combination:
    print('YES')
else:
    print('NO')
