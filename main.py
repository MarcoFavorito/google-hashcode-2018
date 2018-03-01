import sys

from src.sol.random_solution import random_solution
from src.utils import parse_input


def main():
    filename = sys.argv[1]
    input_obj = parse_input(filename)

    o = random_solution(input_obj)
    print(o)



if __name__ == '__main__':
    main()