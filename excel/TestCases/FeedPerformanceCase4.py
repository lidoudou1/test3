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

    def test_case4(self):
        driver = self.driver
        time.sleep(30)
        # 步骤A
        timeA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        list = ['日本新防卫大纲担忧中国军事动向 华春莹：老调重弹，冷战思维',
                '韬蕴资本：贾跃亭躲在豪宅大门紧闭 拒绝接受任何法律文书',
                '凉凉！谷歌中国版搜索引擎被内部“毙了”',
                '中美经贸微妙时期，中国率先释放一重磅信号',
                '李彦宏：百度将在正确轨道上为人类服务',
                '无人店实地调查！风口未起的2018，门前冷清，多家关店',
                '优酷出台网络电影分账新规，能有效破除唯流量论吗？',
                '推特称检测到自中国和沙特IP地址的可疑活动 外交部回应',
                '解剖京东数科：刘强东持股或超25%，仍是实际控制人',
                '一个月播放32亿+！快手政务号引爆“政能量”传播']
        for i in range(50):
            aa = self.driver.find_elements_by_id('com.baidu.searchbox:id/eq')[0].text
            if aa in list:
                self.driver.find_elements_by_id('com.baidu.searchbox:id/eq')[0].click()
                time.sleep(3)
                for i in range(20):
                    try:
                        driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.4 * self.y, 1000)
                    except:
                        pass
                    time.sleep(1)
                    el = PublicFunctions.isElement(self, 'id', 'com.baidu.searchbox:id/rl_commentitem')
                    if el:
                        for i in range(2):
                            driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.4 * self.y, 1000)
                            time.sleep(1)
                        break
                driver.keyevent(4)
                time.sleep(3)
                del list[0]
            elif len(list) == 0:
                print('测试完成！')
                break
            else:
                print len(list)
                driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.8 * self.y, 1000)
        time.sleep(10)
        # 步骤B
        timeB = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timeData = timeA + ',' + timeB
        # 将A 和 B 的时间用逗号连起来后，存储到相应的case文件中
        timeFile = os.getcwd() + baseConfig['case4']['directory'] + '/' + baseConfig['case4']['time_file']

        PublicFunctions.writeDateToFile(timeData, timeFile)


if __name__ == '__main__':
    unittest.main()
