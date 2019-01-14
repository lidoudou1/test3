
#coding=utf-8
__author__ = 'lixuefang'

#预先设定每个点的个数,
dict_dest_count = {
    '485': 7,
    '322': 6,
    '515': 6,
}
#该变量中的点必须在上面变量中存在
dict_desc_rules = {
    # 724_1表示，点724倒数第一次出现

    '485_5': {
        "content": ['"from":"video"', '"page":"video_landing"'],
    },
    '485_4': {
        "content": ['"from":"video"', '"page":"video_landing"'],
    },
    '485_3': {
        "content": [ '"from":"video"', '"page":"video_landing"']
    },
    '485_2': {
        "content": ['"from":"video"','"page":"videoChannel"'],
    },
    '485_1': {
        "content": ['"from":"video"', '"page":"video_landing"'],
    },


    '515_6': {
        "content": ['"from":"video"', '"type":"first_rec_show"', '"source":"na"', '"page":"videoChannel"', '"value":"channel-na"']
    },
    '515_5': {
        "content": ['"from":"video"', '"type":"first_rec_show"', '"source":"na"', '"page":"videoChannel"', '"value":"channel-na"']
    },
    '515_4': {
        "content": ['"from":"video"', '"type":"first_rec_show"', '"source":"na"', '"page":"video_landing"', '"value":"channel-na"']
    },
    '515_3': {
        "content": ['"from":"video"', '"type":"first_rec_show"', '"source":"na"', '"page":"video_landing"', '"value":"channel-na"']
    },
    '515_2': {
        "content": ['"from":"video"', '"type":"first_rec_show"', '"source":"na"', '"page":"videoChannel"', '"value":"channel-na"']
    },
    '515_1': {
        "content": ['"from":"video"', '"type":"first_rec_show"', '"source":"na"', '"page":"video_landing"', '"value":"channel-na"']
    },

    '322_6': {
        "content": ['"type":"first_frame"', '"from":"video"', '"page":"videoChannel"']
    },
    '322_5': {
        "content": ['"type":"first_frame"','"from":"video"','"page":"videoChannel"']
    },
    '322_4': {
        "content": ['"type":"first_frame"','"from":"video"','"page":"video_landing"']
    },
    '322_3': {
        "content": ['"type":"first_frame"','"from":"video"','"page":"video_landing"']
    },
    '322_2': {
        "content": ['"type":"first_frame"','"from":"video"','"page":"videoChannel"']
    },
    '322_1': {
        "content": ['"type":"first_frame"','"from":"video"','"page":"video_landing"']
    },

}