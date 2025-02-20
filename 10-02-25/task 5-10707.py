def convert (num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //=sys
    return res [::-1]

ans = []
for N in range(1, 10000):
    R = convert(N, 6)
    if N % 3 == 0:
        R = R + R[:2]
    else:
        R = R + convert(N % 3 * 10, 6)
    R = int(R, 6)
    if R > 680:
        ans.append(R)
print(min(ans))


