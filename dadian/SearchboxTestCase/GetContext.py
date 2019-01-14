# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'lixuefang'

import urllib
import json
import time


#读取页面源码
def read_pageHtml(url):
    file = urllib.urlopen(url)
    data = file.read()
    return data

#把文件json化并存储到本地
def storageToLocalFiles(storagePath, data):
    with open(storagePath, 'w') as json_file:
        json_file.write(json.dumps(data, ensure_ascii=False))

#手机为cuid，获取n页的目标数据段
def saveNpage(cuid, inputtime):
    allData = []
    n = 1
    while True:
        url = 'http://10.44.87.166:8260/ucenter?model=ubc&page=validateList&action=ajax' + '&cuid=' + str(cuid) + '&rn=40' + '&p=' + str(n)
        #data为爬取页面信息
        data = read_pageHtml(url)
        newData = getParams(data, inputtime, allData)
        if newData:
            n += 1
            allData = newData
        else:
            break
    #for i in range(n):
    #    url = 'http://ucenter.mbd.baidu.com/ucenter?model=ubc&page=validateList&action=ajax'+'&cuid='+str(cuid)+'&rn=40' + '&p='+str(i)
    #    data = read_pageHtml(url)
    #    allData = getParams(data, inputtime, allData)

    return allData

#取目标文件（此处为url）中的某些字段
def getParams(urlData, inputtime, redata):
    res = json.loads(urlData)  # urlData 就是从url请求返回的数据,经过解析之后，是 字典 类型
    print(res)
    count = 0
    for item in res['rows']:  #遍历list，去拿rows中的值
        time = item['index_time']
        if time < inputtime:
            break
        count += 1
        action_data = item['action_data']

        message = item['message']
        ubcid= item['ubcid']
        itemdata = {
            'time': time,
            'ubcid': ubcid,
            'action_data': action_data,
            'message': message
        }#把需要的字段都放入到字典中
        redata.append(itemdata)
    if count == 0:
        return False
    return redata


def getJson(objItem):

    res = json.loads(objItem)
    item = []
    for key in res:
        if key is None:
            continue
        if is_json(res[key]) is True:
            t = {
                key: getJson(res[key])
            }
        else:
            t = {
                key: res[key]
            }
        item.append(t)
    return item

def is_json(myjson):
    try:
        myjson=str(myjson)
        a =json.loads(myjson)
        if isinstance(a, dict) is True:
            return True
        else:
            return False
    except ValueError:
        return False

#将ubc平台的打点信息存储到对应的log文件中
def getData(timestamp, storagePath):
    data = saveNpage('D323A318A98E66C4D9A9FCA5A050B6B4|0', timestamp)
    storageToLocalFiles(storagePath, data)

if __name__ == "__main__":
    data = saveNpage('D323A318A98E66C4D9A9FCA5A050B6B4|0', 1539332607.901284)
    storagePath = "UBC_log.txt"
    storageToLocalFiles(storagePath, data)
