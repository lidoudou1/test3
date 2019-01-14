
#coding=utf-8
__author__ = 'lixinyan'

#预先设定每个点的个数,
dict_dest_count = {
    '298': 7,
    '505': 1,
    '59': 3,
    '507': 6,
    '61': 5,
    '346': 1
}
#该变量中的点必须在上面变量中存在
dict_desc_rules = {
    # 298_1表示，点298倒数第一次出现
    '298_4': {
        "content": ['"source":"na"', '"frame_source":"video"', '"type":"clkin"', '"ext":"{"source":"feed"}"'],
    },
    '298_5': {
        "content": ['"source":"rn"',  '"frame_source":"feed"', '"type":"editin"', '"ext":"{"source":"feed"}"'],
    },
    '298_6': {
        "content": ['"source":"na"',  '"frame_source":"feed"', '"type":"clkin"', '"ext":"{"source":"feed"}"'],
    },
    '298_7': {
        "content": ['"source":"rn"',  '"frame_source":"feed"', '"type":"slidein"', '"ext":"{"source":"home"}"'],
    },

    '505_1': {
        "content": ['"from":"home"','"type":"tab_clk_video"'],
    },

    '59_1': {
        "content": ['"session_id":'],
    },
    '507_1': {
        "content": ['"source":"na"', '"duration":', '"frame_source":"feed"'],
    },
    '507_2': {
        "content": ['"source":"rn"', '"duration":', '"frame_source":"feed"'],
    },
    '507_3': {
        "content": ['"source":"na"', '"duration":', '"frame_source":"feed"'],
    },

    '61_1': {
        "content": ['"source":"na"', '"duration":','"frame_source":"feed"'],
    },
    '61_2': {
        "content": ['"source":"na"', '"duration":','"frame_source":"feed"'],
    },
    '61_3': {
        "content": ['"source":"rn"', '"duration":','"frame_source":"feed"'],
    },

    '346_1': {
        "content": ['"duration":'],
    },
}
