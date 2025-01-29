class Alphabet:
    __punkt = " ,.-\\/|*`\"\';:1234567890"

    def __init__(self, lang="ua", letters="абвгдежзиіїйклмнопрстуфхцчшщьюя"):
        self.lang = lang
        self.letters = letters

    def print_alphabet(self):
        print("літери: ", self.letters)

    def letters_num(self):
        return len(self.letters)

    def is_valid_string(self, string):
        for i in string:
            if i.lower() not in self.letters and i.lower() not in self.__punkt:
                print(f"є не {self.lang} символи!")
                return False
        print(f"всі символи {self.lang}")
        return True

    @classmethod
    def getPunkt(cls):
        return cls.__punkt


class EngAlphabet(Alphabet):
    __en_letters_num = 26

    def __init__(self, lang="en", letters="abcdefghijklmnopqrstuvwxyz"):
        super().__init__(lang, letters)

    def is_en_letter(self, string):
        return self.is_valid_string(string)

    def letters_num(self):
        return f"кількість літер: {self.__en_letters_num}"

    @staticmethod
    def example():
        return "it is an example text"


class UaAlphabet(Alphabet):
    def __init__(self, lang="ua", letters="абвгдежзиіїйклмнопрстуфхцчшщьюя"):
        super().__init__(lang, letters)

    def is_ua_lang(self, string):
        return self.is_valid_string(string)
