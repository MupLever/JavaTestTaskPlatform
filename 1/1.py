_, wallet = map(int, input().split(' '))
prices = list(map(int, input().split(' ')))

price_of_affordable_gun = 0
for price in prices:
    if wallet - price > 0 and \
        price > price_of_affordable_gun:
        price_of_affordable_gun = price
    
print(price_of_affordable_gun)
