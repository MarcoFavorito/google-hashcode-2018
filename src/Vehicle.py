class Vehicle(object):
    def __init__(self, id):
        self.id = id
        self.rides = []
        self.position = (0,0)

    #position deve essere una lista di 2 interi (x,y)
    def move(self, position):
        self.position = position

    def __str__(self):
        return str(self.id)
