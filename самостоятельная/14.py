from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:32]:
    n1 = int('931' + x + '964', 32)
    n2 = int('4' + x + '51' + x + '1', 32)
    n3 = int('2861' + x + '637', 32)
    num = n1+n2+n3
    if num % 31==0:
        print(num//31)
