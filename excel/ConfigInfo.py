# coding=utf-8
__author__ = 'lixuefang'

import os

path = os.getcwd()

baseConfig = {

        #colimns平均值
        #time_columns差值

    # 'case1': {
    #     'directory': '/Data/case1_refresh',
    #     'columns': ['CPU%', 'VSS', 'RSS'],
    #     'time_columns': ['CPU%', 'RSS'],
    #     'time_file': 'time_case1.txt',
    #     'description': '1.冷启动手百后，静置1min'
    # },

    'case2': {
        'directory': '/Data/case2_refresh',
        'columns': ['CPU%', 'VSS', 'RSS'],
        'time_columns': ['CPU%', 'RSS'],
        'time_file': 'time_case2.txt',
        'description': '冷启动手百后，静置30s。反复刷新10次，至当屏数据完全展现'
    },

    'case3': {
        'directory': '/Data/case3_refresh',
        'columns': ['CPU%', 'VSS', 'RSS'],
        'time_columns': ['CPU%', 'RSS'],
        'time_file': 'time_case3.txt',
        'description': '冷启动手百后，静置30s。反复进入同一篇图文落地页10次，至相关推荐展现，评论展现一屏。'
    },
    'case4': {
        'directory': '/Data/case4_refresh',
        'columns': ['CPU%', 'VSS', 'RSS'],
        'time_columns': ['CPU%', 'RSS'],
        'time_file': 'time_case4.txt',
        'description': '冷启动手百后，静置30s。反复进入10篇不同图文落地页，至相关推荐展现，评论展现一屏'
    },
    'case5': {
        'directory': '/Data/case5_refresh',
        'columns': ['CPU%', 'VSS', 'RSS'],
        'time_columns': ['CPU%', 'RSS'],
        'time_file': 'time_case5.txt',
        'description': '冷启动手百后，静置30s。反复进入同一篇图集落地页10次，至相关推荐展现。'
    },
    'case6': {
        'directory': '/Data/case6_refresh',
        'columns': ['CPU%', 'VSS', 'RSS'],
        'time_columns': ['CPU%', 'RSS'],
        'time_file': 'time_case6.txt',
        'description': '冷启动手百后，静置30s。反复进入10篇不同图集落地页，至相关推荐展现'
    }

}

# 设置maxValueStatistics（峰值）需要判断的属性以及每个属性的阈值
maxCompareData = {
    'VSS': 2.8,
    'RSS': 1,
}

# 设置diffValueStatistics（稳定性）需要判断的属性以及每个属性的阈值
diffCompareData = {
    'CPU%': {
        'avg': 80,
        'diff': 5,
    },
    'RSS': {
        'avg': 600000.0,
        'diff': 50000,
    }
}