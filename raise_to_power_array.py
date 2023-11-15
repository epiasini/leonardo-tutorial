#!/usr/bin/env python
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


parser = argparse.ArgumentParser(description="Take in an integer N, defined as the i-th element of a pre-defined data array (N=data[i]) and raise it to the power a. By default, this will compute the square (a=2).")

parser.add_argument('input_id', metavar='i', type=int,
                    help="Index of the input to be evaluated")

parser.add_argument('--power', metavar='a', type=float, default=2,
                    help="Power to which you want to raise the integer (default: 2)")


if __name__ == '__main__':

    import numpy as np

    # hardcoded data array
    data = np.arange(-10, 11, 1, dtype=int)
    logging.info(f"The hardcoded data array is defined as {data}")
    
    args = parser.parse_args()
    logging.info(f"Done parsing the arguments. The argument dictionary is: {args}")
    
    result = np.power(args.input_id, args.power)

    print(f"Result: {result}")
