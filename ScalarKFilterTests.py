import unittest
import numpy as np
import matplotlib.pyplot as plt
import ScalarKFilter as skf

class MyTestCase(unittest.TestCase):
     # add assertion here
    def generate_test_data(self, num_steps, initial_state_mean, initial_state_var, process_noise_mean, process_noise_var,
                           measurement_noise_mean, measurement_noise_var, a, c):
        # Generate true state trajectory
        true_states = [initial_state_mean]
        for _ in range(num_steps - 1):
            #X_{k+1} = a * X_k + v
            state = a * true_states[-1] + np.random.normal(process_noise_mean, np.sqrt(process_noise_var))
            true_states.append(state)

        # Generate noisy measurements
        measurements = [c * state + np.random.normal(measurement_noise_mean, np.sqrt(measurement_noise_var))
                        for state in true_states]

        return true_states, measurements
    def test1(self):

        # Define parameters
        num_steps = 100
        initial_state_mean = 20.0  # Initial state mean
        initial_state_var = 5.0  # Initial state variance
        process_noise_mean = 0  # Process noise mean
        process_noise_var = .1  # Process noise variance
        measurement_noise_mean = 5  # Measurement noise mean
        measurement_noise_var = 2  # Measurement noise variance
        a = 0.9  # Dynamics parameter
        c = 1.2  # Observation parameter

    # Generate test data
        true_states, measurements = self.generate_test_data(num_steps, initial_state_mean, initial_state_var,
                                                       process_noise_mean, process_noise_var,
                                                       measurement_noise_mean, measurement_noise_var,
                                                       a, c)
        # Initialize Kalman filter okbject defined in SacaarKFilter.py
        kf = skf.ScalarKFilter(a, process_noise_var, process_noise_mean, c, measurement_noise_var,
                               measurement_noise_mean, initial_state_mean, initial_state_var)
        # Initialize lists to store filter estimates
        filtered_states = []
        filtered_state_covariances = []
        for measurement in measurements:
            kf.predict()
            kf.update(measurement)
            filtered_states.append(kf.state)
            filtered_state_covariances.append(kf.estimationVariance)
        self.show_plot(num_steps, true_states, filtered_states, measurements)
        # Plot filtered states and measurements versus time
    def show_plot(self, num_steps, true_states, filtered_states, measurements):
        plt.figure(figsize=(10, 6))
        plt.plot(range(num_steps), true_states, label='True States')
        plt.plot(range(num_steps), filtered_states, c='g', label='Filtered States')
        plt.scatter(range(num_steps), measurements, c='r', label='Measurements')
        plt.xlabel('Time Steps')
        plt.ylabel('Temperature')
        plt.legend()
        plt.title('Kalman Filter')
        plt.grid(True)
        plt.show()



if __name__ == '__main__':
    unittest.main()
