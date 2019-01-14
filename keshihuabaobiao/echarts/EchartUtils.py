# encoding: utf-8
import time
import numpy
from pyecharts import Bar, Line, Pie, Page
import sys

reload(sys)

sys.setdefaultencoding('utf8')

"""
图表绘制工具类，目前支持柱状图、折线图、饼图。
可复用、可扩展
"""

#生成柱状图
def show840Bar(dictData, renderAlone):
    """
    840柱状图
    dictData:{'A':2,'B':3,...}
    renderAlone:是否单独渲染
    """
    bar = Bar('840刷新报表', '平均值',
              title_pos='center',
              width=1600, height=900,
              page_title='840刷新报表')
    x_axis = tuple(dictData.keys())
    y_axis = tuple(dictData.values())
    bar.add('840刷新报表', x_axis, y_axis,
            legend_orient="vertical",
            legend_pos='left',
            is_visualmap=True,
            visual_range=[-500, 3000],
            is_more_utils=True,
            is_datazoom_show=True,
            is_label_show=True,
            label_pos='top')
    # 其他主题：vintage,macarons,infographic,shine，roma
    bar.use_theme('vintage')
    if renderAlone:
        bar.render('840-bar-{}.html'.format(time.strftime('%Y%m%d%H%M%S')))
    else:
        return bar

#生成折线图
def show840Line(headers, arrayData, renderAlone):
    """
    840折线图
    headers:['A','B',...]
    arrayData:{'A':2,'B':3,...}
    renderAlone:是否单独渲染
    """
    line = Line('840刷新报表', '各指标趋势',
                title_pos='center',
                width=1600, height=900,
                page_title='840刷新报表')
    for i in range(0, len(headers)):
        temp = arrayData[i]
        x_axis = numpy.arange(0, len(temp))
        y_axis = temp
        line.add(headers[i], x_axis, y_axis,
                 legend_orient="vertical",
                 legend_pos='left',
                 mark_line=['average'],
                 mark_point=["max", "min"],
                 is_more_utils=True,
                 is_datazoom_show=True,
                 # is_visualmap=True,
                 # visual_range=[-500, 3000],
                 is_label_show=True,
                 label_text_size=15,
                 is_smooth=True,
                 label_pos='top')
        # 其他主题：vintage,macarons,infographic,shine，roma
        # line.use_theme('macarons')
    if renderAlone:
        line.render('840-line-{}.html'.format(time.strftime('%Y%m%d%H%M%S')))
    else:
        return line

#生成饼图
def show840Pie(dictData, renderAlone):
    """
    840饼图，待完善
    dictData:{'A':2,'B':3,...}
    renderAlone:是否单独渲染
    """
    pie = Pie('840刷新报表', '平均值饼图',
              title_pos='center',
              width=1600, height=900,
              page_title='840刷新报表')
    x_axis = tuple(dictData.keys())
    y_axis = tuple(dictData.values())
    pie.add('840刷新报表', x_axis, y_axis,
            legend_orient="vertical",
            legend_pos='left',
            rosetype='radius',
            radius=[30, 70],
            is_more_utils=True,
            is_label_show=True)
    # 其他主题：vintage,macarons,infographic,shine，roma
    pie.use_theme('vintage')
    if renderAlone:
        pie.render('840-pie-{}.html'.format(time.strftime('%Y%m%d%H%M%S')))
    else:
        return pie

#生成所有图
def show840All(*charts):
    """
    840报表相关的图合并在一个文件输出
    """
    page = Page('840刷新报表')
    for temp in charts:
        page.add(temp)
    page.render('840-all-{}.html'.format(time.strftime('%Y%m%d%H%M%S')))
