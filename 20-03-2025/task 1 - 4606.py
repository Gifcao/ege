from itertools import permutations

graph = 'CE EG GF FA AC CD DH HE AB FB'.split()
matrix ='68 47 45 237 368 15 248 157'.split()

for i in permutations('ABFGEHDC'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)