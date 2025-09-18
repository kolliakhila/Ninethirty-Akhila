class Car:
    car_count=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.car_count+=1
    @classmethod
    def get_car_count(cls):
        return cls.car_count
car1=Car("Suzuki","Swift")
car2=Car("Honda","Accord")
car3=Car("Tata","Nexon")
print("Number of cars:",Car.get_car_count())
