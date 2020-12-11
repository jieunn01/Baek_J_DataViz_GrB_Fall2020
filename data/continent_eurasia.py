import matplotlib.pyplot as plt

values = [440, 263]
labels = ["Soviet Union", "Russia"]
colors = ['#EAE38C','#CEC87E']

explode = [0.1, 0.1]

plt.pie(values, labels=labels, colors=colors, explode = explode,  startangle=90, autopct='%.1f%%' )
plt.title("EURASIA", pad=10)
# generate the chart
plt.show()