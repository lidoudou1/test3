# encoding: utf-8
from echarts import EchartUtils
from echarts.CSVDataManager import CSVDataManager

"""
生成840折线图报表，用于分析测试数据各指标趋势
"""
csvDataManager = CSVDataManager()
#读取数据
csvDataManager.initData("refresh840.csv")
#生成报表
EchartUtils.show840Line(csvDataManager.getHeader(), csvDataManager.cal840LineData(), True)
