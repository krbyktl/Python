#!/bin/usr/env python3
#kleo1:20180410:perceptron.py

"""
Compare output and expected.
"""

import perc_func
import random

w1=random.uniform(0,1)
w2=random.uniform(0,1)
w3=random.uniform(0,1)

r=0.2
T=((0,0,1,0),(1,0,1,1),(0,1,1,1),(1,1,1,1))

for n in range(200):
  my_t=random.choice(T)
  x1=my_t[0]
  x2=my_t[1]
  x3=my_t[2]
  ybar=my_t[3]
  y=perc_func.perc_output(x1,x2,x3,w1,w2,w3)
  perc_error=ybar-y
  w1=w1+r*perc_error*x1	
  w2=w2+r*perc_error*x2
  w3=w3+r*perc_error*x3
print(w1,w2,w3)
r1=open('OR.out','w')
for i in T:
  x1=i[0]
  x2=i[1]
  x3=i[2]
  r1.write("%i %i %i\n"%(x1,x2,perc_func.perc_output(x1,x2,x3,w1,w2,w3)))
r1.close()



