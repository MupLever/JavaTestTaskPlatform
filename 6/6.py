def check_log(ghost):
    return ghosts_log[ghost-1]

def friends(x, y):
    if x == y:
        return True
    for band in bands:
        if x in band and y in band:
            return True
    return False

def union(x, y):
    if not friends(x, y):
        for band in bands:
            if x in band:
                x_band = band
            if y in band:
                y_band = band
        new_band = x_band + y_band
        for ghost in new_band:
            ghosts_log[ghost-1] += 1
        bands.remove(x_band)
        bands.remove(y_band)
        bands.append(new_band)

ghosts_count, questions_count = map(int, input().split(' '))

ghosts_log = [ 1 for _ in range(ghosts_count) ]
bands = [ [i + 1] for i in range(ghosts_count) ]


for i in range(questions_count):
    params = list(map(int, input().split()))
    if params[0] == 1:
        union(params[1], params[2])
    elif params[0] == 2:
        if friends(params[1], params[2]):
            print('YES')
        else:
            print('NO')
    else:
        print(check_log(params[1]))
