#coding=utf-8
#__author__ = 'lixuefang'

import shutil
import os
import json

from SearchboxTestCase import GetContext
from Point_Rules import TTS_Rules
from Point_Rules import Video_Rules
from Point_Rules import Feed_Rules
from Point_Rules import Ugc_Rules
import time

playStatResult = "<font color=\"#009100\">Pass</font>"
scriptcontent = "<script type=\"text/javascript\">"
jsoncontent = ""
realcontent = ""
statisticshtml = ""

#记录每种类型的点的个数
dict_total_points = {}


# 如果存在duration，判断是否准确
def juageIsHasDuration(dict_action_data, durationpath, times_key): # dict_actual_count为从ubc平台获取的数据；times_key为duration文件夹下，生成的文件名称
    file_name = str(durationpath) + "/" + times_key + ".txt"
    if "content" in dict_action_data.keys():
        dict_content = json.loads(dict_action_data["content"])
        if "duration" in dict_content.keys():
            if os.path.exists(file_name):
                f = open(file_name, 'r')
                time = float(f.read())
            else:
                return '<font color="#FF0000">无文件</font>'
            duration = float(dict_content["duration"])
            if abs(time - duration) <= 10:
                return "准确"
            else:
                playStatResult = '<font color="#FF0000">Fail</font>'
                return '<font color="#FF0000">值不准确</font><br>' + "实际值: "+str(time) + "<br>ubc平台值: " + str(duration)
        else:
            return "无duration值"
    return "异常,无content字段"


# 将结果写入html文件
def writeToHtml():
    reportPath = "../Report/repor" \
                 "t_feed.html"
    global scriptcontent
    scriptcontent += "</script>"
    with open("../template.html", 'r') as template:
        finalcontent = template.readlines()
    with open(reportPath, "w") as report:
        for line in finalcontent:
            if "pointsstatistics" in line:
                line = line.replace("pointsstatistics", statisticshtml)
            if "realcontent" in line:
                line = line.replace("realcontent", realcontent)
            if "scriptcontent" in line:
                line = line.replace("scriptcontent", scriptcontent)
            if "jsoncontent" in line:
                line = line.replace("jsoncontent", jsoncontent)
            report.write(line)


# 从point_rules中获取设定的目标点
def getDestPoints(point_rules):
    re_points = []
    dest_points = point_rules.dict_desc_rules.keys()
    for item in dest_points:
        point = item.split('_')
        re_points.append(point[0])
    return list(set(re_points))


# 将日志文件格式化
def getScriptCode(id, id_key):
    html = 'var text = document.getElementById(\'' + id_key + '\').innerText;'
    html += 'document.getElementById(\'' + id + '\').innerText = JSON.stringify(JSON.parse(text), null, 2);'
    return html


# 判断文件夹是否存在，如果存在，删除文件夹后再重新创建
def fileIsExist(durarionpath):
    flag = os.path.exists(durarionpath)
    if flag:
        shutil.rmtree(durarionpath)
    os.makedirs(durarionpath)


