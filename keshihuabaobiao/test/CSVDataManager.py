import csv
import numpy as np


class CSVDataManager:
    __mHeader = []
    __mRows = []

    def initData(self, fileDir):
        if not fileDir:
            return

        try:
            with open(fileDir, 'r') as f:
                reader = csv.reader(f)
                self.__mHeader = next(reader)
                for row in reader:
                    self.__mRows.append(row)
                f.close()
        except IOError:
            print('读取文件失败！')

    def getHeader(self):
        return self.__mHeader

    def getRows(self):
        return self.__mRows

    def cal840BarData(self):
        dictData = {}
        if (not self.__mHeader) or (not self.__mRows):
            return dictData
        keys = self.__mHeader
        values = []
        valueArray = np.array(self.__mRows)
        for i in range(0, len(keys)):
            temp = valueArray[:, i]
            values.append(CSVDataManager.calAvg(temp))
        dictData = dict(zip(keys, values))
        return dictData

    @staticmethod
    def calAvg(array):
        sums = 0
        if not len(array):
            return sums
        length = len(array)
        for i in range(0, len(array)):
            # 如果值不存在则忽略
            if array[i] == '-' or array[i] == '':
                length -= 1
            else:
                sums += int(array[i])
        if length == 0:
            return 0
        else:
            return sums / length
