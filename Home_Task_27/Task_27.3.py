lst = [[1,2,3], [4,[5,6]], 7,8,'ghj']
res = []
def count(x):
    for i in x:
        if type(i) == list:
            res.append('lst')
            count(i)
        else:
            res.append(i)

    return len(res)

print(count(lst))