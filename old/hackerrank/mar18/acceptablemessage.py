def is_acceptable(s, m):
    count_0 = s.count('0')
    count_1 = s.count('1')
    count_q = s.count('?')
    if abs(count_0 - count_1) > count_q:
        return False

    for i in range(len(s) - m + 1):
        sub = s[i:i+m]
        sub_count_0 = sub.count('0')
        sub_count_1 = sub.count('1')
        sub_count_q = sub.count('?')
        if abs(sub_count_0 - sub_count_1) > sub_count_q:
            return False
        remaining_q = sub_count_q - abs(sub_count_0 - sub_count_1)
        if remaining_q % 2 == 1:
            return False
        if i > 0 and s[i-1] == '?' and sub_count_0 > sub_count_1:
            count_0 += remaining_q // 2
            count_1 += remaining_q // 2 + remaining_q % 2
        elif i > 0 and s[i-1] == '?' and sub_count_1 > sub_count_0:
            count_0 += remaining_q // 2 + remaining_q % 2
            count_1 += remaining_q // 2
        if count_0 < count_1 - remaining_q or count_1 < count_0 - remaining_q:
            return False

    return True

t = int(input())
for _ in range(t):
    x, m = map(int, input().split())
    s = input()
    if is_acceptable(s, m):
        print("YES")
    else:
        print("NO")
