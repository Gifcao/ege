from turtle import *
tracer(0)
screensize(2000,2000)
left(90)
m = 15

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(20 * m)
    rt(90)
up()

fd(8 * m)
rt(90)
back(3 * m)
lt(90)
down()

for i in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)
up()
for x in range(-10, 40):
    for y in range(-10, 40):
        goto(x*m, y*m)
        dot(3, 'red')

done()


