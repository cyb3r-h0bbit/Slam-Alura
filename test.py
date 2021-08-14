import cudf
import numpy as npfrom cuml.linear_model import LogisticRegression

X = cudf.DataFrame()X['col1'] = np.array([1,1,2,2], dtype = np.float32)
X['col2'] = np.array([1,2,2,3], dtype = np.float32)y = cudf.Series( np.array([0.0, 0.0, 1.0, 1.0], dtype = np.float32) )# trainingreg = LogisticRegression()
reg.fit(X,y)

print("Coefficients:")
print(reg.coef_.copy_to_host())
print("Intercept:")
print(reg.intercept_.copy_to_host())# making predictionsX_new = cudf.DataFrame()X_new['col1'] = np.array([1,5], dtype = np.float32)
X_new['col2'] = np.array([2,5], dtype = np.float32)

preds = reg.predict(X_new)

print("Predictions:")
print(preds)
