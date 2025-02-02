UA_LETTERS = "абвгдежзиіїйклмнопрстуфхцчшщьюя"
EN_LETTERS = "abcdefghijklmnopqrstuvwxyz"
PUNCTUATION = " ,.-\\/|*`\"';:1234567890"

class Alphabet:
    def __init__(self, lang="ua", letters=UA_LETTERS):
        self.lang = lang
        self.letters = letters

    def print_alphabet(self):
        print("літери:", self.letters)

    def letters_num(self):
        print("довжина літер:", len(self.letters))

    def is_valid_string(self, string):
        print(f"Перевірка чи всі символи відповідають алфавіту ({self.lang}): {string}")
        for i in string:
            if i.lower() not in self.letters and i.lower() not in PUNCTUATION:
                print("Є недопустимі символи!")
                return False
        print("Всі символи валідні")
        return True

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__(lang="en", letters=EN_LETTERS)

    def is_en_letter(self, string):
        return self.is_valid_string(string)

    def letters_num(self):
        return f"Кількість літер: {len(self.letters)}"
    
    @staticmethod
    def example():
        return "it is an example text"