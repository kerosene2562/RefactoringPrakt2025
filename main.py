from Alphabet import *
from Human import *
from Apple import *
from KmrCsv import *

def inputNumber(text, need):
    while True:
        try:
            x = int(input(text))
            if need:
                assert x > 0
            break
        except Exception as ex:
            print("ви ввели не число або довжина не є коректною (довжина повинна бути більше за 0)!")
    return x

while(True):
    print("\n1 - літери"
          "\n2 - покупка дому"
          "\n3 - сад"
          "\n4 - csv"
          "\n0 - вихід")
    choice = inputNumber("оберіть завдання: ", False)
    match choice:
        case 1:
            uk = Alphabet()
            uk.print_alphabet()
            uk.letters_num()
            uk.is_ua_lang("уйр *")
            uk.is_ua_lang("Щ")

            en = EngAlphabet()
            en.print_alphabet()
            print(en.letters_num())
            en.is_en_letter("asdf")
            en.is_en_letter("J")
            en.is_en_letter(EngAlphabet.example())
            print(EngAlphabet.example())
        case 2:
            Human.default_info()
            human = Human("Sasha", "20", 500)
            human.info()
            human.earn_money(2000)
            human.info()

            house = House(100, 2000, 15)
            smallHouse = SmallHouse(10, 100)

            human.buy_house(house)
            human.info()
        case 3:
            apple = Apple()
            print(apple._state)
            apple.grow()
            print(apple._state)
            apple.grow()
            print(apple._state)
            apple.grow()
            print(apple._state)
            apple.grow()

            apple = Apple()
            print(apple._state)
            apple.grow()
            print(apple._state)
            apple.grow()
            print(apple._state)
            apple.grow()
            print(apple._state)
            apple.grow()


            print("\napple tree")
            tree = AppleTree(4)
            gardener = Gardener("Sasha", tree)
            Gardener.apple_base(tree)
            gardener.work()
            Gardener.apple_base(tree)
            gardener.work()
            Gardener.apple_base(tree)
            gardener.work()
        case 4:
            test1 = KmrCsv()
            results1 = test1.readResults()
            test1.fileInfo(results1)

            for index, bal in enumerate(Statistic.avg_stat(results1)):
                print(f"на запитання номер {index} правильних відповідей = {bal:.2f}%")

            dictBals = Statistic.marks_stat(results1)
            for bal, count in dictBals.items():
                print(f"оцінок {bal} балів: {count}")

            for id, balPerMin in Statistic.marks_per_time(results1).items():
                print(f"студент з айді {id} отримав {balPerMin:.2f} білів за хвилину")

            print("топ 5 оцінок з заданими межами")
            for id, bal, balPM in Statistic.best_marks_per_time(results1,0, 0.4):
                print(f"студент з айді {id} та загальним балом {bal} має {balPM} балів за одну хвилину")

            plt = Plots()
            plt.avg_plot(Statistic.avg_stat(results1))

            plt.marks_plot(dictBals)

            plt.best_marks_plot(Statistic.best_marks_per_time(results1,0, 0.4))

            Kmr1 = KmrWork("marks.lab6.csv", 1)
            Kmr2 = KmrWork("marks2.lab11.csv", 2)

            results1 = Kmr1.readResults()
            Kmr1.avg_plot(Statistic.avg_stat(results1))

            results2 = Kmr2.readResults()
            Kmr2.avg_plot(Statistic.avg_stat(results2))

            Kmr1.compare_csv()
            Kmr1.compare_avg_plots([Statistic.avg_stat(results1),Statistic.avg_stat(results2)])
        case 0:
            print("завершення роботи програми")
            break
        case _:
            print("оберіть інший варіант!")