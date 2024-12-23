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
    def __init__(self, capacity, turns, thickness, radius = 0.06):
        super().__init__(capacity, turns, thickness)
        self.radius = radius

    def bytes_per_20seconds(self):
        return super().bytes_per_20seconds(self.radius)

    def average_rotation_time(self):
        return super().average_rotation_time()


class DVD(OpticalDisk):
    def __init__(self, capacity, turns, thickness, radius = 0.06):
        super().__init__(capacity, turns, thickness)
        self.radius = radius

    def bytes_per_20seconds(self):
        return super().bytes_per_20seconds(self.radius)

    def average_rotation_time(self):
        return super().average_rotation_time()


#пример

if __name__ == "__main__":

    cd = CD(capacity=700 * 1024**2, turns=500, thickness=780)
    dvd = DVD(capacity=4700 * 1024**2, turns=1500, thickness=650)

    print("CD:")
    print(f"Количество байт за 20 секунд: {cd.bytes_per_20seconds():.2f}")
    print(f"Среднее время оборота: {cd.average_rotation_time():.2f} секунд")

    print("\nDVD:")
    print(f"Количество байт за 20 секунд: {dvd.bytes_per_20seconds():.2f}")
    print(f"Среднее время оборота: {dvd.average_rotation_time():.2f} секунд")

    comb_disc = cd + dvd
    print("\nКомбинированный диск:")
    print(f"Ёмкость: {comb_disc.capacity} байт")
    print(f"Обороты: {comb_disc.turns}")
    print(f"Толщина лазера: {comb_disc.thickness} нм")


