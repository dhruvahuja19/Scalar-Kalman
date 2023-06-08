class ScalarKFilter():
    def __init__(self, a, v_variance, v_mean, c, w_variance,w_mean, state=None):
        """
        Initialize the Kalman filter based on the following model
        x_{k+1} = a * x_k + v
        y_k = c * x_k + w
        :param a: Dynamics of the process. How X actually changes assuming no noise
        :param v: Variance of the process noise
        :param c: Dynamics of the observation.
        :param w: Variance of the measurement noise
        :param state: Our best guess of X(X_hat))
        """
        self.a = a
        self.v_variance = v_variance
        self.c = c
        self.w_variance = w_variance
        self.v_mean = v_mean
        self.w_mean = w_mean
        self.K = 0
        if state is None:
            self.state = 0
        else:
            self.state = state
        self.estimationVariance = 0


    def predict(self):
        #Update X_hat(n| n -1) and Sigma(n|n-1)
        self.state = self.a * self.state + self.v_mean
        self.estimationVariance = self.a**2 * self.estimationVariance + self.v_variance
        self.K = self.estimationVariance * self.c / (self.c**2 * self.estimationVariance + self.w_variance)

    def update(self, measurement):
        innovation = measurement - self.c * self.state - self.w_mean
        self.state = self.state + self.K * innovation
        self.estimationVariance = (1 - self.K * self.c) * self.estimationVariance

