from scipy.optimize import linprog

# coeficients of the objective function
# (since initial task statement is to maximaize the objective function,
# it is necessary to multiply the coeficients by (-1))
obj = [-2, 1]
# left side coeficients of the inequity constraints
lhs_ineq = [
    [1, 1],
    [2, -2],
    [2, 1],
    [3, 2]
]
# right sides of the inequity constraints
rhs_ineq = [
    1,
    1,
    2,
    3
]

# minimize the objective function
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")

print("x1 = ", opt.x[0])
print("x2 = ", opt.x[1])
# since initial task statement is to maximaize the objective function,
# it is necessary to multiply the result value by (-1)
print("F(x1, x2) = ", (-1) * opt.fun)
