from src.Input import Input
from src.Output import Output
from src.Vehicle import Vehicle
from src.utils import distance


def sol(input_obj: Input) -> Output:
    rides = sorted(input_obj.rides, key=lambda x: (x.earliest_start, x.latest_finish))

    num_vehicles = input_obj.vehicles

    id2vehicles = {k:Vehicle(k) for k in range(num_vehicles)}

    # first rides
    first_rides, second_rides = rides[:num_vehicles], rides[num_vehicles:]
    for v in range(num_vehicles):
        current_ride = first_rides[v]
        current_vehicle = id2vehicles[v]
        current_vehicle.rides.append(current_ride.id)
        current_vehicle.move(current_ride.to_cell)

    # already sorted
    current_rides = second_rides

    # list of vehicles for current round
    current_round_vehicles = id2vehicles.values()

    # second rides
    for ride in current_rides:
        # select vehicles for the current round
        best_vehicle = min(current_round_vehicles, key=lambda x: distance(x.position, ride.from_cell))
        best_vehicle.rides.append(ride.id)
        best_vehicle.move(ride.to_cell)



    o = Output({vehicle_id: vehicle.rides for vehicle_id, vehicle in id2vehicles.items()})
    return o
