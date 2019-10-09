#!/usr/bin/python

# import argparse

def find_max_profit(prices):
  profit_list = []
  profit = None
  for i in range(len(prices)):
    if len(prices[i+1:]) > 0:
      print(prices[i], prices[i+1:])
      for j in prices[i+1:]:
        profit_list.append(j - prices[i])
    profit_list.sort()
    print("return", profit_list[-1])
    profit = profit_list[-1]
    print(profit)
  return profit


  

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

test = [10, 7, 5, 8, 11, 9]

find_max_profit(test)