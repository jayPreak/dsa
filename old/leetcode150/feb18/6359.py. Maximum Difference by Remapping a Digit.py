num = 11891

x = str(num)
y = str(num)
max = 0
min = 0
        
for i in x:
    if i == "9":
        pass
    else:
        x1 =x.replace(i, "9", len(x))
        # print(x1)
        max = int(x1)
        break
                
tochange = y[0]
y1 = y.replace(tochange, "0")
# print(max)
min = int(y1)
print(max-min)