from src.Output import Output
from src.Input import Input
import random

def random_solution(input_obj: Input) -> Output:
    vehicles2rides = {}
    rides_num = list(range(len(input_obj.rides)))
    random.shuffle(rides_num)
    while rides_num:
        for v in range(1, input_obj.vehicles+1):
            if not rides_num:break
            if v not in vehicles2rides:
                vehicles2rides[v] = []
            vehicles2rides[v].append(rides_num.pop())

    return Output(vehicles2rides)