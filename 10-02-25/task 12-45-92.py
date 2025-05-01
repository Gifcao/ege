for N in range(1, 10000):
    st = '>' +'0'*17 + '3'* N + '2' *17
    while '>3' in st or '>2' in st or '>0' in st:
        if '>3' in st:
            st = st.replace('>3', '22>', 1)
        if '>2' in st:
            st =st.replace('>2', '2>', 1)
        if '>0' in st:
            st = st.replace('>0', '3>', 1)
#проверка квадрата
    summ = sum(map(int,st[:-1]))
    if summ**0.5 == int(summ**0.5):
        print(N)
        break


