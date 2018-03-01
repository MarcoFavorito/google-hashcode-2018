import sys

from src.sol import earliest_start_earliest_finish, skip_rides
from src.sol.random_solution import random_solution
from src.utils import parse_input


def main():
    filename = sys.argv[1]
    input_obj = parse_input(filename)

    # o = random_solution(input_obj)
    # o = earliest_start_earliest_finish.sol(input_obj)
    o = skip_rides.sol(input_obj)
    print(str(o))



if __name__ == '__main__':
    main()
