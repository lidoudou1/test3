#/usr/bin/env
# -*- coding:utf-8 -*

import os
import sys
import time
import traceback

# from log import logger

from selenium.common.exceptions import NoSuchElementException

def isElement(self,identifyBy,c, multipe = False, wait = 10):
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
            except NoSuchElementException as e:
                # logger.error(traceback.format_exc())
                flag = False

        wait_count += 1

    return flag

def swipe(self, a, b, c, d):
    '''
    usage:
    根据屏幕坐标上滑或者下滑，评估一个大概位置做操作
        #上滑
        self.driver.swipe(x / 2, y / 2, x / 2, y / 4, 200)
        #下滑
        self.driver.swipe(x / 2, y / 4, x / 2, y * 3 / 4, 200)
    :param self:
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    '''
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    # 上滑
    self.driver.swipe(x * a, y * b, x * c, y * d, 200)

def take_screen_shot(self,title):
    '''

    :param self:
    :param classname:
    :param methodname:
    :return:
    '''
    screen_path = sys.path[0] + "/Report/screenpicture/" + self.__class__.__name__
    if not os.path.exists(screen_path):
        try:
            os.makedirs(screen_path)
        except Exception as err:
            # logger.error(traceback.format_exc())
            print("error")
    filename = screen_path + time.strftime('%m_%d_%H_%M', time.localtime(time.time())) + '_' + title + '.png'
    self.driver.get_screenshot_as_file(filename)
    time.sleep(3)
    return filename

def get_coverage(self,second=3):
    '''
    收集覆盖率数据，当前应用至于后台second s，
    driver.background_app(5)  # 置于后台，持续5秒
    driver.background_app(-1) # 持续置于后台
    driver.background_app({'timeout': None}) # 持续置于后台

    :param self:
    :param second:
    :return:
    '''
    self.driver.background_app(second)

def restart_app(self):
    '''
    先关闭当前应用，再启动
    :param self:
    :return:
    '''
    self.driver.close_app()
    self.driver.launch_app()
    time.sleep(2)

def push_configini(mode=1):
    '''
    push外部配置文件,mode=1从mock平台获取配置文件，其他值后续再配置
    :param mode: 获取searchbox.ini的方式
    :return:
    '''
    if mode == 1:
        download_config_cmd = 'wegt http://mock.baidu-int.com:8001/mock/iniConf/qrcodeNormal/doufangfang/searchbox_config.ini'
        os.popen(download_config_cmd)

if __name__ == "__main__":
    push_configini(1)

