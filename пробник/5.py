ans = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R =R + [len(R)//2:]