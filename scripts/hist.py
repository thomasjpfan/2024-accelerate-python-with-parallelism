from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.datasets import make_regression

X_train, y_train = make_regression(n_samples=10_000, n_features=100, random_state=4)

hist = HistGradientBoostingRegressor(random_state=42)

hist.fit(X_train, y_train)
