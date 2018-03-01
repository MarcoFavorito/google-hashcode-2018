class Input(object):
    def __init__(self, rows, columns, vehicles, rides, bonus, steps):
        self.rows       = rows
        self.columns     = columns
        self.vehicles   = vehicles
        self.rides      = rides
        self.bonus      = bonus
        self.steps      = steps


    def __str__(self):
        return """rows     = {self.rows}
columns  = {self.columns}
vehicles = {self.vehicles}
rides    = {self.rides}
bonus    = {self.bonus}
steps    = {self.steps}""".format(**locals())