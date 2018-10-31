class CarOwner:
    # 차주인에 관한 생성자
    def __init__(self, name):
        self.name = name

    # 메소드 concentrate는 운전에만 집중해야해서 내보냄.
    def concentrate(self):
        print('{} can not do anything else'.format(self.name))


class Car:
    # 자동차에관한 생성자
    def __init__(self, owner_name):
        self.owner = CarOwner(owner_name)

    # 자동차에 관련된 메소드 지정
    def drive(self):
        # 일단 운전을 해야한다면 집중해야하니 다른건 안한다는 지령!!
        self.owner.concentrate()
        # 운전중이라는 상태메세지를 내보낸다.
        print('{} is driving now.'.format(self.owner.name))


# Car를 상속한 자율주행자동차
class SelfDrivingCar(Car):

    # 자율주행은 운전자에게 특별한 집중을 요구하지 않기에
    # drive를 overriding해서 다시 정의한다.
    def drive(self):
        print('Car is driving by itself')

if __name__=='__main__':
    car = Car('Greg')
    car.drive()
    print('')

    s_car = SelfDrivingCar('John')
    s_car.drive()