# coding=utf-8
__author__ = 'lixuefang'

import time
import unittest
from appium import webdriver
import os
import datetime
import PublicFunctions
from ConfigInfo import baseConfig
from appium import webdriver
import appium

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = PublicFunctions.appium_start()

        xy = self.driver.get_window_size()
        self.x = xy['width']
        self.y = xy['height']

    def tearDown(self):
        os.system("ps -ef | grep get_cpu_memory_v3 | grep -v grep | awk '{print $2}' | xargs kill -9")
        self.driver.quit()

    def test_case1(self):
        # 步骤A
        timeA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time.sleep(2)
        # 步骤B
        timeB = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timeData = timeA + ',' + timeB
        # 将A 和 B 的时间用逗号连起来后，存储到相应的case文件中
        timeFile = os.getcwd() + baseConfig['case1']['directory'] + '/' + baseConfig['case1']['time_file']
        PublicFunctions.writeDateToFile(timeData, timeFile)


if __name__ == '__main__':
    unittest.main()

