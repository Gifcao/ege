from itertools import permutations

graph = 'ab bc cf fg ge ea ed da db dc df'.split()
matrix = '23576 145 146 23 127 137 156'.split()

for i in permutations ('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)]for x, y in graph):
        print(*i)
