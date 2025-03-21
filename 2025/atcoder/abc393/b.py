s = list(input())
count = 0

#eliminate 3rd loop dayum
for i in range(len(s)):
    if s[i] != "A":
        continue
    for j in range(i+1, len(s)):
        if s[j] != "B":
            continue

        k = 2*j-i
        if k < len(s) and s[k] == "C":
            count+=1
        # for k in range(j+1, len(s)):
        #     if j-i == k-j and s[i] == "A" and s[j] == "B" and s[k] == "C":
        #         count += 1

print(count)



