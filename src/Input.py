class Input(object):
    def __init__(self, rows, columns, vehicles, rides, bonus, steps):
        self.rows       =  int(rows)
        self.columns     = int(columns)
        self.vehicles   =  int(vehicles)
        self.rides      =  int(rides)
        self.bonus      =  int(bonus)
        self.steps      =  int(steps)


    def __str__(self):
        return """rows     = {self.rows}
columns  = {self.columns}
vehicles = {self.vehicles}
rides    = {self.rides}
bonus    = {self.bonus}
steps    = {self.steps}""".format(**locals())