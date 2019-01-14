# coding=utf-8

__author__ = 'lixuefang'

from appium import webdriver
import shutil
import os
import time
import sys

def appium_start():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = '36LBB18228505405'
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

# 判断文件夹是否存在，如果存在，删除文件夹后再重新创建
def dirIsExist(durarionpath):
    flag = os.path.exists(durarionpath)
    if flag:
        shutil.rmtree(durarionpath)
        time.sleep(1)
    os.makedirs(durarionpath)


# 判断文件是否存在，如果存在，删除文件后再重新创建
def fileIsExist(filepath):
    flag = os.path.exists(filepath)
    if flag:
        os.remove(filepath)


def writeDateToFile(timeData, path):
    with open(path, "a") as file:
        file.writelines(str(timeData) + '\n')

def restart_app(self):
    '''
    先关闭当前应用，再启动
    :param self:
    :return:
    '''
    self.driver.close_app()
    self.driver.launch_app()
    time.sleep(60)
    print(1)

def isElement(self,identifyBy,c, multipe = False, wait = 2):
    '''
    一个元素是否存在，考虑到网络、性能等因素，如果10s一个元素还未检测到，说明没有这个元素
    Usage:
    isElement(By.XPATH,"//a")
    :param self:
    :param identifyBy:
    :param c:
    :return:
    '''
    time.sleep(1)
    flag=None
    wait_count = 1
    while(wait_count < wait):
        if(flag == False or flag == None):
            time.sleep(1)
            try:
                if multipe == False:
                    if identifyBy == "id":
                        self.driver.find_element_by_id(c)
                    elif identifyBy == "xpath":
                        self.driver.find_element_by_xpath(c)
                    elif identifyBy == "class":
                        self.driver.find_element_by_class_name(c)
                    elif identifyBy == "link text":
                        self.driver.find_element_by_link_text(c)
                    elif identifyBy == "partial link text":
                        self.driver.find_element_by_partial_link_text(c)
                    elif identifyBy == "name":
                        self.driver.find_element_by_name(c)
                    elif identifyBy == "tag name":
                        self.driver.find_element_by_tag_name(c)
                    elif identifyBy == "css selector":
                        self.driver.find_element_by_css_selector(c)
                    flag = True
                if multipe == True:
                    if identifyBy == "id":
                        self.driver.find_elements_by_id(c)
                    elif identifyBy == "xpath":
                        self.driver.find_elements_by_xpath(c)
                    elif identifyBy == "class":
                        self.driver.find_elements_by_class_name(c)
                    elif identifyBy == "link text":
                        self.driver.find_elements_by_link_text(c)
                    elif identifyBy == "partial link text":
                        self.driver.find_elements_by_partial_link_text(c)
                    elif identifyBy == "name":
                        self.driver.find_elements_by_name(c)
                    elif identifyBy == "tag name":
                        self.driver.find_elements_by_tag_name(c)
                    elif identifyBy == "css selector":
                        self.driver.find_elements_by_css_selector(c)
                    flag = True
            except:
                # logger.error(traceback.format_exc())
                flag = False

        wait_count += 1

    return flag

