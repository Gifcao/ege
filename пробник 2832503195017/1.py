from itertools import*
graph='gb ba ad de ev vb dv'.split()
matrix='245 136 25 15 134 2'.split()

for i in permutations('abvgde'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
