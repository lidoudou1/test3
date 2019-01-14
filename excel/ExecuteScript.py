# coding=utf-8
__author__ = 'lixuefang'

import os
import shutil
from ConfigInfo import baseConfig
import maxValueStatistic
import diffValueStatistic
from PublicFunctions import fileIsExist
from PublicFunctions import dirIsExist


# 每个场景生成性能数据的文件夹路径path_case2
path_case2 = os.getcwd() + baseConfig['case2']['directory'] + '/'
# 判断这个文件夹是否存在，如果已经存在咋删除，否则重新创建
dirIsExist(path_case2)
for i in range(5):
    print 'test2 第 %s 次' % i
    # 异步执行收集性能数据的脚本
    os.system("nohup python get_cpu_memory_v3.py -c " + path_case2 + " >> nohup.out &")
    # 执行自动化case脚本
    os.system('python /Users/v_lixinyan01/PycharmProjects/CompanyProject/FeedOOMTest/TestCases/FeedPerformanceCase2.py')

#每个场景生成性能数据的文件夹路径path_case3
path_case3 = os.getcwd() + baseConfig['case3']['directory'] + '/'
# 判断这个文件夹是否存在，如果已经存在咋删除，否则重新创建
dirIsExist(path_case3)
for i in range(5):
    print 'test3 第 %s 次' % i
    # 异步执行收集性能数据的脚本
    os.system("nohup python get_cpu_memory_v3.py -c " + path_case3 + " >> nohup.out &")
    # 执行自动化case脚本
    os.system('python /Users/v_lixinyan01/PycharmProjects/CompanyProject/FeedOOMTest/TestCases/FeedPerformanceCase3.py')

#每个场景生成性能数据的文件夹路径path_case4
path_case4 = os.getcwd() + baseConfig['case4']['directory'] + '/'
# 判断这个文件夹是否存在，如果已经存在咋删除，否则重新创建
dirIsExist(path_case4)
for i in range(5):
    print 'test4 第 %s 次' % i
    # 异步执行收集性能数据的脚本
    os.system("nohup python get_cpu_memory_v3.py -c " + path_case4 + " >> nohup.out &")
    # 执行自动化case脚本
    os.system('python /Users/v_lixinyan01/PycharmProjects/CompanyProject/FeedOOMTest/TestCases/FeedPerformanceCase4.py')

#每个场景生成性能数据的文件夹路径path_case5
path_case5 = os.getcwd() + baseConfig['case5']['directory'] + '/'
# 判断这个文件夹是否存在，如果已经存在咋删除，否则重新创建
dirIsExist(path_case5)
for i in range(5):
    print 'test5 第 %s 次' % i
    # 异步执行收集性能数据的脚本
    os.system("nohup python get_cpu_memory_v3.py -c " + path_case5 + " >> nohup.out &")
    # 执行自动化case脚本
    os.system('python /Users/v_lixinyan01/PycharmProjects/CompanyProject/FeedOOMTest/TestCases/FeedPerformanceCase5.py')

# 每个场景生成性能数据的文件夹路径path_case6
path_case6 = os.getcwd() + baseConfig['case6']['directory'] + '/'
# 判断这个文件夹是否存在，如果已经存在咋删除，否则重新创建
dirIsExist(path_case6)
for i in range(5):
    print 'test6 第 %s 次' % i
    # 异步执行收集性能数据的脚本
    os.system("nohup python get_cpu_memory_v3.py -c " + path_case6 + " >> nohup.out &")
    # 执行自动化case脚本
    os.system('python /Users/v_lixinyan01/PycharmProjects/CompanyProject/FeedOOMTest/TestCases/FeedPerformanceCase6.py')

print('脚本执行完毕！')
# 最终调用maxValueStatistic 和 diffValueStatistic生成峰值和差值的报告
maxValueStatistic.statisticDataResult()
diffValueStatistic.caculateDiffData()

