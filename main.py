import sys

from src.Input import Input
from src.Output import Output
from src.Ride import Ride
from src.sol.random_solution import random_solution


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        input_obj = Input(*f.readline().strip().split(" "))
        rides = []
        for r in range(input_obj.rides):
            from_1, from_2, to_1, to_2, earliest_start, latest_finish = list(map(int,f.readline().strip().split(" ")))
            r = Ride((from_1, from_2), (to_1, to_2), earliest_start, latest_finish)
            rides.append(r)

        input_obj.rides = rides

    # print(input_obj)

    o = random_solution(input_obj)
    print(o)



if __name__ == '__main__':
    main()