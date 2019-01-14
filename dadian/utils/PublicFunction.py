# -*- coding: utf-8 -*-
from appium import webdriver

import os

def appium_start():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = 'PBV5T16C06007020'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['fullReset'] = False
    desired_caps['noReset'] = True
    desired_caps['recreateChromeDriverSessions'] = True
    desired_caps['appPackage'] = 'com.baidu.searchbox'
    desired_caps['appActivity'] = '.MainActivity'

    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    return driver
    # 这里init应该进入到对应的页面哦～

def get_windowsize(self):
    xy = self.driver.get_window_size()
    x = xy['width']
    y = xy['height']
    return x, y

def upslide(self):
    x = get_windowsize(self)[0]
    y = get_windowsize(self)[1]
    self.driver.swipe(0.5 * x, 0.9 * y, 0.5 * x, 0.1 * y, 1000)  # 向上滑

def downslide(self):
    x = get_windowsize(self)[0]
    y = get_windowsize(self)[1]
    self.driver.swipe(0.5 * x, 0.1 * y, 0.5 * x, 0.9 * y, 1000)  # 向下滑

def leftslide(self):
    x = get_windowsize(self)[0]
    y = get_windowsize(self)[1]
    self.driver.swipe(0.8 * x, 0.5 * y, 0.2 * x, 0.5 * y, 1000)  #向左滑

def rightslide(self):
    x = get_windowsize(self)[0]
    y = get_windowsize(self)[1]
    self.driver.swipe(0.2 * x, 0.5 * y, 0.9 * x, 0.5 * y, 1000)  #向右滑

def writeDateToFile(point, i, path, duration):
    # pwd = os.getcwd()
    # filePath = pwd + '/TopicDuration/' + path + '/' + str(point) + "_" + str(i) + ".txt"
    # filePath ='/Users/v_lixinyan01/Pycharm/TopicDuration/' + path + '/' + str(point) + "_" + str(i) + ".txt"
    filePath = path + '/' + str(point) + "_" + str(i) + ".txt"


    with open(filePath, "a") as file:
        file.write(str(duration))
