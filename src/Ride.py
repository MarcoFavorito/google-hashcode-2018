class Ride(object):
    def __init__(self, id,from_cell, to_cell, earliest_start, latest_finish):
        self.id = id
        self.from_cell      = from_cell
        self.to_cell            = to_cell
        self.earliest_start = earliest_start
        self.latest_finish  = latest_finish

    def __repr__(self):
        return " ".join(map(str,[self.from_cell , self.to_cell , self.earliest_start ,self.latest_finish]))

    def __str__(self):
        return """from_cell      = {self.from_cell}
to_cell        = {self.to_cell}
earliest_start = {self.earliest_start}
latest_finish  = {self.latest_finish}""".format(**locals())
