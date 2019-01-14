# encoding: utf-8
import csv
import numpy as np

class CSVDataManager:
    """
    CSV管理器，每个csv文件一一对应一个管理器
    """

    __mHeader = []  # 标题栏，例：['A','B',...]
    __mRows = []  # 数据行，例：[[1,2,3],[4,5,6],...]

    #传入csv文件路径，读取csv文件数据，获得标题栏和数据行
    def initData(self, fileDir):
        """
        初始化CSV数据管理器，需传入csv文件路径
        会读取csv文件数据，获得标题栏和数据行
        """
        if not fileDir:
            return

        try:
            with open(fileDir, 'r') as f:
                reader = csv.reader(f)
                print reader
                # 读取标题栏
                self.__mHeader = next(reader)
                # 读取数据行
                for row in reader:
                    self.__mRows.append(row)
                f.close()
        except IOError:
            print('读取文件失败！')

    #获取标题栏数据
    def getHeader(self):
        return self.__mHeader
    #获取数据行数据
    def getRows(self):
        return self.__mRows

    #计算柱状图数据
    def cal840BarData(self):
        """
        计算840柱状图数据，key-value形式，key为标题
        value为该标题对应列的平均值
        例：{'A':2,'B':3,...}
        """
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

    #计算数组平均值
    @staticmethod
    def calAvg(array):
        """
        计算一个数组的平均值，如果值不存在则直接抛弃
        """
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

    #计算折线图数据
    def cal840LineData(self):
        """
        计算840折线图数据，每个阶段耗时为一个数组存储
        例：[[1,2],[3,4],...]
        """
        result = []
        if (not self.__mHeader) or (not self.__mRows):
            return result
        keys = self.__mHeader
        valueArray = np.array(self.__mRows)
        for i in range(0, len(keys)):
            temp = valueArray[:, i]
            value = CSVDataManager.formatArray(temp)
            result.append(value)
            print result
        return result

    #格式化数组,把'-'替换为0
    @staticmethod
    def formatArray(array):
        """
        格式化数组，会把'-'替换为0
        """
        result = []
        if not len(array):
            return result
        for i in range(0, len(array)):
            if array[i] == '-' or array[i] == '':
                result.append(0)
            else:
                result.append(array[i])
        return result
























