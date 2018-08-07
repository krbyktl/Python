#!/bin/usr/env python3
#kleo1:20180409:perc_func.py

"""
Machine learning with a perceptron!
"""

def weight_sum(x1,x2,x3,w1,w2,w3):
  S=x1*w1+x2*w2+x3*w3
  return S

def step_func(S):
  if S >= 0:
    return 1
  else:
    return 0


def perc_output(x1,x2,x3,w1,w2,w3):
  y=step_func(weight_sum(x1,x2,x3,w1,w2,w3))
  return y

if __name__=="__main__":
  print(perc_output(0,1,1,0.2,0.4,0.2))

