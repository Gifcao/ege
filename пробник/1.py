from itertools import*

graph='ae eh hg gc cf fa ed df db bh bg'.split()
matrix='367 568 18 58 247 127 156 234'.split()

for i in permutations('abcdefhg'):
    if all(str(i.index(x)+1) in matrix [i.index(y)] for x,y in graph):
        print(*i)