from dice import DD
import pygal

di_1 = DD()
di_2 = DD()
di_3 = DD()

restuest = [di_1.roll()+di_2.roll()+di_3.roll() for values in range(1000)]
frequencise = [restuest.count(value) for value in range(3,19)]


hist = pygal.Bar()

hist.title = 'Three D6 sum.'
hist.x_title = "Result"
hist.y_title = "Frequency"
hist.x_labels = map(str,range(1,13))

hist.add('Three D6',frequencise)
hist.render_to_file('threeD6.svg')
