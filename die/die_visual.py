from die import Die
import pygal

#创建一个骰子
die = Die()

#收集1000次中出现的点数
# resultes = []
# for roll_num in range(1000):
#     resulte = die.roll()
#     resultes.append(resulte)

#使用列表解释
resultes = [die.roll() for roll_num in range(1000)]


#统计1~6，个点数出现的次数
# frequencies = []
# for value in range(1,die.num_sides+1):
#     frequency = resultes.count(value)
#     frequencies.append(frequency)

    # 使用列表解释
frequencies = [resultes.count(value) for value in range(1,die.num_sides+1)]
#绘制图表，显示出来，具体参数可去pygal官网查看
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels =map(str,range(1,7))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')