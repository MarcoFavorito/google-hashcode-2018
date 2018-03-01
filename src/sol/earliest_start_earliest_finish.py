from src.Input import Input
from src.Output import Output
from src.Vehicle import Vehicle


def sol(input_obj: Input) -> Output:
    rides = sorted(input_obj.rides, key=lambda x: (x.earliest_start, x.latest_finish))

    num_vehicles = input_obj.vehicles

    id2vehicles = {k:Vehicle(k) for k in range(num_vehicles)}

    # first rides
    first_rides, second_rides = rides[:num_vehicles], rides[num_vehicles:]
    for v in range(num_vehicles):
        id2vehicles[v].rides.append(first_rides[v].id)


    current_rides = second_rides
    # second rides
    # while current_rides:
    #     pass


    o = Output({vehicle_id: vehicle.rides for vehicle_id, vehicle in id2vehicles.items()})
    return o
