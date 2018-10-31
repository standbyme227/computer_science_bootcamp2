# Animal은 모든걸 엮는 base class인데
# 사실 상속된 클래스들이 보여주든 다들 특정한 meat이나 grass를 먹지
# something을 먹는 존재는 이세상에 존재하지 않는걸로보인다.
# 이럴 때 추상화클래스를 이용한다.

# class Animal:
#     def eat(self):
#         print('eat something')

from abc import *

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def eat(self):
        pass

class Lion(Animal):
    def eat(self):
        print('eat meat')

class Deer(Animal):
    def eat(self):
        print('eat grass')

class Human(Animal):
    def eat(self):
        print('eat meat and grass')

if __name__=='__main__':
    animals = []

    animals.append(Lion())
    animals.append(Deer())
    animals.append(Human())

    animals.append(Animal())

    for animal in animals:
        animal.eat()


