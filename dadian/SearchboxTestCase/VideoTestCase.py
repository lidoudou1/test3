#coding=utf-8
import shutil

__author__ = 'lixuefang'

from appium import webdriver
import unittest
import time
from utils import PublicFunction
import os

class VideoTestCase(unittest.TestCase):

    #执行在每个case之前，用于启动手百
    def setUp(self):
        self.driver = PublicFunction.appium_start()

    #执行每个case之后运行，用于退出
    def tearDown(self):
        self.driver.quit()

    # 是否为4G网络，如果为4G网络弹出流量提示浮层
    def is_4G(self):
        try:
            continue_play = 0
            self.driver.find_element_by_id("com.baidu.searchbox:id/bt_continue_play")  # 流量提示浮层的继续播放按钮
        except:
            continue_play = 1
        self.assertNotEqual(continue_play, 0, msg="4G网络弹出流量提示浮层")

    # 是否视频播放失败，播放失败弹出加载失败重试弹层
    def is_error(self):
        try:
            retry = 0
            self.driver.find_element_by_id("com.baidu.searchbox:id/bt_retry")  # 无网络或加载失败浮层点击重试按钮
        except:
            retry = 1
        self.assertNotEqual(retry, 0, msg="视频加载成功，开始播放")
        # 推送弹窗是否展现，如果展现将其关闭

    def dialog_idshow(self):
        try:
            self.driver.find_element_by_id("com.baidu.searchbox:id/negative_button").click()  # 推送弹窗
            time.sleep(3)
        except:
            print("推送弹窗元素不存在")

    # 点击好看视频、切换好看列表视频、进入视频落地页、进入百家号作者页返回、点击推荐视频
    def test_avideo_485(self):
        path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        pathTopic = path + '/' + 'TopicDuration' + '/' + 'video_duration'
        time.sleep(10)
        self.dialog_idshow()
        try:
            videobar = self.driver.find_elements_by_id("com.baidu.searchbox:id/home_tab_item_textview")[
                1]  # 点击好看视频底bar
            if videobar.is_displayed():
                videobar.click()
                time.sleep(10)
                channelvideo1 = self.driver.find_elements_by_id("com.baidu.searchbox:id/tab_video_img")[
                    0]  # 点击好看视频列表视频
                if channelvideo1.is_displayed():
                    channelvideo1.click()
                    starttime5 = time.time()
                    time.sleep(20)
                    self.driver.find_elements_by_id("com.baidu.searchbox:id/tab_video_img")[1].click()  # 切换列表视频
                    endtime5 = time.time()
                    duration5 = endtime5 - starttime5
                    PublicFunction.writeDateToFile(485, 5, pathTopic, duration5)

                    starttime4 = endtime5
                    time.sleep(20)
                    self.driver.find_elements_by_id("com.baidu.searchbox:id/tab_indi_title")[1].click()  # 切换列表tab
                    endtime4 = time.time()
                    duration4 = endtime4 - starttime4
                    PublicFunction.writeDateToFile(485, 4, pathTopic, duration4)

                    time.sleep(5)
                    self.driver.find_elements_by_id("com.baidu.searchbox:id/tab_video_author_text")[
                        0].click()  # 进入视频落地页
                    starttime3 = time.time()
                    time.sleep(15)
                    author = self.driver.find_element_by_id(
                        "com.baidu.searchbox:id/video_detail_author")  # 跳转到百家号作者页
                    endtime3 = time.time()
                    if author.is_displayed():
                        author.click()
                        duration3 = endtime3 - starttime3
                        PublicFunction.writeDateToFile(485, 3, pathTopic, duration3)
                        # self.assertTrue(author.is_displayed(), "落地页推荐视频加载成功")

                        time.sleep(5)
                        self.driver.find_element_by_id("com.baidu.searchbox:id/redtip_icon").click()  # 返回到视频落地页
                        starttime2 = time.time()
                        time.sleep(10)
                        recommend = self.driver.find_elements_by_id("com.baidu.searchbox:id/feed_content")[
                            1]  # 点击视频落地页推荐视频
                        if recommend.is_displayed():
                            recommend.click()
                            endtime2 = time.time()
                            duration2 = endtime2 - starttime2
                            PublicFunction.writeDateToFile(485, 2, pathTopic, duration2)

                            starttime1 = endtime2
                            time.sleep(10)
                            self.driver.find_element_by_id("com.baidu.searchbox:id/redtip_icon").click()  # 点击落地页返回键
                            endtime1 = time.time()
                            duration1 = endtime1 - starttime1
                            PublicFunction.writeDateToFile(485, 1, pathTopic, duration1)

                        else:
                            self.driver.find_element_by_id("com.baidu.searchbox:id/redtip_icon").click()  # 点击落地页返回键
                            print("没有推荐视频")
                    else:
                        self.driver.find_element_by_id("com.baidu.searchbox:id/redtip_icon").click()  # 点击落地页返回键
                        print("推荐视频加载失败或没有百家号作者")
                else:
                    print("列表页没有加载成功～")
            else:
                print("好看底bar未显示")

        except:
            print("未进入手百！")

    # 点击好看视频、视频落地页视频
    def test_avideo_515_322(self):
        path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        pathTopic = path + '/' + 'TopicDuration' + '/' + 'video_duration'
        print("\n" + "点击好看视频、视频落地页视频, 测试515，322")
        time.sleep(3)
        self.dialog_idshow()
        try:
            videobar = self.driver.find_elements_by_id("com.baidu.searchbox:id/home_tab_item_textview")[
                1]  # 点击好看视频底bar
            PublicFunction.writeDateToFile(515, 1, pathTopic, 1)
            if videobar.is_displayed():
                videobar.click()
                time.sleep(10)
                image = self.driver.find_elements_by_id("com.baidu.searchbox:id/tab_video_img")[0]  # 点击好看视频列表视频
                if image.is_displayed():
                    image.click()
                    time.sleep(10)
                    try:
                        error_isdispaly = 0
                        self.driver.find_element_by_id(
                            "com.baidu.searchbox:id/feed_video_play_error")  # 视频播放失败浮层，不上报日志
                    except:
                        error_isdispaly = 1
                        print("播放成功！")
                    self.assertNotEqual(error_isdispaly, 0, msg="播放不成功")
                else:
                    print("推荐tab未显示")

                self.driver.find_elements_by_id("com.baidu.searchbox:id/tab_indi_title")[1].click()  # 切换列表tab
                time.sleep(10)
                if image.is_displayed():
                    authors = self.driver.find_elements_by_id(
                        "com.baidu.searchbox:id/tab_video_author_text")  # 获得百家号作者title
                    authors[0].click()  # 点击进入落地页
                    time.sleep(10)
                    self.is_error()
                    self.is_4G()
                    banck = self.driver.find_element_by_id("com.baidu.searchbox:id/redtip_icon")  # 点击落地页返回
                    if banck.is_displayed():
                        banck.click()
                else:
                    print("搞笑tab未显示")
            else:
                print("好看频道未显示")
        except:
            print("未进入手百")



if __name__ == "__main__":
    unittest.main()
