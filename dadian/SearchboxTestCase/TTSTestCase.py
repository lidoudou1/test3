#coding=utf-8
__author__ = 'lixuefang'

from appium import webdriver
import unittest
import time
from utils import PublicFunction
from utils import CommonAction
import os
# import HTMLTestRunner
# import os


class TTSTestCase(unittest.TestCase):

    #执行在每个case之前，用于启动手百
    def setUp(self):
        self.driver = PublicFunction.appium_start()

    #执行每个case之后运行，用于退出
    def tearDown(self):
        self.driver.quit()

    def test_TTSBroadcastDuration_724(self):
        path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        pathTopic = path + '/' + 'TopicDuration' + '/' + 'tts_duration'
        time.sleep(3)
        # 判断耳机是否存在，如果存在说明当前是处于看听模式
        element_exist = CommonAction.isElement(self, 'id', 'com.baidu.searchbox:id/tab_right_tts')
        if element_exist:
            # 判断播报按钮是否存在，如果存在说明已经打开看听模式
            element_exist = CommonAction.isElement(self, 'id', 'com.baidu.searchbox:id/feed_id_radio_icon_tag')
            if element_exist:
                broadcastIcon = self.driver.find_elements_by_id("com.baidu.searchbox:id/feed_id_radio_icon_tag")  # 播放图标
                broadcastIcon[1].click()
                starttime4 = time.time()
            else:
                headsetIcon = self.driver.find_element_by_id("com.baidu.searchbox:id/tab_right_tts")  # 小耳机图标
                headsetIcon.click()
                broadcastIcon = self.driver.find_elements_by_id("com.baidu.searchbox:id/feed_id_radio_icon_tag")
                broadcastIcon[2].click()
                starttime4 = time.time()

            '''在迷你bar按下一条按钮'''
            time.sleep(5)   #实际测试时改成10或15
            miniPauseIcon = self.driver.find_element_by_id("com.baidu.searchbox:id/radio_mini_play_pause")
            radio_mini_play_next = self.driver.find_elements_by_id("com.baidu.searchbox:id/radio_mini_play_next")[0]    #mini bar 下一条按键
            radio_mini_play_next.click()
            endtime4 = time.time()
            duration4 = endtime4 - starttime4
            PublicFunction.writeDateToFile(724, 4, pathTopic, duration4)
            print("\n" + "在迷你bar按下一条按钮")
            print(duration4)

            '''在迷你bar点击关闭按钮'''
            starttime3 = time.time()
            time.sleep(5)  # 实际测试时改成10或15
            miniPauseIcon.click()  #从minibar关闭播放
            endtime3 = time.time()
            duration3 = endtime3 - starttime3
            PublicFunction.writeDateToFile(724, 3, pathTopic, duration3)
            print("\n" + "在迷你bar点击关闭按钮")
            print(duration3)

            '''进入全屏态后，点击开始按钮'''
            fullIcon = self.driver.find_element_by_id("com.baidu.searchbox:id/radio_mini_tts_album_cover")
            fullIcon.click()  #进入全屏态播放器
            time.sleep(3)
            fullMusicPause = self.driver.find_element_by_id("com.baidu.searchbox:id/music_play_pause")
            fullMusicPause.click()  #开启全屏态播放
            starttime2 = time.time()
            time.sleep(5)#实际测试时改成10或15


            '''在全屏态页面，点击上一首按钮'''
            music_previous = self.driver.find_element_by_id("com.baidu.searchbox:id/music_previous")
            music_previous.click()
            starttime1 = endtime2 = time.time()
            duration2 = endtime2 - starttime2
            PublicFunction.writeDateToFile(724, 2, pathTopic, duration2)
            print("\n" + "进入全屏态后，开始播放后，点击上一首按钮")
            print(duration2)

            '''返回首页，关闭看听模式'''
            time.sleep(5)
            self.driver.keyevent(4)
            headsetIcon.click()
            endtime1 = time.time()
            duration1 = endtime1 - starttime1
            PublicFunction.writeDateToFile(724, 1, pathTopic, duration1)
            print("\n" + "返回首页，关闭看听模式")
            print(duration1)
            time.sleep(3)
        else:
            print("当前处于非看听模式")



if __name__ == "__main__":
    unittest.main()

    # for suiteName in [SearchUBCTest, ]:
    #     print(suiteName)
    #     suite = unittest.TestLoader().loadTestsFromTestCase(suiteName)
    #     unittest.TextTestRunner(verbosity=2).run(suite)



    '''#生成html报告
    fp = open('res.html', 'wb')
    suite = unittest.TestSuite()
    suite.addTest(SearchUBCTest('test_TTSBroadcastDuration_724'))
    runnner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='all_tests', description='所有测试情况')
    runnner.run(suite)
    # unittest.main()
    '''