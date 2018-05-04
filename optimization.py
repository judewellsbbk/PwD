elements = ['Platinum', 'Gold', 'Silver', 'Palladium']

instance = [[20, 711],
            [15, 960],
            [2000, 12],
            [130, 735]]

quantities, unit_prices = zip(*instance)

print quantities, unit_prices

coll = zip(elements, quantities, unit_prices)

print coll

import matplotlib as plt
import numpy

elements = ['Platinum', 'Gold', 'Silver', 'Palladium']

instance = [[20, 711],
            [15, 960],
            [2000, 12],
            [130, 735]]

W = 211


def main():
    """solves the Knapsack problem over a list of elements
        and a list of pairs [qty, unit_value]
        return the total value and the quantity for each element
        This version uses the instance AS A GLOBAL VARIABLE
    """

    quantities, unit_prices = zip(*instance)

    coll = zip(elements, quantities, unit_prices)

    collection = sorted(coll, key=lambda coll: coll[2], reverse=True)


    print collection
    # use W as a downwart counter
    value = 0

    avail = W

    # iterate from 0 the taking of metal
    # under constraint on
    # -the available bar, and
    # the remaining payload in the knapsack

    i = 0
    while avail > 0:

        if avail - collection[i][1] >= 0:

            avail -= collection[i][1]

            stolen = collection[i][1] * collection[i][2]
            value += stolen

            print 'steal GBP ' + str(stolen) + ' by taking the ' + collection[i][0] + ' bar'

            i += 1

        else:
            # we reached the first element that 'falls off' the knapsack
            break

    # consider cutting the last bar to the desired weight.

    value += avail * collection[i][2]

    print 'Finally, cut off ' + str(avail) + ' ounces of ' + collection[i][0]


# complete here with some meaningful print

main()