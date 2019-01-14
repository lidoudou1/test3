# coding=utf-8
__author__ = 'lixuefang'
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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

    def test_case5(self):
        driver = self.driver
        time.sleep(30)
        # 步骤A
        timeA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.1 * self.y, 1000)
        driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.1 * self.y, 1000)
        title1 = '样子也太可爱了吧！早期出席活动的郭碧婷，看起来好开心！'
        for i in range(10):
            print(i)
            for i in range(50):
                aa = self.driver.find_elements_by_id('com.baidu.searchbox:id/eq')[0].text
                if aa == title1:
                    self.driver.find_elements_by_id('com.baidu.searchbox:id/eq')[0].click()
                    time.sleep(3)
                    for i in range(8):
                        try:
                            driver.swipe(0.8 * self.x, 0.5 * self.y, 0.2 * self.x, 0.5 * self.y, 1000)
                        except:
                            pass
                        time.sleep(1)
                    self.driver.keyevent(4)
                    time.sleep(3)
                    break
                else:
                    driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.8 * self.y, 1000)
        time.sleep(10)
        # 步骤B
        timeB = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timeData = timeA + ',' + timeB
        # 将A 和 B 的时间用逗号连起来后，存储到相应的case文件中
        timeFile = os.getcwd() + baseConfig['case5']['directory'] + '/' + baseConfig['case5']['time_file']
        PublicFunctions.writeDateToFile(timeData, timeFile)


if __name__ == '__main__':
    unittest.main()

