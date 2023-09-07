def combination(sum, vals):
    for i in range(len(vals)):
        cur_sum = 0
        suggestion = []
        for j in range(i, len(vals)):
            if cur_sum + vals[j] <= sum:
                cur_sum += vals[j]
                suggestion.append(vals[j])
        if sum == cur_sum:
            return suggestion
    return []
    
required_amount = int(input().split(' ')[0])

vals = sorted(list(filter(lambda x: x <= required_amount, map(int, input().split(' ')))) * 2, reverse=True)

resulting_combination = combination(required_amount, vals)

if resulting_combination:
    print(len(resulting_combination))
    print(' '.join(map(str, resulting_combination)))
else:
    print(-1)
