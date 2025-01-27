import csv
import re
import matplotlib.pyplot as plt
import os
import numpy as np

class KmrCsv:
    def __init__(self, ref = 'marks2.lab11.csv', num = 1):
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
        print("номер КМР:",self.__num, "кількість студентів, які проходили КМР:", len(data))

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
        resultDict = {}
        bals = [data[i][4] for i in range(len(data))]
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
                resultDict[row[0]] = float(row[4].replace(',','.')) / (minutes * 60 + seconds) * 60
        return resultDict

    @staticmethod
    def best_marks_per_time(data, bottom_margin, top_margin):
        resultArr = []
        bestFive = []

        avgBals = [float(data[i][4].replace(',','.')) for i in range(len(data))]
        for index, (student, markPerTime) in enumerate(Statistic.marks_per_time(data).items()):
            resultArr.append([student, avgBals[index], markPerTime])

        resultArr = sorted(resultArr, key =  lambda x: x[2], reverse = True)

        for index,(id, bal, balPM) in enumerate(resultArr):
            if balPM > bottom_margin and balPM < top_margin:
                bestFive.append(resultArr[index])
            if len(bestFive) == 5:
                break

        return bestFive

class Plots:
    def set_cat(self, ref):
        self.__ref = ref

    def avg_plot(self, bals):
        ansNumber = [i + 1 for i in range(len(bals))]
        plt.bar(ansNumber, bals)
        plt.grid(axis = 'y')
        plt.title("відсоток правильних відповідей на кожне питання")
        plt.xlabel("номер запитання")
        plt.ylabel("відсоток правильних відповідей")
        plt.xticks(ansNumber)
        plt.savefig('avg_plot.png')
        plt.show()

    def marks_plot(self, dict):
        plt.figure(figsize=(15,7))
        plt.grid(axis = 'y')
        plt.bar(dict.keys(), dict.values())
        plt.title("кількість набраних оцінок")
        plt.xlabel("оцінка")
        plt.ylabel("кількість студентів отримавших оцінку")
        plt.savefig('marks_plot.png')
        plt.show()

    def best_marks_plot(self, arr):
        students = [arr[i][0] for i in range(len(arr))]
        balPM = [arr[i][2] for i in range(len(arr))]
        plt.figure(figsize=(20,7))
        plt.grid(axis = 'y')
        plt.bar(students, balPM)
        plt.xlabel("айді студентів")
        plt.ylabel("оцінка за хвилину")
        plt.savefig('best_marks_plot.png')
        plt.show()

class KmrWork(KmrCsv, Statistic, Plots):
    kmrs = {}
    cat = 'results'
    def __init__(self, ref, num):
        super().__init__(ref, num)
        KmrWork.kmrs[num] = ref

    def compare_csv(self):
        compareArr = []
        for num, kmr in self.kmrs.items():
            test = []
            tmp = KmrCsv(kmr, num)
            data = tmp.readResults()
            test.append(len(data))

            dictStat = Statistic.marks_stat(data)
            zagBal = 0
            for bal, kilk in dictStat.items():
                bal = float(bal.replace(',','.'))
                zagBal += (bal * kilk)
            test.append(zagBal / len(data))

            zagTime = 0
            for row in data:
                time = re.match(r"(\d+)\s*хв(?:\s*(\d+)\s*сек)?", row[3])
                if time:
                    minutes = int(time[1])
                    seconds = int(time[2]) if time[2] else 0
                    zagTime +=  minutes * 60 + seconds
            test.append(zagTime / 60 / len(data))
            compareArr.append(test)
        with open(f"{self.cat}/scv_compare.txt", 'w', encoding="utf-8") as file:
            if not os.path.isdir(self.cat):
                os.mkdir(self.cat)
            for index, test in enumerate(compareArr):
                file.write(f"кількість проходжень тесту номер {index+1}: {test[0]}, середній бал: {test[1]}, середній час проходження тесту: {test[2]}\n")

    def compare_avg_plots(self, bals):
        width = 0.3
        x = np.arange(1,len(bals[0])+1,1)
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
        plt.savefig('results/cmpGist.png')
        plt.show()

