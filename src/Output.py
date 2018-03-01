class Output(object):
    def __init__(self, vehicles2rides):
        self.vehicles2rides = vehicles2rides


    def __str__(self):
        return "\n".join(str(v) + " " + " ".join(map(str,l)) for v,l in self.vehicles2rides.items())