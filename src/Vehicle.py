class Vehicle(object):
    def __init__(self, id):
        self.id = id
        self.rides = []


    def __str__(self):
        return str(self.id)