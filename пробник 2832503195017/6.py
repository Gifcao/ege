from turtle import*
tracer(0)
m=15
screensize(2000,2000)
lt(90)
for i in range(100):
    fd(10*m)
    rt(180)
    fd(10*m)
    rt(198)
up()
for x in range(20,-20):
    for y in range(20,-20):
        goto(x*m, y*m)
        dot(5,'red')
done()