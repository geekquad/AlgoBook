import numpy as np

class PolynomialFeatures:
    def __init__(self, degree):
        self.degree = degree

    def fit_transform(self, X):
        """Fit the Polynomial Features into Input matrix."""
        degree = self.degree
        if X.ndim == 1:
            X_poly = np.zeros((X.shape[0], degree+1))
            for i in range(0, degree+1):
                X_poly[:, i] = X.flatten() ** i
        else:
            X_poly = np.ones((X.shape[0], 1))
            X_poly_temp = np.zeros((X.shape[0], degree))
            for j in np.split(X, X.shape[1], axis=1):
                for i in range(1, degree+1):
                    X_poly_temp[:, i-1] = j.flatten() ** i
                X_poly = np.concatenate([X_poly, X_poly_temp], axis=1)

        return X_poly


class LinearRegression:
    """Linear Regression Algorithm for Machine Learning."""

    def __init__(self):
        self.new_theta = []
        self.coef_ = []
        self.intercept_ = []

    def _computeCost(self, X, y, theta):
        m = X.shape[0]
        h = np.dot(X, theta)
        J = (1 / 2 * m) * np.sum(np.square(h-y))

        return J

    def _gradientDescent(self, X, y, theta, alpha, iterations):
        m = y.size
        J_history = []
        theta = theta.copy()
        for i in range(iterations):
            h = np.dot(X, theta)
            theta -= (alpha / m) * (h - y).dot(X)
            J_history.append(self._computeCost(X, y, theta))

        return theta, J_history

    def fit(self, X, y, cost=False, theta=False, alpha=0.01, iterations=1000):
        """
        Train the given model.
        Arguments
        -------
            X: nd-array
                Input Variables
            y: nd array
                Target/ Output variables
            cost: bool, default= False
                If true returns the array of costs of every iteration
            theta: nd array, default=False
                Initial values of theta, default is 0 for every theta
            alpha: float, default= 0.01
                Learning Rate
            iterations: int, default = 1000
                Number of iterations in gradient descent
        """

        new_theta = self.new_theta
        coef_ = self.coef_
        intercept_ = self.intercept_

        if X.ndim == 1:
            X = X.reshape(-1, 1)

        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)

        if not theta:
            theta = np.zeros(X.shape[1])

        theta, J_history = self._gradientDescent(
            X, y, theta, alpha, iterations)
        for i in theta:
            new_theta.append(i)

        coef_ = np.array(coef_.append(new_theta[1:]))
        intercept_ = np.array(intercept_.append(new_theta[0]))
        new_theta = np.array(new_theta)
        pass

    def predict(self, X):
        """
            Predict y for given X according to trained model.
            Parameters
            ----------
                X: ndarray
                    Input test array
            Returns
            ------
                y_pred: ndarray
                    Predicted value of y for X.
        """
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
        theta = self.new_theta
        y_pred = np.dot(X, theta)
        return y_pred
