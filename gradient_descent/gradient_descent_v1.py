import numpy as np


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iteration = 10
    n = len(x)
    learning_rate = 0.1

    for i in range(iteration):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val ** 2 for val in (y-y_predicted)])
        md = -(2/n) * sum(x * (y-y_predicted))
        bb = -(2/n) * sum((y-y_predicted))
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bb
        print("m {},c {}, b {}, iteration {}".format(m_curr, cost, b_curr, i))


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)


