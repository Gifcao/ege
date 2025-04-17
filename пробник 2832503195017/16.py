from functools import lru_cache
@lru_cache(None)
def f(n):
    if n >= 4040: return n
    if n < 4040: return n+4+f(n+4)
for i in range(5000,1,-1):
    f(i)
print(f(3) - f(15))