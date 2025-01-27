class Alphabet:
    __punkt = " ,.-\\/|*`\"\';:1234567890"

    def __init__(self, lang = "ua", letters = "абвгдежзиіїйклмнопрстуфхцчшщьюя"):
        self.lang = lang
        self.letters = letters

    def print_alphabet(self):
        print("літери: ",self.letters)

    def letters_num(self):
        print("довжина літер: ", len(self.letters))

    def is_ua_lang(self, string):
        print(f"перевірка чи всі символи українські в стрічці: {string}")
        for i in string:
            if i.lower() not in self.letters and i.lower() not in self.__punkt:
                print("є не українські символи!")
                return False
        print("всі символи українські")
        return True
            

    @classmethod
    def getPunkt(cls):
        return cls.__punkt

class EngAlphabet(Alphabet):
    __en_letters_num = 26

    def __init__(self, lang = "en", letters = "abcdefghijklmnopqrsntuvwxyz"):
        super().__init__(lang, letters)

    def is_en_letter(self, string):
        print(f"перевірка чи всі символи англійські в стрічці: {string}")
        for i in string:
            if i.lower() not in self.letters and i.lower() not in super().getPunkt():
                print("є не англійські символи!")
                return False
        print("всі символи англійські")
        return True

    def letters_num(self):
        return f"кількість літер: {self.__en_letters_num}"
    
    @staticmethod
    def example():
        return "it is an example text"