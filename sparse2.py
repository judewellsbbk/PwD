from __future__ import division
from scipy import sparse
import random
import numpy as np
import time
from matplotlib import pyplot as plt



sample = np.array(range(0,75), dtype=np.uint8)
ary1 = np.random.choice(75,size=1000000, replace=True)
ary = np.array(np.random.choice(75,size=1000000, replace=True), dtype=np.uint8)
ary3 = np.random.choice(sample, size=1000000, replace=True)



def coo_m3(n):

    coords = np.array(range(0, n), dtype=np.uint32)
    no_of_data_points = random.randint(min(n * 10, n**2, 1000000), min(n * 50, 200000000))
    # print(no_of_data_points)

    row = np.random.choice(coords, no_of_data_points, replace=True)
    col = np.random.choice(coords, no_of_data_points, replace=True)
    col.sort()
    data = np.zeros(no_of_data_points,dtype='uint8')
    old_col_num = 0
    remaining_share = 100
    counter = 0
    for col_num in col:
        if row[counter] == col_num:
            counter += 1
            continue
        if col_num == old_col_num:
            if remaining_share > 0:
                allocation = random.randint(1, remaining_share)
                data[counter] += allocation
                remaining_share -= allocation

        else:
            if counter != 0:
                data[counter-1] += remaining_share
            remaining_share = 100
            old_col_num = col_num
            allocation = random.randint(1, remaining_share)
            data[counter] += allocation
            remaining_share -= allocation
        counter += 1
    data[counter - 1] += remaining_share


    return sparse.coo_matrix((data, (row, col)), shape=(n, n))


def coo_m4(n):

    coords = np.array(range(0, n), dtype=np.uint32)
    no_of_data_points = random.randint(min(n * 10, n**2, 1000000), min(n * 50, 200000000))
    # print(no_of_data_points)
    col = np.random.choice(coords, (no_of_data_points - len(coords)), replace=True)
    col = np.append(col, coords)
    row = np.random.choice(coords, no_of_data_points, replace=True)
    col.sort()
    # col_set = set(col)
    # coords_set = set(coords)
    # # if not coords_set.issubset(col_set):
    # #     print("not subset")
    # #     print('cols', col_set)
    # #     print('coords', coords_set)
    data = np.zeros(no_of_data_points,dtype='uint8')
    old_col_num = 0
    remaining_share = 100
    counter = 0
    for col_num in col:
        if row[counter] == col_num:
            counter += 1
            continue
        if col_num == old_col_num:
            if remaining_share > 0:
                allocation = random.randint(1, remaining_share)
                data[counter] += allocation
                remaining_share -= allocation

        else:
            col = np.append(col, old_col_num)
            row = np.append(row, (old_col_num + 1) % n)
            data = np.append(data, remaining_share)
            remaining_share = 100
            old_col_num = col_num
            allocation = random.randint(1, remaining_share)
            data[counter] += allocation
            remaining_share -= allocation
        counter += 1
    col = np.append(col, old_col_num)
    row = np.append(row, (old_col_num + 1) % n)
    data = np.append(data, remaining_share)


    return sparse.coo_matrix((data, (row, col)), shape=(n, n))


def matrix_converter(M):
    multiplier = np.array([100])
    M = np.array(M)
    M = M*multiplier
    return sparse.coo_matrix(M)



