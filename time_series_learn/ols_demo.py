
import statsmodels.api as sm
Y = [1,3,4,5,2,3,4]
X = range(1,8)
X = sm.add_constant(X)
model = sm.OLS(Y,X)
results = model.fit()
print(results.params)
    # array([ 2.14285714,  0.25      ])
print(results.tvalues)
    # array([ 1.87867287,  0.98019606])
print(results.t_test([1, 0]))
