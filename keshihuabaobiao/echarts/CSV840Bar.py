# encoding: utf-8
from echarts import EchartUtils
from echarts.CSVDataManager import CSVDataManager

"""
生成840柱状图报表，用于分析测试数据均值
"""
csvDataManager = CSVDataManager()
csvDataManager.initData("refresh840.csv")
EchartUtils.show840Bar(csvDataManager.cal840BarData(), True)
