class Output(object):
    def __init__(self, vehicles2rides):
        self.vehicles2rides = vehicles2rides


    def __str__(self):
        return "\n".join("this veihcleis assigned %s ride: %s" % (v, l) for v,l in self.vehicles2rides.items())
