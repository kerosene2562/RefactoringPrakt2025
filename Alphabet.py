class Alphabet:
    __punkt = " ,.-\\/|*`\"\';:1234567890"

    def __init__(self, lang = "ua", letters = "абвгдежзиіїйклмнопрстуфхцчшщьюя"):
        self.lang = lang
        self.letters = letters

    def print_alphabet(self):
        print("літери: ",self.letters)

    def letters_num(self):
        print("довжина літер: ", len(self.letters))

    def is_valid_string(self, string):
        print(f"Перевірка чи всі символи відповідають алфавіту ({self.lang}): {string}")
        for i in string:
            if i.lower() not in self.letters and i.lower() not in PUNCTUATION:
                print("Є недопустимі символи!")
                return False
        print("Всі символи валідні")
        return True
            

    @classmethod
    def getPunkt(cls):
        return cls.__punkt

class EngAlphabet(Alphabet):
    __en_letters_num = 26

    def __init__(self, lang = "en", letters = "abcdefghijklmnopqrsntuvwxyz"):
        super().__init__(lang, letters)

    def is_en_letter(self, string):
        return self.is_valid_string(string)

    def letters_num(self):
        return f"Number of letters: {len(self.letters)}"
    
    @staticmethod
    def example():
        return "it is an example text"