#!/bin/usr/env python3
#kleo1:20180410:roulette.py

"""
A game of Russian roulette
"""

import random

start_chips=10
while start_chips > 0:
  b_chips=int(input("How many chips do you want to bet? "))
  b_number=int(input("Bet on a number between 0 and 10: "))
  b_color=input("Bet on Green, Red, or Black:  ")

  spin=random.randint(0,11)
  print("You have spun %i!"%spin)
  if spin == 0:
    color = 'Green'
  elif spin%2==0:
    color = 'Black'
  else:
    color = 'Red'

  winnings=0
  if b_number == spin:
    winnings=b_chips*10
  if b_color == color:
    winnings=winnings+b_chips*2
  else:
    start_chips=start_chips-b_chips
  print("Your chip balance is %i"%(start_chips+winnings))
  
  if (start_chips+winnings) < 0:
    print("GAME OVER")
    break

  ask=input("Do you want to play again? ")
  if ask == 'no':
    break
