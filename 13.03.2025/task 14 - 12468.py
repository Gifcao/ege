from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:19]:
    num1 = int('78' + x + '79643', 19)
    num2 = int('25' + x + '43', 19)
    num3 = int('63' + x + '5', 19)
    num = num1 + num2 + num3
    if num %18 ==0:
        print(num//18)
