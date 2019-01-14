#coding=utf-8
__author__ = 'lixinyan'

from Point_Rules import TTS_Rules
from Point_Rules import Video_Rules
from Point_Rules import Feed_Rules
from Point_Rules import Ugc_Rules
from SearchboxTestCase.OutputReport import fileIsExist
from SearchboxTestCase.OutputReport import dataParser
from SearchboxTestCase.OutputReport import statisticsPoints
from SearchboxTestCase.OutputReport import writeToHtml
from SearchboxTestCase import GetContext
import os
import time


def functionSet(durationPath, pointLog, Topic, pointRules, testCase,dict_total_points):
    # 在每执行一个case文件的时候，先判断是否有该topic的duration文件。如果有，删除后再创建。
    durationP = os.path.join('TopicDuration/' + durationPath)
    fileIsExist(durationP)

    # 在每执行一个case文件的时候，先判断是否有该topic的ubclog文件（从UCenter平台拉取下拉的）。如果有，删除后再创建。
    ubcP = os.path.join('UBCLog/' + pointLog)
    fileIsExist(ubcP)

    # 在执行case前先获得当前的时间戳A，从UCenter平台拉取数据时获取该时间戳A之后的数据。
    implementtime = time.time()
    print(implementtime)

    # 被执行case的路径，跟进每个人的路径做修改
    testcasepath = "python /Users/lixuefang/Pycharm/SearchboxTestCase/" + str(testCase)
    os.system(testcasepath)
    time.sleep(30)

    # 根据上面获得的时间戳，调用GetContext讲拉取的数据存储到logPath里面
    logPath = os.path.join(ubcP + '/' + Topic + '.txt')
    GetContext.getData(implementtime, logPath)

    # 调用OutputReport进行对比。对比项有：1.预取点是否存在 2.预取点的次数是否一致，是否有多打或漏打的情况 3.预取点的参数是否正确 4.如果是时长打点，判断duration是否准确
    dataParser(logPath, Topic, pointRules, durationP,dict_total_points)

if __name__ == "__main__":
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

    functionSet('feed_duration', feedLog, "FEED", Feed_Rules, 'FeedTestCase.py', dict_total_points)
    # functionSet('tts_duration', ttsLog, "TTS", TTS_Rules, 'TTSTestCase.py', dict_total_points)
    # functionSet('video_duration', videoLog, "VIDEO", Video_Rules, 'VideoTestCase.py', dict_total_points)
    # functionSet('ugc_duration', ugcLog, "UGC", Ugc_Rules, 'UgcTestCase.py', dict_total_points)

    writeToHtml()