#将ubc信息与规则做对比，并返回结果
def dataParser(logpath, pointType, point_rules, durationpath):
    global realcontent
    global jsoncontent
    global scriptcontent
    global dict_total_points
    # 获取从ubc平台爬取的数据，从UBC_log.txt中读取数据并转化成json类型
    with open(logpath, 'r') as file:
        context = file.read()
        data = json.loads(context)

    # itemDict = {}  # 字典类型,
    # context_points = []  # 文件中的所有points

    dict_actual_count = {}  # 记录每个点实际打的个数, ubcid: count
    dict_point_times = {}  # 每个点第几次出现
    dest_points = getDestPoints(point_rules)  # 获取point_rules设定的点

    # 统计UBC_log.txt中每个点出现的实际个数
    # for item in data:
    #     ubcid = item["ubcid"]
    #     count = 1
    #     if ubcid in dict_actual_count.keys():
    #         count = dict_actual_count[ubcid]
    #         count += 1
    #     dict_actual_count[ubcid] = count


    list_exist_points = []  # 目标点存在的所有的点
    dict_times_keys = point_rules.dict_desc_rules.keys()  # point_rules中所有要判断的点

    pass_points = []
    fail_points = []
    for item in data:
        ubcid = item["ubcid"]
        # step1: 判断该点是否存在在目标点中
        if ubcid in dest_points:
            playStatResult = "<font color=\"#009100\">Pass</font>"
            is_exist = 1
            json_action_data = item["action_data"]  # action_data中的值,json 类型
            dict_action_data = json.loads(json_action_data)  # 把json类型转换为字典类型
            json_content = dict_action_data["content"]  # 把action_data中的content字段值取出来
            json_content = json_content.replace('\\', '')

            # step2: 该点是要判断的点，则计算该点是第几次出现
            count = 1
            if ubcid in dict_point_times.keys():
                count = dict_point_times[ubcid]
                count += 1
            dict_point_times[ubcid] = count
            times_key = ubcid + "_" + str(count)

            # step3: 判断该点中字段的值是否符合设定的字段值
            if times_key in dict_times_keys:
                list_exist_points.append(times_key)
                dest_content = point_rules.dict_desc_rules[times_key]["content"]
                is_in = ""
                for key_value in dest_content:
                    # 如果不存在
                    if json_content.find(key_value) < 0:
                        is_exist = 0
                        is_in += key_value + ': <font color="#FF0000">错误</font><br/>'
                    else:
                        is_in += key_value + ': <font color="#009100">正确</font><br/>'

                # step4: 判断预先设定的点个数是否和实际的点个数据相等
                dest_count = point_rules.dict_dest_count[ubcid]  # 预先设定的点的个数
                actual_count = dict_actual_count[ubcid]  # 实际的点的个数
                if dest_count == actual_count:
                    is_equal = "是"
                else:
                    is_exist = 0
                    is_equal = '<font color="#FF0000">否</font>'

                # step5: 取message中的值
                message_ubc = item["message"]

                # step6: 判断duration值
                duration = juageIsHasDuration(dict_action_data, durationpath, times_key)
                if (duration != "准确") and (duration != "无duration值"):
                    is_exist = 0
                else:
                    duration = "<font color=\"#009100\">" + duration + "</font>"
                if is_exist == 0:
                    playStatResult = '<font color="#FF0000">Fail</font>'
                    fail_points.append(times_key)
                else:
                    pass_points.append(times_key)

                # step7: 数据html数据
                # 输出打点以及测试结果
                realcontent += "<tr><td>" + pointType + "</td><td>" + times_key + "</td><td>" + playStatResult + "</td>"
                # 输出参数是否准确以及ubc平台解析结果
                realcontent += "<td>" + is_in + "</td><td>" + message_ubc + "</td>"
                # 输出打点次数与预期结果是否一致
                realcontent += "<td>预期次数：" + str(dest_count) + "<br/>实际次数：" + str(
                    actual_count) + "<br/>是否相等：" + is_equal + "</td>"
                # 如果存在duration参数，判断是否准确
                realcontent += "<td>" + duration + "</td><td><p id='" + times_key + "'></p></td></tr>"
                id_key = times_key + "_"
                jsoncontent += "<p id = '" + id_key + "'>" + json_action_data + "</p>"
                scriptcontent += getScriptCode(times_key, id_key)

    dict_total_points[pointType]["pass"] = pass_points
    dict_total_points[pointType]["fail"] = fail_points
    for point in dict_times_keys:
        if point in list_exist_points:
            continue
        else:
            dict_total_points[pointType]["fail"].append(point)
            playStatResult = '<font color="#FF0000">Fail</font>'
            realcontent += "<tr><td>" + pointType + "</td><td>" + point + "</td><td>" + playStatResult + "</td>"
            realcontent += "<td></td><td></td>"
            realcontent += "<td></td>"
            realcontent += "<td></td><td></td></tr>"

#执行脚本并创建写入ubc平台信息
#时长打点文件(feed_duration)，打点数据(ubclog_feed)，topic(feed)，打点规则(feed_rules)，执行场景文件(feedtestcase）
def functionSet(durationPath, pointLog, Topic, pointRules, testCase):
    #
    durationP = os.path.join('../TopicDuration/' + durationPath)
    fileIsExist(durationP)
    ubcP = os.path.join('../UBCLog/' + pointLog)
    fileIsExist(ubcP)
    implementtime = time.time()
    testcasepath = "python /Users/v_lixinyan01/PycharmProjects/CompanyProject/dadiancase/SearchboxTestCase/" + str(testCase)
    os.system(testcasepath)
    time.sleep(30)
    logPath = os.path.join(ubcP + '/' + Topic + '.txt')
    GetContext.getData(implementtime, logPath)
    dataParser(logPath, Topic, pointRules, durationP)

def statisticsPoints():
    type_keys = dict_total_points.keys()
    global statisticshtml

    #statisticshtml = "<p>"

    for key in type_keys:
        pass_list = dict_total_points[key]["pass"]
        fail_list = dict_total_points[key]["fail"]
        total_pass = len(pass_list)
        total_fail = len(fail_list)
        total_count = total_fail + total_pass
        pass_list = ",".join(pass_list)
        fail_list = ",".join(fail_list)
        # statisticshtml += "类型:" + key + ",pass点个数:" + str(total_pass) + ",pass点列表:" + pass_list
        # statisticshtml += ",fail点个数:" + str(total_fail) + ",fail点列表:" + fail_list + "<br/>"
        statisticshtml += "<tr><td>" + key + "</td><td>" + str(total_count) + "</td><td>" + str(total_pass) + "</td>"
        statisticshtml += "<td>" + str(total_fail) + '</td><td><font color="#009100">' + pass_list + '</font></td><td><font color="#FF0000">' + fail_list + "</font></td></tr>"
    # statisticshtml += "</p>"

if __name__ == '__main__':
    ttsLog = "ubclog_tts"
    feedLog = "ubclog_feed"
    ugcLog = "ubclog_ugc"
    videoLog = "ubclog_video"

    dict_total_points = {
        "FEED": {"pass": [], "fail": []},
        "TTS": {"pass": [], "fail": []},
        "VIDEO": {"pass": [], "fail": []},
        "UGC": {"pass": [], "fail": []},
    }

    functionSet('feed_duration', feedLog, "FEED", Feed_Rules, 'FeedTestCase.py')
    functionSet('tts_duration', ttsLog, "TTS", TTS_Rules, 'TTSTestCase.py')
    functionSet('video_duration', videoLog, "VIDEO", Video_Rules, 'VideoTestCase.py')
    # functionSet('ugc_duration', ugcLog, "UGC", Ugc_Rules, 'UgcTestCase.py')

    # 统计点
    statisticsPoints()
    writeToHtml()
