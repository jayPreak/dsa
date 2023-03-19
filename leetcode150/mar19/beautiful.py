lst = [2, 4, 6]

pairs = [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i+1, len(lst))]

    # calculate the difference between each pair
differences = [abs(pair[0] - pair[1]) for pair in pairs]

print(differences) # output: [2, 4, 4]