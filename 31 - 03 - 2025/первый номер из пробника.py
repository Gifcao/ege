from itertools import  permutations

graph = 'bf fd dc ch hg ge eb ba da ac ag'.split()
matrix = '36 478 178 258 46 158 23 2346'.split()

for i in permutations('abcdefgh'):
    if all(str(i.index(x)+1) in matrix [i.index(y)] for x,y in graph):
        print(*i)

