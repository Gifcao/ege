def f(cur, end):
    if cur == end: return 1
    if cur < end or cur==24: return 0
    return f(cur-2, end) + f(cur-3,end) + f(cur%4,end)
print(f(36,13))