import math

class OpticalDisk:
    def __init__(self, capacity, turns, thickness):
        self.capacity = capacity
        self.turns = turns
        self.thickness = thickness


    def bytes_per_20seconds(self, radius):
        circle_area = 2 * math.pi * radius
        rev_per_second = self.turns/60
        total_rev = rev_per_second * 20
        total_dist = total_rev * circle_area
        return total_dist/self.thickness
    

    def average_rotation_time(self):
        return 60/self.turns
    

    def __add__(self, other):
        if isinstance(other, OpticalDisk):
            comb_capacity = self.capacity + other.capacity
            comb_turns = (self.turns+other.turns) // 2
            comb_thickness = min(self.thickness, other.thickness)
            return OpticalDisk(comb_capacity, comb_turns, comb_thickness)
        raise TypeError("Невозможно сложить операнды".format(type(other).__name__))

    

class CD(OpticalDisk):
    def __int__(self, capacity, turns, thickness, radius = 0.06):
        super().__init__(capacity, turns, thickness)
        self.radius = radius

    def bytes_per_20seconds(self, radius):
        return super().bytes_per_20seconds(radius)

    def average_rotation_time(self):
        return super().average_rotation_time()


class DVD(OpticalDisk):
    def __int__(self, capacity, turns, thickness, radius = 0.06):
        super().__init__(capacity, turns, thickness)
        self.radius = radius

    def bytes_per_20seconds(self, radius):
        return super().bytes_per_20seconds(radius)

    def average_rotation_time(self):
        return super().average_rotation_time()