def corporate_control(matrix, s):
    control_positions = {s}

    new_control_positions = {s}

    col = []
    data = []

    def control_adder(matrix, positions, main_set, col, data):
        for comp in positions:
            c_row = sparse.find(matrix.getrow(comp))

            for co in c_row[1]:
                col.append(co)

            for da in c_row[2]:
                data.append(da)  # sums values of company ownership in a 1 row matrix for all companies controlled by c

        row = [0] * len(col)
        new_mtx = sparse.coo_matrix((data, (row, col)), shape=(1, matrix.shape[0]))

        sum_own_cols = set()
        for val in new_mtx.col:
            sum_own_cols.add(val) #  adds column integer for every company where (direct or indirect) control by c > zero
        to_be_checked = sum_own_cols.difference(main_set) #  removes all column integers where we already know c has control

        if len(to_be_checked) == 0 or all(c_share <= 50 for c_share in new_mtx.data):
            return main_set
        else:
            new_fifty_set = set()
            counter = 0
            for share_data in sparse.find(new_mtx)[2]: # iterates over every ownership value in the new matrix
                if share_data > 50:
                    new_fifty_set.add(sparse.find(new_mtx)[1][counter])  # when it finds an ownership > 50 it adds the column value to the set
                counter += 1
            new_fifty_set = new_fifty_set.intersection(to_be_checked)  # creates a set only containing column indexes of newly-discovered companies who are over 50% controlled
            if len(new_fifty_set) == 0:
                return main_set
            else:
                main_set.update(new_fifty_set)
                return control_adder(matrix, new_fifty_set, main_set, col, data) # add control shares of the newly discovered companies to the control matrix to see if any more companies are indirectly controlled

    add_column_control = control_adder(matrix, new_control_positions, control_positions, col, data)
    control_positions.update(add_column_control)

    return control_positions



# for i in range(100):
#     mtx = coo_m3(100)
#
#     if control_finder2(mtx, 0) != control_finder(mtx,0):
#         print('ERROR')

def step_gradient(b_current, m_current, x, y):

    learning_rate = 0.0000001
    b_grad = 0
    m_grad = 0
    n = float(len(x))
    for i in range(len(x)):
        x_val = x[i]

        y_val = y[i]
        # print('x val', x_val, 'y val', y_val)
        # error = y_val - (x_val * m_current + b_current)
        # print('error=', error)
        # b_grad2 = y_val - (x_val * (m_current) + b_current)
        b_grad += -(2/n) * (y_val - ((m_current * x_val) + b_current))
        print('b grad', b_grad)
        m_grad += -(2/n) * x_val * (y_val - ((m_current * x_val) + b_current))
        print('m grad', m_grad)
    new_b = b_current - (learning_rate * b_grad)
    new_m = m_current - (learning_rate * m_grad)
    return [new_b, new_m]

def gradient_calculator(m, b, x, y):
    h = 0.00001
    error = (y - ((x * m)+b)
    error_m_plus_h = (y - ((x * (m+h))+b)
    

def linear_regression(x, y):
    num_iterations = 10
    b = 0
    m = 0
    for i in range(num_iterations):
        print('b', b, 'm', m)
        b, m = step_gradient(b, m, x, y)
    return (b, m)

def time_test():
    k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    time_list = []
    n_val = [2**power for power in k]
    for n in n_val:
        print('n =', n)
        start = time.time()
        matrix = coo_m3(n)
        s = random.randint(0, n-1)
        corporate_control(matrix, s)
        total = time.time() - start
        time_list.append(total)
    fig, ax = plt.subplots()
    ax.scatter(n_val, time_list)
    b, m = linear_regression(np.asarray(n_val, dtype=np.float128), np.asarray(time_list, dtype=np.float128))
    y_1 = n_val[-1] * round(m, 3) + round(b, 3)
    print(y_1)
    ax.plot([n_val[0], n_val[-1]], [0, y_1], c='r')
    plt.show()
    return (n_val, time_list)



x, y = time_test()

# m = 0
# b = 0
#
# y_hat = [x_val * m + b for x_val in x]



# def error_calc(y, y_hat):
#     y = np.array(y)
#     y_hat = np.array(y_hat)
#     errors = y_hat - y
#     errors = errors**2
#     return sum(errors)
#
#
# print(error_calc(y, y_hat))



# matrix = coo_m3(5)
# print matrix.todense()
# print (sparse.find(matrix))
# print(control_finder2(matrix, 0))


def  matrix_checker(n):
    fail_count = 0
    for _ in range(n):
        M = coo_m4(4)
        size = M.shape[0]
        expected = [[100]*size]
        if not ((expected == M.sum(axis=0)).all()):
            print("FAIL:")
            print(M.todense())
            print(M.sum(axis=0))
            fail_count += 1
        if sum(M.diagonal()) != 0:
            print("FAIL:")
            print(M.todense())
            fail_count += 1
    print('FAIL COUNT:', fail_count)



# matrix_checker(10000)