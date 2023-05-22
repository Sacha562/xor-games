"""
This file contains an example of a basic semidefinite program.
"""

import numpy as np
import cvxpy as cp

n = 3
C = np.ones((n, n))
A = np.array([[[1, 0, 1], [0, 0, 7], [1, 7, 0]],
              [[0, 2, 0], [2, 6, 0], [0, 0, 4]]])
b = np.array([0, -2])

# Define and solve the CVXPY problem.
# Create a symmetric matrix variable.
X = cp.Variable((n, n), symmetric=True)

# The operator >> denotes matrix inequality.
constraints = [X >> 0]
constraints += [cp.trace(A[i] @ X) == b[i] for i in range(A.shape[0])]
prob = cp.Problem(cp.Minimize(cp.trace(C @ X)),
                  constraints)
prob.solve()

# Print result.
print("The optimal value is", prob.value)
print("A solution X is")
print(X.value)