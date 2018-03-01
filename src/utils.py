from src.Input import Input
from src.Ride import Ride


def parse_input(filename):
    with open(filename) as f:
        input_obj = Input(*f.readline().strip().split(" "))
        rides = []
        for r in range(input_obj.rides):
            from_1, from_2, to_1, to_2, earliest_start, latest_finish = list(map(int,f.readline().strip().split(" ")))
            r = Ride(r, (from_1, from_2), (to_1, to_2), earliest_start, latest_finish)
            rides.append(r)

    input_obj.rides = rides
    return input_obj