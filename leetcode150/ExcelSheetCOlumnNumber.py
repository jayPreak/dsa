x = "CDA"
res = 0
for i in x:
    res *= 26
    res += ord(i) - 64

print(res)
