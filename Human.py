class Human:
    default_name = 'Sasha'
    default_age = '20'

    def __init__(self, name, age, __money = 0, __house = None):
        self.name = name
        self.age = age
        self.__money = __money
        self.__house = __house

    def info(self):
        print(f"name: {self.name}, age: {self.age}, money: {self.__money}, house: {self.__house} m^2")
        
    @staticmethod
    def default_info():
        print(f"name: {Human.default_name}, age: {Human.default_age}")

    def __make_deal(self, house):
        self.__money = self.__money - house.final_price()
        self.__house = house._area

    def earn_money(self, cash):
        print("you earned", cash)
        self.__money = self.__money + cash

    def buy_house(self, house):
        if self.__money < house.final_price():
            print("no money")
            return False
        else:
            print("sueccess purches!")
            self.__make_deal(house)
            return True
        
class House:
    def __init__(self, _area = 50, _price = 1000, discount = 10) :
        self._area = _area
        self._price = _price
        self.discount = discount

    def final_price(cls):
        return cls._price - (cls._price / 100 * cls.discount)

class SmallHouse(House):
    def __init__(self, _area = 50, _price = 1000):
        super().__init__(_area,_price)