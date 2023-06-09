import random

# Define parameters
num_steps = 100  # Number of time steps
initial_state_mean = 20.0  # Initial state mean
initial_state_var = 5.0  # Initial state variance
process_noise_mean = 0.0  # Process noise mean
process_noise_var = 0.1  # Process noise variance
measurement_noise_mean = 0.0  # Measurement noise mean
measurement_noise_var = 1.0  # Measurement noise variance
a = 0.9  # Dynamics parameter
c = 1.2  # Observation parameter

# Initialize measurements list
measurements = []

# Generate true states and measurements
state = initial_state_mean
for _ in range(num_steps):
    # Generate process noise and add it to the state
    process_noise = random.gauss(process_noise_mean, process_noise_var)
    state = a * state + process_noise

    # Generate measurement noise and add it to the state
    measurement_noise = random.gauss(measurement_noise_mean, measurement_noise_var)
    measurement = c * state + measurement_noise

    # Append measurement to the list
    measurements.append(measurement)

# Write measurements to a text file
with open("measurements.txt", "w") as file:
    for measurement in measurements:
        file.write(str(measurement) + "\n")

# Print state space model parameters
print("State Space Model Parameters:")
print("----------------------------")
print("Dynamics parameter (a):", a)
print("Observation parameter (c):", c)
print("Process noise variance:", process_noise_var)
print("Measurement noise variance:", measurement_noise_var)
