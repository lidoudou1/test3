from pyecharts import Bar

v1 = [20, 25, 35, 24]
str1 = ['回忆', '生活', '现实', '失败']
bar1 = Bar('testBar_theme', 'Theme')
bar1.add('test01', str1, v1, is_more_utils=True)
bar1.render()
