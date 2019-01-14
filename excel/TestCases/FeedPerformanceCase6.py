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

    def test_case6(self):
        driver = self.driver
        time.sleep(30)
        # 步骤A
        timeA = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 把所有title都写进来
        list = ['样子也太可爱了吧！早期出席活动的郭碧婷，看起来好开心！',
                '娱乐圈让人羡慕的6对夫妻，黄晓明Angelababy上榜，你最看好哪对',
                '美丽少女张雪迎，穿什么衣服都好看，美貌身材兼备的小鲜肉',
                '佟丽娅厉害了，在耳朵上戴“戒指”不够还单扎麻花辫，美成了初恋',
                'Angelababy早期出席活动，一袭优雅高贵的礼服，犹如仙子般惊艳',
                '鹿晗真会打扮，卫衣叠加风衣帅气十足，搭配中分发型意外的时髦',
                '刘亦菲在裙上安扣子不够，还配双“雨滴鞋”，和黄晓明同框太抢镜',
                '网友偶遇张雪迎，街拍素颜的张雪迎也是仙气满满！',
                '这还是我认识的那个陈妍希吗？早期出席活动的她，这一波美我认了',
                '不愧是“亚洲第一美”！早期走活动的克拉拉，穿吊带裙没一丝赘肉']
        driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.1 * self.y, 1000)
        driver.swipe(0.5 * self.x, 0.9 * self.y, 0.5 * self.x, 0.1 * self.y, 1000)
        for i in range(50):
            aa = self.driver.find_elements_by_id('com.baidu.searchbox:id/eq')[0].text
            if aa in list:
                self.driver.find_elements_by_id('com.baidu.searchbox:id/eq')[0].click()
                time.sleep(3)
                for i in range(10):
                    try:
                        driver.swipe(0.8 * self.x, 0.5 * self.y, 0.2 * self.x, 0.5 * self.y, 1000)
                    except:
                        pass
                    time.sleep(1)
                self.driver.keyevent(4)
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
        timeFile = os.getcwd() + baseConfig['case6']['directory'] + '/' + baseConfig['case6']['time_file']
        PublicFunctions.writeDateToFile(timeData, timeFile)


if __name__ == '__main__':
    unittest.main()

