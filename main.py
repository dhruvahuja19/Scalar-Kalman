import argparse
import os

from matplotlib import pyplot as plt

import ScalarKFilter as skf
def main():
  """Initialize a SclarKFilter Object based on user input"""

  parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
    '--a',
      help = 'Dynamics of the process. How X actually changes assuming no noise',
      required = False,
      default= 1)
  parser.add_argument('--v_variance',
                      help = 'Variance of the process noise',
                      required = False,
                      default= 1)
  parser.add_argument('--v_mean',
                      help = 'Mean of the process noise',
                      required = False,
                      default= 0)
  parser.add_argument('--c',
                      help = 'Dynamics of the observation',
                      required = False,
                      default= 1)
  parser.add_argument('--w_variance',
                      help = 'Variance of the measurement noise',
                      required = False,
                      default= 1)
  parser.add_argument('--w_mean',
                      help = 'Mean of the measurement noise',
                      required = False,
                      default= 0)
  parser.add_argument('--initial_state',help = 'Initial state of the system',
                        required = False,
                        default= 0)
  parser.add_argument('--estimation_variance',
                      help = 'Initial estimation variance of the system',
                        required = False,
                        default= 0)
  args = parser.parse_args()
  a = float(args.a)
  v_variance = float(args.v_variance)
  v_mean = float(args.v_mean)
  c = float(args.c)
  w_variance = float(args.w_variance)
  w_mean = float(args.w_mean)
  Initial_state = float(args.initial_state)
  estimationVariance = float(args.estimation_variance)
  obj = skf.ScalarKFilter(a, v_variance, v_mean, c, w_variance, w_mean, Initial_state, estimationVariance)
  run(obj)
import csv
import matplotlib.pyplot as plt

def run(skf):
    """Read measurements from a CSV file or text file, update the filter, and plot the difference"""

    try:
        with open("measurements.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            measurements = []
            true_states = []
            for row in reader:
                timestep = int(row[0])
                true_state = float(row[1])
                measurement = float(row[2])
                skf.predict()
                skf.update(measurement)
                filtered_state = skf.state
                difference = filtered_state - true_state
                print("Time Step:", timestep)
                print("Measurement:", measurement)
                print("True State:", true_state)
                print("Filtered State:", filtered_state)
                print("Difference:", difference)
                print("---------------------")
                measurements.append(measurement)
                true_states.append(true_state)

            # Plot the difference
            plt.plot(measurements, label="Measurements")
            plt.plot(true_states, label="True States")
            plt.xlabel("Time Step")
            plt.ylabel("Value")
            plt.title("Measurements and True States")
            plt.legend()
            plt.show()
    except FileNotFoundError:
        try:
            with open("measurements.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    measurement = float(line.strip())
                    skf.predict()
                    skf.update(measurement)
                    print("Measurement:", measurement)
                    print("State: ", skf.state)
                    print("---------------------")
        except FileNotFoundError:
            print("No measurement file found. Please provide measurements:")

            while True:
                try:
                    measurement = input("Enter a measurement or hit q to quit: ")
                    if measurement == 'q':
                        exit()
                    measurement = float(measurement)
                    skf.predict()
                    skf.update(measurement)
                    print("State: ", skf.state)
                except ValueError:
                    print("Please enter a valid number")
                    continue
                except KeyboardInterrupt:
                    print("Exiting...")
                    break

# Usage example
# Initialize the Kalman filter object (skf) and other necessary components
# ...
# Run the filter
# run(skf)


def show_plot(num_steps, filtered_states, measurements):
    plt.figure(figsize=(10, 6))
    plt.plot(range(num_steps), filtered_states, c='g', label='Filtered States')
    plt.scatter(range(num_steps), measurements, c='r', label='Measurements')
    plt.xlabel('Time Steps')
    plt.ylabel('State Value')
    plt.legend()
    plt.title('Kalman Filter')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
  main()
