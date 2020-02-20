#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # iterate through array with pointers
    a = 0
    b = 1
    profit = []
    for i in range(0, len(prices)-1):
        while a < (len(prices) - 1) and b < (len(prices)):
            profit.append(prices[b] - prices[a])
            b += 1
        if b > (len(prices) - 1):
            a += 1
            b = a + 1
        else:
            pass
    if len(prices) < 2:
        return 'List not large enough'
    return max(profit)


    # find difference between current index and values after
    # return greatest difference
list_of_prices = [10, 4, 11, 12, 15]
print(find_max_profit(list_of_prices))

# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
