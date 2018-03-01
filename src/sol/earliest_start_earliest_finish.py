from src.Input import Input
from src.Output import Output


def sol(input_obj: Input) -> Output:
    rides = sorted(input_obj.rides, key=lambda x: (x.earliest_start, x.latest_finish))

    num_vehicles = input_obj.vehicles
    vehicles2rides = {k:[] for k in range(num_vehicles)}

    # first rides
    first_rides, second_rides = rides[:num_vehicles+1], rides[num_vehicles+1:]
    for v in range(num_vehicles):
        vehicles2rides[v] = first_rides[v]

    # second rides




    return Output(vehicles2rides)
