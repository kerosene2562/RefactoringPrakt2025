class Apple:
    states = {
        1: "Відсутнє",
        2: "Цвітіння",
        3: "Зелене",
        4: "Червоне"
    }
    count = 0

    def __init__(self):
        self._index = Apple.count
        self._state = self.states[1]
        Apple.count += 1

    def grow(self):
        if not self.is_ripe():
            self.update_state()
        else:
            print(f"Яблуко {self._index} дозріло!")

    def is_ripe(self):
        return self._state == self.states[4]

    def update_state(self):
        for index, value in self.states.items():
            if value == self._state and self._state != self.states[4]:
                self._state = self.states[index + 1]
                break


class AppleTree:
    def __init__(self, numberOfApples):
        self.apples = [Apple() for _ in range(numberOfApples)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
        if not self.apples:
            print("яблука відсутні")
        else:
            print("врожай зібрано!")
            self.apples.clear()


class Gardener:
    def __init__(self, name, _tree):
        self.name = name
        self._tree = _tree

    def work(self):
        print(f"садівник {self.name} працює")
        self._tree.grow_all()
        self.harvest()

    def harvest(self):
        if self._tree.all_are_ripe():
            self._tree.give_away_all()
        else:
            print("урожай ще не дозрів")

    @staticmethod
    def apple_base(tree):
        for apple in tree.apples:
            print(f"яблуко {apple._index} {apple._state}")