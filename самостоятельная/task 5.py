for N in range(1,10000):
    R = bin(N)[2:]
    if R.count('1')%2==0:
        R = R + '1'
    else:
        R = R +'0'
    if int(R,2)%2==0:
        R = R +'10'
    else:
        R = R + '01'

    R =