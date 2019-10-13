#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache = {i: 0 for i in range(n+1)}
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]


# def eating_cookies(n, cache=None):
  # res = [0] * (n + 1)
  # res[0] = 1
  # res[1] = 1
  # res[2] = 2

  # for i in range(3, n + 1):
  #   res[i] = res[i - 1] + res[i - 2] + res[i - 3]
  
  # ways = res[n]
  # return ways

  # if (n == 1 or n == 0):
  #   ways = 1
  # elif n == 2:
  #   ways = 2
  # else:
  #   ways = eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
  # return ways
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')