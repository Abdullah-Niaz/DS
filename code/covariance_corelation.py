import numpy as np

X = [2, 3, 4, 5, 6]
Y = [4, 5, 6, 7, 8]

# Covariance matrix
cov_matrix = np.cov(X, Y, bias=True)
print("Covariance Matrix:\n", cov_matrix)

# Correlation coefficient matrix
corr_matrix = np.corrcoef(X, Y)
print("Correlation Matrix:\n", corr_matrix)
