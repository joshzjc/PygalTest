from rwalk import Randoms
import pygal

rw = Randoms()
rw.fill_work()

hist = pygal.Dot(x_label_rotation=30)
hist.title = "RandomWork"
hist.x_labels = rw.x_values[:]
hist.add('RandomWorkle',rw.y_values)
hist.render_to_file('RandomWork.svg')