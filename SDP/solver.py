import numpy as np
import cvxpy as cp

a_range = b_range = x_range = y_range = range(2)


def D_constructor(x, y):
    return q(x, y) * ((-1) ** f(x, y))


def f(x, y):
    return x * y


def q(x, y):
    return 0.25


D = np.matrix([[D_constructor(x, y) for y in y_range] for x in x_range])
I = np.identity(D.shape[0])

# Define and solve the CVXPY problem.
M = cp.Variable(D.shape)
R = cp.Variable(D.shape)
S = cp.Variable(D.shape)

# Create block matrix Z
Z = cp.bmat([[R, M], [cp.conj(M), S]])

# Create constraints of the problem
constraints = [Z >> 0]
constraints += [cp.diag(Z) == np.ones(Z.shape[0])]

# Solve the problem
problem = cp.Problem(cp.Maximize(cp.trace(cp.conj(D) @ M)),
                     constraints)
problem.solve()

# Print results.
print("The optimal bias is", problem.value)
print("The optimal winning probability is", 0.5 + problem.value / 2)
print("\nA solution M is")
print(M.value)

print("\nA solution Z is")
print(Z.value)
