# encoding: utf-8
from echarts import EchartUtils
from echarts.CSVDataManager import CSVDataManager

"""
生成840饼图报表，用于分析测试数据各指标占比
"""
csvDataManager = CSVDataManager()
csvDataManager.initData("refresh840.csv")
EchartUtils.show840Pie(csvDataManager.cal840BarData(), True)
