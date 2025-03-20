from itertools import permutations

graph = 'DE GE GC CF FA AD AB BE FB'.split()
matrix = '37 367 125 56 34 247 126'.split()

for i in permutations('ABGECDF'):
    if all(str(i.index(x) +1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
