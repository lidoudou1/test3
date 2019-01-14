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

    def test_case3(self):
        driver = self.driver
        time.sleep(3)
        # 步骤A
        timeA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for i in range(10):
            print(i)
            driver.find_elements_by_id('com.baidu.searchbox:id/eq')[0].click()
            time.sleep(3)
            for i in range(20):
                try:
                    driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.4 * self.y, 1000)
                except:
                    pass
                time.sleep(1)
                el = PublicFunctions.isElement(self,'id','com.baidu.searchbox:id/rl_commentitem')
                if el:
                    for i in range(2):
                        driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.4 * self.y, 1000)
                        time.sleep(1)
                    break
            driver.keyevent(4)
            time.sleep(3)
        time.sleep(10)
        #步骤B
        timeB = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timeData = timeA + ',' + timeB
        # 将A 和 B 的时间用逗号连起来后，存储到相应的case文件中
        timeFile = os.getcwd() + baseConfig['case3']['directory'] + '/' + baseConfig['case3']['time_file']
        PublicFunctions.writeDateToFile(timeData, timeFile)


if __name__ == '__main__':
    unittest.main()

