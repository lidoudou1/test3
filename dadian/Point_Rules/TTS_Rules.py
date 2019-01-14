
#coding=utf-8
__author__ = 'lixuefang'

#预先设定每个点的个数,
dict_dest_count = {
    '442': 6,
    '724': 4,
    # '656': 2,
    '655': 1,
}
#该变量中的点必须在上面变量中存在
dict_desc_rules = {
    # 724_1表示，点724第一次出现
    '724_1': {
        "content": ['"from":"tool"', '"source":"minibar"', '"value":"frontend"'],
    },
    '724_2': {
        "content": ['"type":"audio_player_detail"', '"source":"full"'],
    },
    '724_3': {
        "content": ['"source":"minibar"', '"page":"tts"'],
    },
    '724_4': {
        "content": ['"source":"minibar"', '"tts_format":"full_text"'],
    },
    # '656_1': {
    #     "content": ['"from":"feed"', '"type":"kt_tts_clk"', '"source":"close"']
    # },
    # '656_2': {
    #     "content": ['"from":"feed"', '"type":"kt_tts_clk"', '"source":"open"']
    # },
    '655_1': {
        "content": ['"value":"play"', '"from":"feed"', '"type":"kt_tts_btn"', '"source":"active"']
    },
    '442_1': {
        "content": ['"value":"pre"', '"from":"tool"', '"type":"jump_btn_clk"', '"source":"full"']
    },
    '442_2': {
        "content": ['"value":"play"', '"from":"tool"', '"type":"play_btn_clk"', '"source":"full"']
    },
    '442_3': {
        "content": ['"value":"1"', '"page":"tts"', '"type":"player_show"', '"source":"full"']
    },
    '442_4': {
        "content": ['"value":"stop"', '"from":"tool"', '"type":"play_btn_clk"', '"source":"minibar"']
    },
    '442_5': {
        "content": ['"value":"next"', '"from":"tool"', '"type":"jump_btn_clk"', '"source":"minibar"']
    },
    '442_6': {
        "content": ['"value":"1"', '"from":"tool"', '"type":"player_show"', '"source":"minibar"']
    },
}
