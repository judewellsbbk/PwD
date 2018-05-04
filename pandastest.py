import numpy  as np
import pandas as pd


def main():
    my_dict = {'A': [1, 2], 'B': ['John', 4]}

    my_data_frame = pd.DataFrame(data=my_dict)

    print my_data_frame

    print my_data_frame.dtypes

    # a further demo

    my_df = pd.DataFrame(some_filling(), columns=['A', 'B', 'C', 'D', 'E'])

    print my_df


def some_filling():
    """ returns a 5x5 matrix of random integers from [low, high)
    """
    return np.random.randint(low=0, high=10, size=(5, 5))



main()