"""
This program calculates the winning probability of the CHSH game, based on a
specific set of measurements as defined in get_measurement().

- The winning condition function can be modified in the f() function.
- The shared state can be modified in the state() function.
- The measurements used by Alice and Bob can be modified in the get_measurement() function.
- The x,y distribution can be modified in q(). The ranges of the parameters can also be altered.

For more information, please read section A.2 of the thesis document.
"""

import math

import numpy as np


def get_computational_ket(n):
    vec = np.zeros((2, 1), float)
    vec[n, :] = 1
    return vec


def get_hadamard_ket(n):
    if n == '+':
        return (compb[0] + compb[1]) / math.sqrt(2)
    elif n == '-':
        return (compb[0] - compb[1]) / math.sqrt(2)


compb = [np.matrix(get_computational_ket(n)) for n in range(2)]
hadb = [np.matrix(get_hadamard_ket(n)) for n in ['+', '-']]

a_range = b_range = x_range = y_range = range(2)


def f(x, y):
    """
    Part of winning condition: f(x, y) must equal a ^ b to win.
    """
    return x * y


def q(x, y):
    """
    Distribution function. Returns probability of a combination of x and y.
    """
    return 0.25


def V(a, b, x, y):
    """
    Winning condition.
    Returns 1 when the players win, 0 when they lose.
    """
    return f(x, y) == a ^ b


def state():
    """Returns the quantum state Alice and Bob will be using."""
    return (np.kron(compb[0], compb[0]) + np.kron(compb[1], compb[1])) / math.sqrt(2)


def get_measurement(player, input, direction):
    """
    :param player: 0 for Alice, 1 for Bob
    :param input: input bitstring the player receives
    :param direction: on which axis of the measurement basis the measurement is performed. 0 for first axis, 1 for second.
    :return: a measurement operator.
    """
    if player == 0:
        if input == 0:
            return [compb[0] @ compb[0].H, compb[1] @ compb[1].H][direction]
        elif input == 1:
            return [hadb[0] @ hadb[0].H, hadb[1] @ hadb[1].H][direction]
    elif player == 1:
        c = math.cos(math.pi / 8)
        s = math.sin(math.pi / 8)
        if input == 0:
            v1_ket = c * compb[0] + s * compb[1]
            v2_ket = -s * compb[0] + c * compb[1]
            return [v1_ket @ v1_ket.H, v2_ket @ v2_ket.H][direction]
        elif input == 1:
            w1_ket = c * compb[0] - s * compb[1]
            w2_ket = s * compb[0] + c * compb[1]
            return [w1_ket @ w1_ket.H, w2_ket @ w2_ket.H][direction]


def p(a, b, x, y):
    """Returns the probability of Alice and Bob returning a, b given x, y."""
    m_alice = get_measurement(0, x, a)
    m_bob = get_measurement(1, y, b)

    return (state().H @ np.kron(m_alice, m_bob) @ state()).item()


def calculate_winning_probability():
    combinations = np.array(np.meshgrid(a_range, b_range, x_range, y_range)).T.reshape(-1, 4)

    sum = 0
    for (a, b, x, y) in combinations:
        sum += q(x, y) * V(a, b, x, y) * p(a, b, x, y)

    return sum


result = calculate_winning_probability()
print(result)
