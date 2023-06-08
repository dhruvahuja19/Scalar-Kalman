import argparse

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
  parser.add_argument('--Initial_state',help = 'Initial state of the system',
                        required = False,
                        default= 0)
  args = parser.parse_args()
  a = float(args.a)
  v_variance = float(args.v_variance)
  v_mean = float(args.v_mean)
  c = float(args.c)
  w_variance = float(args.w_variance)
  w_mean = float(args.w_mean)
  Initial_state = float(args.Initial_state)
  obj = skf.ScalarKFilter(a, v_variance, v_mean, c, w_variance, w_mean, Initial_state)
  run(obj)
def run(skf):
    """Continuously prompt the user for a measurement and update the filter"""
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




if __name__ == '__main__':
  main()
