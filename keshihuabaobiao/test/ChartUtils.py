import matplotlib.pyplot as plt
import time
from matplotlib.font_manager import FontManager
from pylab import mpl


def showBarChart(dictData):
    # 必须配置中文字体，否则会显示成方块
    # 注意所有希望图表显示的中文必须为unicode格式
    custom_font = mpl.font_manager.FontProperties(fname='hwxw.ttf')

    for a, b in dictData.items():
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    x_axis = tuple(dictData.keys())
    y_axis = tuple(dictData.values())
    plt.bar(x_axis, y_axis, color='rgb', alpha=0.7)

    plt.xlabel(u"刷新阶段", fontproperties=custom_font)
    plt.ylabel(u"耗时", fontproperties=custom_font)
    plt.title(u"840刷新报表", fontproperties=custom_font)
    plt.ylim(-100, 3000)
    plt.savefig('{}.png'.format(time.strftime('%Y%m%d%H%M%S')))
    plt.show()
