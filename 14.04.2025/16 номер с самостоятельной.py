from functools import lru_cache
@lru_cache(None)
def f(n):
    if n >=2010: return n
    if n <2010: return f(n+3) +f(n+2) +f(n+1)
for i in range(1,2010):
    f(i)
print((f(2000) - 2*(f(2002) + f(2003)))/f(2004))
