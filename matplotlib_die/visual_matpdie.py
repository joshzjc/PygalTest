from matp_die import Matp_die
import matplotlib.pyplot as plt

matplotlib_die =Matp_die()


result = [matplotlib_die.matroll() for value in range(1,101)]
frequence = [result.count(num) for num in range(1,matplotlib_die.num_size+1)]

x_values = list(range(1,matplotlib_die.num_size+1))
y_values = frequence[:]
# plt.scatter(x_values,y_values,s=50,edgecolors='none',c=y_values,cmap=plt.cm.Blues)
plt.plot(x_values,y_values,linewidth = 5)
plt.title('Die Count',fontsize = 14)
plt.xlabel('Die number',fontsize = 10)
plt.ylabel('The number of times',fontsize = 10)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()