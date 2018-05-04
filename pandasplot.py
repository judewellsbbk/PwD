import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    my_df = pd.DataFrame(some_filling(), columns=['A', 'B', 'C', 'D', 'E'])

    print my_df

    my_df['A'].plot()

    plt.show()

    # histogram of the bottom-right 3x3 submatrix
    #my_df[['C', 'D', 'E']][-3:].plot(kind='bar')

    #plt.show()


def some_filling():
    """ returns a 5x5 matrix of random integers from [low, high)
    """
    return np.random.randint(low=0, high=10, size=(200, 5))


main()

