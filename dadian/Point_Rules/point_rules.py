
#coding=utf-8
__author__ = 'lixuefang'

#预先设定每个点的个数,
dict_dest_count = {
    '442': 6,
    '724': 4,
    '656': 2,
    '298': 6,
    '505': 1,
    '59': 1,
    '158': 1,
    '159': 1,
    '485': 7,
    '322': 6,
    '515': 6,
    '593': 11,
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
    '656_1': {
        "content": ['"from":"feed"', '"type":"kt_tts_clk"', '"source":"close"']
    },
    '656_2': {
        "content": ['"from":"feed"', '"type":"kt_tts_clk"', '"source":"open"']
    },


    '442_1': {
        "content": ['"value":"pre"', '"source":"full"', '"from":"tool"', '"type":"jump_btn_clk"']
    },
    '442_2': {
        "content": ['"value":"play"', '"source":"full"', '"from":"tool"', '"type":"play_btn_clk"']
    },
    '442_3': {
        "content": ['"value":"1"', '"source":"full"', '"from":"tool"', '"type":"player_show"']
    },
    '442_4': {
        "content": ['"value":"stop"', '"source":"minibar"', '"from":"tool"', '"type":"play_btn_clk"']
    },
    '442_5': {
        "content": ['"value":"next"', '"source":"minibar"', '"from":"tool"', '"type":"jump_btn_clk"']
    },
    '442_6': {
        "content": ['"value":"1"', '"source":"minibar"', '"from":"tool"', '"type":"player_show"']
    },
    '298_1': {
        "content": ['"source":"na"', '"frame_source":"video"', '"type":"clkin"', '"ext":"{"source":"feed"}"'],
    },
    '298_3': {
        "content": ['"source":"rn"',  '"frame_source":"feed"', '"type":"editin"', '"ext":"{"source":"feed"}"'],
    },
    '298_4': {
        "content": ['"source":"na"',  '"frame_source":"feed"', '"type":"clkin"', '"ext":"{"source":"feed"}"'],
    },
    '298_5': {
        "content": ['"source":"rn"',  '"frame_source":"feed"', '"type":"slidein"', '"ext":"{"source":"home"}"'],
    },
    '505_1': {
        "content": ['"from":"home"', '"type":"tab_clk_video"'],
    },
    '59_1': {
        "content": ['"session_id":'],
    },
    '158_1': {
        "content": ['"currentNid":', '"recommendContexts":"{"nid":}"'],
    },
    '159_1': {
        "content": ['"currentNid":', '"nid":'],
    },


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

    '593_1': {
        "content": ['"from":"ugc"', '"type":"pub_click"', '"page":"publish_forward"']
    },
    '593_2': {
        "content": ['"from":"ugc"', '"type":"topic_click"', '"page":"publish_forward"']
    },
    '593_3': {
        "content": ['"from":"ugc"', '"type":"at_click"', '"page":"publish_forward"']
    },
    '593_4': {
        "content": ['"from":"ugc"', '"type":"emoji_click"', '"page":"publish_forward"']
    },
    '593_5': {
        "content": ['"from":"ugc"', '"type":"show"', '"page":"publish_forward"']
    },
    '593_6': {
        "content": ['"from":"ugc"', '"type":"pub_click"', '"page":"publish"']
    },
    '593_7': {
        "content": ['"from":"ugc"', '"type":"topic_click"', '"page":"publish"']
    },
    '593_8': {
        "content": ['"from":"ugc"', '"type":"at_click"', '"page":"publish"']
    },
    '593_9': {
        "content": ['"from":"ugc"', '"type":"photo_click"', '"page":"publish"']
    },
    '593_10': {
        "content": ['"from":"ugc"', '"type":"emoji_click"', '"page":"publish"']
    },
    '593_11': {
        "content": ['"from":"ugc"', '"type":"show"', '"page":"publish"']
    },
}
