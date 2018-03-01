from src.Input import Input
from src.Output import Output
from src.Vehicle import Vehicle
from src.utils import distance


def sol(input_obj: Input) -> Output:
    rides = sorted(input_obj.rides, key=lambda x: (x.earliest_start, x.latest_finish))

    num_vehicles = input_obj.vehicles

    vehicles = [Vehicle(k) for k in range(num_vehicles)]

    for ride in rides:
        # select vehicles for the current round
        best_vehicle = min(vehicles, key=lambda x: (distance(x.position, ride.from_cell), x.time))
        best_vehicle.rides.append(ride.id)
        best_vehicle.move(ride.to_cell)

    o = Output({v.id: v.rides for v in vehicles})
    return o
