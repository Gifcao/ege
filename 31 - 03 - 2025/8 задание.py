from itertools import product
alph = sorted(set('лунатик'))

cnt=0
for i in product(alph, repeat =6):
    i=''.join(i)
    if i[0] =='н' and i.count('у') + i.count('а') + i.count('и') == 1:
        cnt+=1
        print(cnt, i)
