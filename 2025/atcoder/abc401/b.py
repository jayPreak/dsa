n = int(input())
loggedIn = False
c = 0

for _ in range(n):
    s = input()
    match s:
        case "login":
            loggedIn = True
        case "logout":
            loggedIn = False
        case "private":
            if (not loggedIn):
                c += 1


print(c)


