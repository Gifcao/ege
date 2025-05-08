for n in range(3,10001):
    st = '3' + '5'*n
    while '333' in st or '555' in st:
        if '555' in st:
            st=st.replace('555','3',1)
        else:
            st=st.replace('333','5',1)

    summ = sum(int(i) for i in st)

    print(summ)