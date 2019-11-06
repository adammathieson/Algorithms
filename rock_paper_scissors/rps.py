#!/usr/bin/python

import sys

# def add_round(arr):

#   choice = ['rock', 'paper', 'scissors']

#   if len(arr) < 3:
#     for c in choice:
#       arr.append([c])
#       arr.append([c])
#       arr.append([c])
#   else:
#     pass
    # arr += arr.copy() + arr.copy()
    # arr.sort(
    # arr *= 3
    # arr.sort()
    # for i in arr:
    #   i *= 3

    # for i in arr:
    #   for c in choice:
    #     i.append(c)
    # arrA = arr.copy()
    # arr += arrA * 2
    # for i in arr:
    #   print(i)
    #   i

  # return arr


def rock_paper_scissors(n):
  choice = ['rock', 'paper', 'scissors']
  plays = []

  def add_round(n, play=[]):
    if n == 0:
      plays.append(play)
      return
    for c in choice:
      # print(c)
      add_round(n-1, play + [c])
      
  add_round(n, [])
  return plays

print(rock_paper_scissors(3))
