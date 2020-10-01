import numpy as np
from scipy import optimize


class LogisticRegression:
    def __init__(self):
        self.coef_ = []
        self.intercept_ = []
        self.theta = []

    def _sigmoid(self, z):
        z = np.array(z)
        g = 1 / (1 + np.exp(-z))
        return g

    def _costFunction(self, theta, X, y):
        m = y.shape[0]
        J = 0
        h = self._sigmoid(np.dot(X, theta))
        J = (1/m) * np.sum(- np.dot(y, np.log(h)) - (1-y).dot(np.log(1-h)))
        grad = (1/m) * (h-y).dot(X)
        return J, grad

    def fit(self, X, y, C=1, maxiter=1000):

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)

        theta = np.zeros(X.shape[1])
        options = {
            'maxiter': maxiter
        }

        res = optimize.minimize(self._costFunction,
                                theta,
                                (X, y),
                                jac=True,
                                method='TNC',
                                options=options
                                )
        theta = res.x
        self.theta.append(theta)
        self.coef_.append(theta[1:])
        self.intercept_.append(theta[0])

        self.theta = np.array(self.theta)
        self.coef_ = np.array(self.coef_)
        self.intercept_ = np.array(self.intercept_)
        return

    def predict(self, X):
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)

        h = self._sigmoid(np.dot(X, self.theta.T))
        y_pred = [int(round(i[0])) for i in h]
        return y_pred

    def accuracy_score(self, y_test, y_pred):
        accuracy = np.mean(y_test == y_pred)
        return accuracy