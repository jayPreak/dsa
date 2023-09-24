import random
import string

res = ""
a = []
n = 10
specials = "!@#$%^&*()<>?"
nums = '0123456789'
specials = list(specials)
x = len(specials)
a = len(nums)


# print(random.choice())
for i in range(10):
    z = random.randint(0, x-1)
    b = random.randint(0, a-1)
    res = "".join(random.choices(string.ascii_uppercase, k=n))
    r = list(res)
    # temp = res[3]
    # res.replace(temp, specials[z])
    r[3] = specials[z]
    r[6] = nums[b]
    r1 = ''
    for i in r:
        r1 += i
    # r1 = str(r)
    print(r1)
