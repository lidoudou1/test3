# -*- coding: utf-8 -*-

__author__ = 'lixuefang'

from appium import webdriver
import unittest
import time
from utils import PublicFunction
# import HTMLTestRunner
import os


class FeesTestCase(unittest.TestCase):

    #执行在每个case之前，用于启动手百
    def setUp(self):
        self.driver = PublicFunction.appium_start()

    #执行每个case之后运行，用于退出
    def tearDown(self):
        self.driver.quit()

    '''298：切换Tab页：打3个点：
                1、滑动切换Tab（slidein）；Tab页类型（rn）；非吸顶（home） 
                2、点击切换tab（clkin）；Tab页类型（na）；吸顶（feed） 
                3、新增切换Tab（editin）；Tab页类型（rn）；吸顶（feed）
        59：进入feed吸顶态'''
    def test_FeedMounting_298and59(self):
        print("\n" + "298，59")
        try:
            time.sleep(3)
            PublicFunction.rightslide(self)
            time.sleep(3)
            PublicFunction.rightslide(self)
            time.sleep(10)
            PublicFunction.upslide(self)
            time.sleep(5)
            vdIcon = self.driver.find_elements_by_class_name("android.widget.TextView")
            vdIcon[1].click()
            time.sleep(5)
            self.driver.find_element_by_id("com.baidu.searchbox:id/tab_right_plus").click()
            time.sleep(5)
            # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[25]/android.widget.TextView").click()
            # 点击添加频道下的频道
            feed_multi_tab_item_title_arr = self.driver.find_elements_by_id('com.baidu.searchbox:id/feed_multi_tab_item_title')
            # 关注和推荐不可移动，所以从2开始,没必要添加太多tab
            for i in range(10, 12):
                feed_multi_tab_item_title_arr[i].click()
            time.sleep(5)
            self.driver.keyevent(4)
            time.sleep(2)
        except:
            print("NoSuchElement!")

        self.assertIn("MainActivity", self.driver.current_activity)

    # 313：图集滑动&趣图滑动（暂时不要）
    # 158：图集相关推荐展现
    # 159：图集相关推荐点击
    def test_FeedMounting_313and158and159(self):
        print("\n" + "图集")
        try:
            time.sleep(5)
            self.driver.find_element_by_android_uiautomator("text(\"图片\")").click()
            time.sleep(25)
            # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.TextView").click()
            # self.driver.tap([(0.5*x, 0.5*y)], 1)
            tpelement = self.driver.find_element_by_id("com.baidu.searchbox:id/feed_viewpager")
            tpelement.find_elements_by_class_name("android.widget.ImageView")[0].click()
            time.sleep(2)
            #左划23次
            for i in range(24):
                time.sleep(1)
                PublicFunction.leftslide(self)

            time.sleep(2)
            vdIconb = self.driver.find_elements_by_id("com.baidu.searchbox:id/relative_album_text")
            vdIconb[1].click()
            self.driver.keyevent(4)
            self.driver.keyevent(4)
        except:
            print("NoSuchElement!")

        self.assertIn("MainActivity", self.driver.current_activity)

    #505：底bar点击视频
    def test_FeedMounting_505(self):
        try:
            time.sleep(5)
            self.driver.find_elements_by_id("com.baidu.searchbox:id/home_tab_item_textview")[1].click()  # 点击好看视频底bar
            time.sleep(5)
        except:
            print("NoSuchElement!")

        self.assertIn("MainActivity", self.driver.current_activity)

    # 非吸顶态时间戳，ubc id='507'
    # 吸顶态时间戳，ubc id = '61'
    # 落地页时间戳，ubc id='346'
    def test_FeedMounting_507and61and346(self):
        # starttime = time.time()
        try:
            # 非吸顶态时长--507
            starttime507_3 = time.time()
            time.sleep(20)
            endtime507_3 = time.time()

            # 右划，非吸顶态的时长 --507
            PublicFunction.rightslide(self)
            starttime507_2 = time.time()
            time.sleep(20)
            endtime507_2 = time.time()

            # 上滑，进入吸顶态的时长 --61
            PublicFunction.upslide(self)
            starttime61_3 = time.time()
            time.sleep(20)
            endtime61_3 = time.time()

            # 左划， 进入吸顶态的时长 --61
            PublicFunction.leftslide(self)
            starttime61_2 = time.time()
            time.sleep(20)
            endtime61_2 = time.time()

            # 返回， 进入吸顶态的时长 --61
            self.driver.keyevent(4)
            starttime507_1 = time.time()
            time.sleep(20)
            endtime507_1 = time.time()

            # 点击落地页， 落地页时长打点--346
            self.driver.find_element_by_id("com.baidu.searchbox:id/feed_template_base_title_id").click()
            starttime346_1 = time.time()
            time.sleep(20)
            endtime346_1 = time.time()

            # 返回到推荐列表，进入吸顶态的时长 --61
            self.driver.keyevent(4)
            starttime61_1 = time.time()
            time.sleep(20)
            endtime61_1 = time.time()
            self.driver.keyevent(4)
        except:
            print("NoSuchElement!")
        self.assertIn("MainActivity", self.driver.current_activity)
        duration507_1 = endtime507_1 - starttime507_1
        duration507_2 = endtime507_2 - starttime507_2
        duration507_3 = endtime507_3 - starttime507_3
        duration61_1 = endtime61_1 - starttime61_1
        duration61_2 = endtime61_2 - starttime61_2
        duration61_3 = endtime61_3 - starttime61_3
        duration346_1 = endtime346_1 - starttime346_1

        path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        pathTopic = path + '/' + 'TopicDuration' + '/' + 'feed_duration'
        PublicFunction.writeDateToFile(507, 1, pathTopic, duration507_1)
        PublicFunction.writeDateToFile(507, 2, pathTopic, duration507_2)
        PublicFunction.writeDateToFile(507, 3, pathTopic, duration507_3)
        PublicFunction.writeDateToFile(61, 1, pathTopic, duration61_1)
        PublicFunction.writeDateToFile(61, 2, pathTopic, duration61_2)
        PublicFunction.writeDateToFile(61, 3, pathTopic, duration61_3)
        PublicFunction.writeDateToFile(346, 1, pathTopic, duration346_1)

if __name__ == "__main__":
    unittest.main()
