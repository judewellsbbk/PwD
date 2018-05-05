from __future__ import division
from numpy import *
import matplotlib.pyplot as plt



def compute_error_for_line_given_points(b, m, x_list, y_list):
    totalError = 0
    for i in range(0, len(x_list)):
        x = x_list[i]
        y = y_list[i]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(x_list))

def step_gradient(b_current, m_current, x_list, y_list, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(x_list))
    for i in range(0, len(x_list)):
        x = x_list[i]
        y = y_list[i]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(x_list, y_list, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, x_list, y_list, learning_rate)
    return [b, m]


def run():
    x_list = [i for i in range(10)]
    y_list = [i * -121 - 670 for i in x_list]
    learning_rate = 0.0001
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    num_iterations = 10000
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, x_list, y_list))
    print "Running..."
    [b, m] = gradient_descent_runner(x_list, y_list, initial_b, initial_m, learning_rate, num_iterations)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, x_list, y_list))
    fig, ax = plt.subplots()
    ax.scatter(x_list, y_list)
    slope = m
    ax.plot([0, x_list[-1]], [b, ((x_list[-1] * m)+b)], c='r')
    plt.show()


run()