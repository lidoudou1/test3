from test import ChartUtils
from test.CSVDataManager import CSVDataManager

csvDataManager = CSVDataManager()
csvDataManager.initData("refresh840.csv")
ChartUtils.showBarChart(csvDataManager.cal840BarData())
