#!/usr/bin/env python
import argparse
import logging


parser = argparse.ArgumentParser(description="Take in an integer N and raise it to the power a. By default, this will compute the square (a=2).")

parser.add_argument('integer', metavar='N', type=int,
                    help="An integer for the calculation")

parser.add_argument('--power', metavar='a', type=float, default=2,
                    help="Power to which you want to raise the integer (default: 2)")

if __name__ == '__main__':

    import numpy as np
   
    args = parser.parse_args()
    logging.info(f"Done parsing the arguments. The argument dictionary is:\n{args}")
    
    result = np.power(args.integer, args.power)

    print(f"Result: {result}")
