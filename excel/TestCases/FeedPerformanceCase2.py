# coding=utf-8
__author__ = 'lixuefang'

import time
import unittest
from appium import webdriver
import os
import datetime
import PublicFunctions
from ConfigInfo import baseConfig

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = PublicFunctions.appium_start()

        xy = self.driver.get_window_size()
        self.x = xy['width']
        self.y = xy['height']

    def tearDown(self):
        os.system("ps -ef | grep get_cpu_memory_v3 | grep -v grep | awk '{print $2}' | xargs kill -9")
        self.driver.quit()

    def test_case2(self):
        driver = self.driver
        time.sleep(30)
        # 步骤A
        timeA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for i in range(10):
            driver.find_elements_by_id('com.baidu.searchbox:id/tab_indi_title')[1].click()
            time.sleep(3)
        time.sleep(10)
        #步骤B
        timeB = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timeData = timeA + ',' + timeB
        #将A 和 B 的时间用逗号连起来后，存储到相应的case文件中
        timeFile = os.getcwd() + baseConfig['case2']['directory'] + '/' + baseConfig['case2']['time_file']
        PublicFunctions.writeDateToFile(timeData, timeFile)


if __name__ == '__main__':
    unittest.main()

