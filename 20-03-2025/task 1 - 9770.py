from itertools import permutations

graph = 'ac cf fd dh hg ga ab cb be ed'.split()
matrix ='56 378 26 68 17 134 258 247'.split()

for i in permutations('abcdefhg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)