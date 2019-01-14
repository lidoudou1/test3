# encoding: utf-8
from echarts import EchartUtils
from echarts.CSVDataManager import CSVDataManager

"""
生成840报表，包含支持的所有图
"""
csvDataManager = CSVDataManager()
csvDataManager.initData("refresh840.csv")
#把所有可视图都放到一张页面中
EchartUtils.show840All(EchartUtils.show840Line(csvDataManager.getHeader(), csvDataManager.cal840LineData(), False),
                       EchartUtils.show840Bar(csvDataManager.cal840BarData(), False),
                       EchartUtils.show840Pie(csvDataManager.cal840BarData(), False))
