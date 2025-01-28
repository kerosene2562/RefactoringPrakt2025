import csv
import re
import matplotlib.pyplot as plt
import os
import numpy as np

# Константи
DEFAULT_CSV_FILE = 'marks2.lab11.csv'
RESULTS_DIR = 'results'
CSV_COMPARE_FILE = 'scv_compare.txt'
AVG_PLOT_FILE = 'avg_plot.png'
MARKS_PLOT_FILE = 'marks_plot.png'
BEST_MARKS_PLOT_FILE = 'best_marks_plot.png'
CMP_GIST_FILE = 'results/cmpGist.png'


class KmrCsv:
    def __init__(self, ref=DEFAULT_CSV_FILE, num=1):
        self.__ref = ref
        self.__num = num

    @property
    def ref(self):
        return self.__ref

    @ref.setter
    def ref(self, ref):
        self.__ref = ref

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    def readResults(self):
        with open(self.__ref, 'rt', encoding='utf-8') as marks_file:
            csvrecord = csv.reader(marks_file)
            data = [row for row in csvrecord]
            return data

    def fileInfo(self, data):
        print(f"номер КМР: {self.__num}, кількість студентів, які проходили КМР: {len(data)}")


class Statistic:
    @staticmethod
    def avg_stat(data):
        resultArr = []
        correctCounter = [0 for _ in range(len(data[0][5:]))]
        for strIndex, string in enumerate(data):
            for balIndex, bal in enumerate(string[5:]):
                if bal != '-' and float(bal.replace(',', '.')) != 0.00:
                    correctCounter[balIndex] += 1
        for ans in correctCounter:
            resultArr.append((ans * 100) / len(data))
        return resultArr

    @staticmethod
    def marks_stat(data):
        return Statistic._calculate_stat(data, index=4)

    @staticmethod
    def _calculate_stat(data, index):
        resultDict = {}
        bals = [data[i][index] for i in range(len(data))]
        for bal in bals:
            if bal in resultDict:
                resultDict[bal] += 1
            else:
                resultDict[bal] = 1
        return resultDict

    @staticmethod
    def marks_per_time(data):
        resultDict = {}
        for row in data:
            time = re.match(r"(\d+)\s*хв(?:\s*(\d+)\s*сек)?", row[3])
            if time:
                minutes = int(time[1])
                seconds = int(time[2]) if time[2] else 0
                resultDict[row[0]] = float(row[4].replace(',', '.')) / (minutes * 60 + seconds) * 60
        return resultDict

    @staticmethod
    def best_marks_per_time(data, bottom_margin, top_margin):
        resultArr = []
        bestFive = []
        searchCol = 4
        max_students = 5

        avgBals = [float(data[i][searchCol].replace(',', '.')) for i in range(len(data))]
        for index, (student, markPerTime) in enumerate(Statistic.marks_per_time(data).items()):
            resultArr.append([student, avgBals[index], markPerTime])

        resultArr = sorted(resultArr, key=lambda x: x[2], reverse=True)

        for index, (id, bal, balPM) in enumerate(resultArr):
            if balPM > bottom_margin and balPM < top_margin:
                bestFive.append(resultArr[index])
            if len(bestFive) == max_students:
                break

        return bestFive


class Plots:
    def set_cat(self, ref):
        self.__ref = ref

    def avg_plot(self, bals):
        ansNumber = [i + 1 for i in range(len(bals))]
        plt.bar(ansNumber, bals)
        plt.grid(axis='y')
        plt.title("відсоток правильних відповідей на кожне питання")
        plt.xlabel("номер запитання")
        plt.ylabel("відсоток правильних відповідей")
        plt.xticks(ansNumber)
        plt.savefig(AVG_PLOT_FILE)
        plt.show()

    def marks_plot(self, dict):
        plt.figure(figsize=(15, 7))
        plt.grid(axis='y')
        plt.bar(dict.keys(), dict.values())
        plt.title("кількість набраних оцінок")
        plt.xlabel("оцінка")
        plt.ylabel("кількість студентів отримавших оцінку")
        plt.savefig(MARKS_PLOT_FILE)
        plt.show()

    def best_marks_plot(self, arr):
        students = [arr[i][0] for i in range(len(arr))]
        balPM = [arr[i][2] for i in range(len(arr))]
        plt.figure(figsize=(20, 7))
        plt.grid(axis='y')
        plt.bar(students, balPM)
        plt.xlabel("айді студентів")
        plt.ylabel("оцінка за хвилину")
        plt.savefig(BEST_MARKS_PLOT_FILE)
        plt.show()


class KmrWork(KmrCsv, Statistic, Plots):
    kmrs = {}
    cat = RESULTS_DIR

    def __init__(self, ref, num):
        super().__init__(ref, num)
        KmrWork.kmrs[num] = ref

    def compare_csv(self):
        compareArr = []

        for num, kmr in self.kmrs.items():
            test = self.process_single_test(kmr, num)
            compareArr.append(test)

        self.save_results(compareArr)

    def process_single_test(self, kmr, num):
        tmp = KmrCsv(kmr, num)
        data = tmp.readResults()

        test = []
        test.append(len(data))
        test.append(self.calculate_average_score(data))
        test.append(self.calculate_average_time(data))

        return test

    def calculate_average_score(self, data):
        dictStat = Statistic.marks_stat(data)
        total_score = 0

        for bal, count in dictStat.items():
            bal = float(bal.replace(',', '.'))
            total_score += bal * count

        return total_score / len(data)

    def calculate_average_time(self, data):
        total_time = 0

        for row in data:
            time_match = re.match(r"(\d+)\s*хв(?:\s*(\d+)\s*сек)?", row[3])
            if time_match:
                minutes = int(time_match[1])
                seconds = int(time_match[2]) if time_match[2] else 0
                total_time += minutes * 60 + seconds

        return total_time / 60 / len(data)

    def save_results(self, compareArr):
        if not os.path.isdir(self.cat):
            os.mkdir(self.cat)

        with open(os.path.join(self.cat, CSV_COMPARE_FILE), 'w', encoding="utf-8") as file:
            for index, test in enumerate(compareArr):
                file.write(
                    f"Кількість проходжень тесту номер {index + 1}: {test[0]}, середній бал: {test[1]}, середній час проходження тесту: {test[2]}\n")

    def compare_avg_plots(self, bals):
        width = 0.3
        x = np.arange(1, len(bals[0]) + 1, 1)
        fig, ax = plt.subplots()
        ax.bar(x - width / 2, bals[0], width, label=1)
        ax.bar(x + width / 2, bals[1], width, label=2)
        ax.set_xticks(x)
        ax.grid(axis='y')
        ax.set_xlabel("номер запитання")
        ax.set_ylabel("відсотки")
        ax.set_title("порівняння гістограм з відсотками правильних відповідей")
        ax.legend()
        if not os.path.isdir(self.cat):
            os.mkdir(self.cat)
        plt.savefig(CMP_GIST_FILE)
        plt.show()
