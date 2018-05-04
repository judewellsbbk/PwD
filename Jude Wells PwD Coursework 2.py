from __future__ import division
from random import randint
from random import sample
from random import random
from random import shuffle
from time import time
from matplotlib import pyplot as plt
from numpy import shape
from numpy import zeros


def MatrixGen(n_companies):
    matrix = []
    for row in range(n_companies):
        split_proportions = sample(range(0,n_companies), n_companies)
        denominator = sum(split_proportions)
        company_ownership = [round((i / denominator), 2) for i in split_proportions]
        matrix.append(company_ownership)

    print(matrix)

    rotated_matrix = map(list, zip(*matrix))

    print(rotated_matrix)

    for n in range(n_companies):
        rotated_matrix[n][n] = 0

    print(rotated_matrix)


def MatrixGen2(n_companies):
    matrix = []
    for row in range(n_companies):
        remaining_share = 1
        company_ownership = []
        for company in range(n_companies):
            share = round((remaining_share * random()), 2)
            company_ownership.append(share)
            remaining_share = max(remaining_share - share, 0)  # Prevents negative numbers caused by rounding
            shuffle(company_ownership)  # Un-does the bias for companies with a lower matrix index having higher ownership rates.
        matrix.append(company_ownership)

    print(matrix)

    rotated_matrix = map(list, zip(*matrix))

    for n in range(n_companies):
        rotated_matrix[n][n] = 0

    print(rotated_matrix)


def MatrixGen3(n_companies, Markovian = True):
    matrix = []
    for row in range(n_companies):
        remaining_share = 1
        company_ownership = []
        for company in range(n_companies - 1):
            share = round((remaining_share * random()), 2)
            company_ownership.append(share)
            remaining_share = max(remaining_share - share, 0)  # Prevents negative numbers caused by rounding
        if Markovian:
            unclaimed_share = round((1 - sum(company_ownership)), 2)
            company_ownership[randint(0, (n_companies - 2))] += unclaimed_share
        shuffle(company_ownership)  # Un-does the bias for companies with a lower matrix index having higher ownership rates.
        matrix.append(company_ownership)


    column_position = 0
    for row in matrix:
        row.insert(column_position, 0)
        column_position += 1

    rotated_matrix = map(list, zip(*matrix))

    return rotated_matrix


def MatrixGen4(n_companies, Markovian = True):
    matrix = []
    for row in range(n_companies):
        remaining_share = 1
        company_ownership = []
        counter = n_companies
        for company in range(counter):
            counter -= 1
            if remaining_share < 0.01:
                zero_list = [0] * (counter)
                company_ownership = company_ownership + zero_list
                break
            share = round((remaining_share * random()), 2)
            company_ownership.append(share)
            remaining_share = max(remaining_share - share, 0)  # Prevents negative numbers caused by rounding
        if Markovian:
            unclaimed_share = round((1 - sum(company_ownership)), 2)
            company_ownership[randint(0, (n_companies - 2))] += unclaimed_share
        shuffle(company_ownership)  # Un-does the bias for companies with a lower matrix index having higher ownership rates.
        matrix.append(company_ownership)

    column_position = 0
    for row in matrix:
        row.insert(column_position, 0)
        column_position += 1

    rotated_matrix = map(list, zip(*matrix))

    return rotated_matrix


def MatrixGen5(n_companies):
    matrix = zeros((n_companies, n_companies), dtype=int)
    for row in range(len(matrix)):
        remaining_share = 1
        while remaining_share > 0.05:
            row, column = randint(0, n_companies-1), randint(0, n_companies-1)
            allocation = remaining_share * random()
            matrix[row][column] += allocation
            print matrix[row][column]
            remaining_share -= allocation
    return(matrix)


def MatrixGen6(n_companies):
    matrix = zeros((n_companies, n_companies), dtype= 'uint8')
    for row in range(len(matrix)):
        remaining_share = 100
        while remaining_share > 5:
            row, column = randint(0, n_companies-1), randint(0, n_companies-1)
            allocation = randint(5, 100)
            matrix[row][column] += allocation
            remaining_share -= allocation
        if row % 100000 == 0:
            print(row)
    return(matrix)


def Control_Finder(matrix, s):
    for row in matrix:
        row[s] = 0
    matrix[s][s] = 1
    control_positions = set()
    def recursive_checker(matrix, control_positions, s_row):
        company_column = 0
        control_positions.add(s_row)
        for company in matrix[s_row]:
            if company > 0.5:
                if company_column not in control_positions:
                    control_positions.add(company_column)
                    control_positions.update(recursive_checker(matrix, control_positions, company_column))
            company_column += 1
        return(control_positions)
    return(recursive_checker(matrix, control_positions, s))

print('\n')
print('\n')



def time_test():
    k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    time_list = []
    for power in k:
        n = 2**power
        print('n =', n)
        matrix = MatrixGen4(n, Markovian=False)
        s = randint(0, n-1)
        start = time()
        Control_Finder(matrix, s)
        total = time() - start
        time_list.append(total)
    print(time_list)
    plt.plot(time_list)
    plt.show()

# time_test()

def matrix_gen_time():
    k = [4] * 10
    time_list_3 = []
    time_list_4 = []
    for power in k:
        n = 5**power
        start = time()
        matrix = MatrixGen3(n, Markovian=False)
        total = time() - start
        time_list_3.append(total)

    for power in k:
        n = 5**power
        start = time()
        matrix = MatrixGen4(n, Markovian=False)
        total = time() - start
        time_list_4.append(total)

    print("mat3", sum(time_list_3))
    print("mat4", sum(time_list_4))

def test_numpy(n):
    k = []
    timing = []
    for i in range(1):
        start = time()
        M = MatrixGen6(n)
        total = time() - start
        print(total)
        timing.append(total)
        print(shape(M))
        #print(M[1])

    print("time", timing)
    print(M.nbytes)
    # print(M[1][0:1000])
    # print(M[2][0:1000])
    # print(M[3][0:1000])
    # print(M[4][0:1000])
    # print(M[-1][0:1000])
    # print(M[-2][0:1000])


#test_numpy(10000000)


#matrix_gen_time()

def company_allocation_probability():
    number_of_allocations = []
    for i in range (50000):
        share = 100
        counter = 0
        while share > 0:
            share -= randint(1, share)
            counter += 1
        number_of_allocations.append(counter)
    print('average allocations = ', sum(number_of_allocations) / len(number_of_allocations))
    plt.hist(number_of_allocations, bins=10)
    plt.show()


company_allocation_probability()