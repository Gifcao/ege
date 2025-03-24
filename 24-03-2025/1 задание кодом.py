from itertools import permutations

graph ='ag gb be ef fd dc ca cf ba'.split()
matrix ='246 16 57 15 347 127 356'.split()

for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)