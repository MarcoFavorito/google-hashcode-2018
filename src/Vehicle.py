from src.utils import distance


class Vehicle(object):
    def __init__(self, id):
        self.id = id
        self.rides = []
        self.position= (0,0)
        self.time = 0

    #position deve essere una lista di 2 interi (x,y)
    def move(self, position):
        self.time = distance(position, self.position)
        self.position = position

    def __str__(self):
        return str(self.id)
