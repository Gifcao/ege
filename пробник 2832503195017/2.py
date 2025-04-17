from itertools import *
 def f(w,x,y,z):
     return z or (not(w <= x)) or ((not z) <= (not y))
 