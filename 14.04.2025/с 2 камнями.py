def f(x,s,m):
    if s + x >=259: return m%2==0
    if m==0: return 0
    h=[f(x+1, s,m-1),
       f(x*2, s,m-1),
       f(x, s+1,m-1),
       f(x,s*2,m-1)]
    return any(h) if m%2 !=0 else all(h)
print('19)',[s for s in range(1,259) if f(17,s,2)])
print('20)',[s for s in range(1,259) if not f(17,s,1) and f(17,s,3)])
print('21)',[s for s in range(1,259) if not f(17,s,2) and f(17,s,4)])

