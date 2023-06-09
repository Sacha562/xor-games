import numpy as np
import cvxpy as cp
from toqito.nonlocal_games.xor_game import XORGame


def generate_bitstrings(n: int) -> list:
    """
    Function that generates all possible bitstrings of length n.
    """
    if n == 0:
        return [[]]
    else:
        previous_bitstrings = generate_bitstrings(n - 1)
        current_bitstrings = []
        for bitstring in previous_bitstrings:
            current_bitstrings.append(bitstring + [0])
            current_bitstrings.append(bitstring + [1])
        return current_bitstrings


def q_uniform():
    x_possibilities = len(x_values)
    y_possibilities = len(y_values)

    return 1 / (x_possibilities * y_possibilities)


def q(x, y):
    return q_uniform()


def f(x: list, y: list):
    return x[0] * y[0]


# This function shouldn't be changed
def V(a: int, b: int, x: list, y: list):
    return a ^ b == f(x, y)


def D_constructor(x: list, y: list):
    """
    :param x: Bitstring x (Alice). A list of integers.
    :param y: Bitstring y (Bob). A list of integers.
    """
    return q(x, y) * ((-1) ** f(x, y))


m = 1
n = 1

x_values = generate_bitstrings(m)
y_values = generate_bitstrings(n)

# Our own entangled value solver
D = np.matrix([[D_constructor(x, y) for y in y_values] for x in x_values])
M = cp.Variable(D.shape)
R = cp.Variable((len(x_values), len(x_values)))
S = cp.Variable((len(y_values), len(y_values)))
Z = cp.bmat([[R, M], [cp.conj(M).T, S]])
constraints = [Z >> 0]
constraints += [cp.diag(Z) == np.ones(Z.shape[0])]
problem = cp.Problem(cp.Maximize(cp.trace(cp.conj(D).T @ M)),
                     constraints)
problem.solve()
print('Our own entangled value is', 0.5 + problem.value / 2)


# Our own classical value solver
def create_strategies_shape(bitstring_length):
    shape = [-1]
    for _ in range(bitstring_length):
        shape.append(2)

    return shape


strategies_A = np.array(generate_bitstrings(2 ** m)).reshape(*create_strategies_shape(m))
strategies_B = np.array(generate_bitstrings(2 ** n)).reshape(*create_strategies_shape(n))
best_strategy = None
best_value = 0

for strategy_A in strategies_A:
    for strategy_B in strategies_B:
        sum = 0
        for x in x_values:
            for y in y_values:
                prob = q(x, y)
                a = strategy_A[(*x,)]
                b = strategy_B[(*y,)]
                sum += prob * V(a, b, x, y)
        if sum > best_value:
            best_value = sum
            best_strategy = {'A': strategy_A, 'B': strategy_B}

print('Our own classical value is', best_value)


# Toqito's entangled and classical value
prob_mat = np.array([[q(x,y) for y in y_values] for x in x_values])
pred_mat = np.array([[f(x,y) for y in y_values] for x in x_values])

game = XORGame(prob_mat, pred_mat)
print('Toqito\'s quantum value is', game.quantum_value())
print('Toqito\'s classical value is', game.classical_value())
