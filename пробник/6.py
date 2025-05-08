from turtle import*
tracer(0)
m=15
screensize(2000,2000)
lt(90)
for i in range(2):
    fd(5*m)
    lt(90)
    back(13*m)
    lt(90)
up()
bk(10*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(2):
    fd(11*m)
    rt(90)
    fd(7*m)
    rt(90)
up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(5,'red')
done()