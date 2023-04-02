from collections import UserDict

class Garage(UserDict):
    def add_car(self,car):
        self.data[car.mark.value] = car



class Car:
    def __init__(self, mark, model, reg_number, mileage=None):
        self.model = model
        self.mark = mark
        self.reg_number = reg_number
        self.repair = mileage
        self.repairs = []
        if mileage:
            self.repairs.append(mileage)


    def add_mileage(self, mileage):
        max_mileage = max([m.value for m in self.mileages])
        if self.mileages and mileage.value < max_mileage:
            raise ValueError(f"Max mileage {max_mileage}")
        self.mileages.append(mileage)
        


class Core:
    def __init__(self, value):
        self.value = value
    def __str__(self) -> str:
        return self.value

class Mark(Core):
    def __init__(self, value):
        if not  isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value



class Model(Core):
    pass


class Regnumber(Core):
    pass

class Mileage(Core):
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError('must be a integer')
        self.value = value



if __name__ == '__main__':
    mark = Mark("VW")
    model = Model("Passat")
    reg = Regnumber("AO0402AO")
    mil1 = Mileage(200000)
    car1 = Car(mark, model, reg, mil1)
    print(250000 > mil1.value)
    

    print (f'{car1.model}: {car1.mark} - {car1.reg_number}')
    

    car1.add_mileage(Mileage(10000))
    car1.add_mileage(Mileage(50000))