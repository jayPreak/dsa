def sub_lists (l):
    lists = []
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists

def diff(lst):
    # create a list of all possible pairs of elements
    pairs = [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i+1, len(lst))]

    # calculate the difference between each pair
    differences = [abs(pair[0] - pair[1]) for pair in pairs]

    return differences # output: [2, 4, 4]

l1 = [2, 4, 6]
k = 2
x = sub_lists(l1)
reslist = []
for i in range(len(x)):
    if len(x[i])==1:
        reslist.append(x[i])
    else:
        print(x[i], "original list")
        zz = x[i]
        res = diff(zz)
        print(res)
        if k not in res:
            reslist.append(x[i])

print(reslist)


