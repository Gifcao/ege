def convert(num,sys):
    res =''
    while num:
        res+=str(num%sys)
        num//=sys
    return res [::-1]

num = 2 * 729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 -338
ans = convert(num,9)
ans = len(ans) - ans.count('0')
print(ans)