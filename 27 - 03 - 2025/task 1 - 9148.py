from itertools import permutations

graph = 'аг аб бв ав вд дг гб гж жз же ед дз зе'.split()
matrix = '256 1458 478 237 126 158 348 2367'.split()

for i in permutations('абвгдежз'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)