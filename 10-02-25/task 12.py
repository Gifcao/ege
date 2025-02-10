# нашлось
a1 = '24'
a2 = '1234'
print(a1 in a2)

# заменить один раз
st = '12345678'
st = st.replace('1', '*')
print(st)

# заменить 1 раз
st = '1234567811'
st = st.replace('1', '*', 1)
print(st)


# формирование строки опрееделенной длины
st = '1' * 100
print(st)

# сумма цифр числа


# способ 1
summ = 0
for i in st:
    summ += int(i)
# способ 2
    summ = sum(int(i) for i in st)
# способ 3
    summ = sum(map(int, st))