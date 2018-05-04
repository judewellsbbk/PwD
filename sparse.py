from scipy import sparse
import random
import numpy as np
import time


sample = np.array(range(0,75), dtype=np.uint8)
ary1 = np.random.choice(75,size=1000000, replace=True)
ary = np.array(np.random.choice(75,size=1000000, replace=True), dtype=np.uint8)
ary3 = np.random.choice(sample, size=1000000, replace=True)


def coo_m(n):
    ownership_range = np.array(range(1,75), dtype=np.uint8)
    coords = np.array(range(0,n), dtype=np.uint16)
    no_of_data_points = random.randint(min(n*2, 60000), min(n**2, 65535))
    print(no_of_data_points)
    data = np.random.choice(ownership_range, size=no_of_data_points, replace=True)
    row = np.random.choice(coords, no_of_data_points, replace=True)
    col = np.random.choice(coords, no_of_data_points, replace=True)
    return sparse.coo_matrix((data, (row, col)), shape=(n, n))

def coo_m2(n):
    ownership_range = np.array(range(1,75), dtype=np.uint8)
    coords = np.array(range(0,n), dtype=np.uint32)
    no_of_data_points = random.randint(min(n*2, 60000), min(n**2, 200000000))
    print(no_of_data_points)
    data = np.random.choice(ownership_range, size=no_of_data_points, replace=True)



    row = np.random.choice(coords, no_of_data_points, replace=True)
    col = np.random.choice(coords, no_of_data_points, replace=True)
    col.sort()

    return sparse.coo_matrix((data, (row, col)), shape=(n, n))


def coo_m3(n):
    ownership_range = np.array(range(1, 75), dtype=np.uint8)
    coords = np.array(range(0, n), dtype=np.uint32)
    no_of_data_points = random.randint(min(n * 10, n**2, 1000000), min(n * 100, 200000000))
    # print(no_of_data_points)

    row = np.random.choice(coords, no_of_data_points, replace=True)
    col = np.random.choice(coords, no_of_data_points, replace=True)
    col.sort()
    data = np.zeros(no_of_data_points,dtype='uint8')
    old_col_num = 0
    remaining_share = 100
    counter = 0
    for col_num in col:
        if col_num == old_col_num:
            if remaining_share > 0:
                allocation = random.randint(1, remaining_share)
                data[counter] += allocation
                remaining_share -= allocation

        else:
            data[counter-1] += remaining_share
            remaining_share = 100
            old_col_num = col_num
            allocation = random.randint(1, remaining_share)
            data[counter] += allocation
            remaining_share -= allocation
        counter += 1
    data[counter - 1] += remaining_share


    return sparse.coo_matrix((data, (row, col)), shape=(n, n))


def control_finder(matrix, c):
    control_positions = set()

    def recursive_checker(matrix, control_set, s):
        c_row = sparse.find(matrix.getrow(s))
        col_index = 0
        control_set.add(s)
        for share in c_row[2]:
            if share > 50:
                share_col_index = c_row[1][col_index]
                if share_col_index not in control_set:
                    control_set.add(share_col_index)
                    control_set.update(recursive_checker(matrix, control_set, share_col_index))
            col_index += 1
        return (control_set)


    over_fifty_control = recursive_checker(matrix, control_positions, c)
    print("+50", over_fifty_control)

    row = []
    col = []
    data = []
    def control_adder(matrix, positions, over_fifty_control, row, col, data):
        for comp in positions:
            c_row = sparse.find(matrix.getrow(comp))

            for ro in c_row[0]:
                row.append(ro)

            for co in c_row[1]:
                col.append(co)

            for da in c_row[2]:
                data.append(da)

        new_mtx = sparse.coo_matrix((data, (row, col)), shape=(1, matrix.shape[0]))
        print(new_mtx.todense(), '\n')

        print(sparse.find(new_mtx))

        sum_own_cols = set()
        print('new m col', new_mtx.col)
        for val in new_mtx.col:
            sum_own_cols.add(val)
        print('sum own cols', sum_own_cols)
        to_be_checked = sum_own_cols.difference(over_fifty_control)
        print('to be checked', to_be_checked)

        if len(to_be_checked) == 0 or all(c_share <= 50 for c_share in new_mtx.data):
            print('No more checks required')
            return over_fifty_control
        else:
            new_fifty_set = set()
            counter = 0
            for share_data in sparse.find(new_mtx)[2]:
                if share_data > 50:
                    new_fifty_set.add(sparse.find(new_mtx)[1][counter])
                counter += 1
            print ('new fifty set', new_fifty_set)
            new_fifty_set = new_fifty_set.intersection(to_be_checked)
            print ('new fifty set', new_fifty_set)
            if len(new_fifty_set) == 0:
                print('No more checks required')
                return over_fifty_control
            else:
                over_fifty_control.update(new_fifty_set)
                print('****LOOOP*****')
                return control_adder(matrix, new_fifty_set, over_fifty_control, row, col, data)
    add_column_control = control_adder(matrix, over_fifty_control, over_fifty_control, row, col, data)
    over_fifty_control.update(add_column_control)
    print('add column control', add_column_control)
    return over_fifty_control






row_0_count = 0
row_13_count = 0



# for i in range(0):
#     start = time.time()
#     mtx = coo_m3(100)
#     total = time.time() - start
#
#     row_13 = mtx.getrow(13).toarray()
#     row_0 = mtx.getrow(0).toarray()
#
#
#     if any(o > 50 for o in row_0[0]):
#             row_0_count += 1
#
#     if any(o > 50 for o in row_13[0]):
#             row_13_count += 1


mtx = coo_m3(6)
print(mtx.todense())
print('FINAL ANSWER', control_finder(mtx, 0))