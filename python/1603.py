class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.parking[carType - 1] -= 1
        return self.parking[carType - 1] >= 0
