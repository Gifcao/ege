from turtle import *
tracer(0)
screensize(2000,2000)
left(90)
m = 15

for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()

fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
down()

for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)

up()
for x in range(-10, 40):
    for y in range(-10, 40):
        goto(x*m, y*m)
        dot(10, 'white')
update()
done()