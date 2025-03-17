from itertools import product

cnt = 0
for i in product('IGROK',repeat=5):
    i =''.join(i)
    if len(i) == len(set(i)):
        if i [0] != 'K' and 'ROK' not in i:
            cnt +=1
print(cnt)
