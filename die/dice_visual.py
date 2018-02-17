from die import Die
import pygal

#创建两个骰子实例
die_1 = Die()
die_2 = Die(10)

#统计多次结果，并存储
# results = []
# for roll_num in range(5000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
results = [die_1.roll() + die_2.roll() for roll_num in range(5000)]

#分析结果
# frequencies = []
# max_result = die_2.num_sides + die_1.num_sides
# for value in range(2,max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
max_result = die_2.num_sides + die_1.num_sides
frequencies = [results.count(value) for value in range(2,max_result+1)]

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 dice 5000 times."
hist.x_labels = map(str,range(2,17))
hist.x_title = 'Result'
hist.y_title = 'Frequncy of Result'

hist.add('D6+D10',frequencies)
hist.render_to_file('dice_visual.svg')
