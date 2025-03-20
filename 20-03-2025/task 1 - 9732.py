from itertools import permutations

graph = 'CG GA AD DB BF FC GE CE FE BE'.split()
matrix ='47 357 2567 16 236 345 123'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)