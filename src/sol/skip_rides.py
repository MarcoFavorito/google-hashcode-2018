from src.Input import Input
from src.Output import Output
from src.Vehicle import Vehicle
from src.utils import distance


def sol(input_obj: Input) -> Output:
    rides = sorted(input_obj.rides, key=lambda x: (x.earliest_start, x.latest_finish, -distance(x.from_cell, x.to_cell)))

    num_vehicles = input_obj.vehicles

    id2vehicles = {k:Vehicle(k) for k in range(num_vehicles)}


    for ride in rides:
        # select vehicles for the current round
        current_vehicles = list(id2vehicles.values())
        compatible_vehicles = list(filter(lambda x: x.time + distance(x.position, ride.from_cell) < input_obj.steps, current_vehicles))
        if not compatible_vehicles:
            continue
        best_vehicle = min(compatible_vehicles, key=lambda x: (distance(x.position, ride.from_cell), x.time))
        id2vehicles[best_vehicle.id].rides.append(ride.id)
        id2vehicles[best_vehicle.id].move(ride.to_cell)

    o = Output({v.id: v.rides for v in id2vehicles.values()})
    return o
