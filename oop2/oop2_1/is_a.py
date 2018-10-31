class Computer:
    """

        attributes:
        CPU :
        RAM :
    """
    # 생성자
    def __init__(self, cpu, ram):
        self.CPU = cpu
        self.RAM = ram

    # 메소드
    def browse(self):
        print('browse')

    # 메소드
    def work(self):
        print('work')

# Computer를 상속
class Laptop(Computer):
    # battery 멤버 추가
    def __init__(self, cpu, ram, battery):
        # Computer 클래스의 생성자를 호출
        super().__init__(cpu, ram)
        self.battery = battery

    # 메서드 추가
    def move(self, to):
        print('move to {}'.format(to))

if __name__== '__main__':
    lap = Laptop('intel', 16, 'powerful')
    lap.browse()
    lap.work()
    lap.move('office')