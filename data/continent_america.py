import matplotlib.pyplot as plt

values = [653, 625]
labels = ["United States", "Canada"]
colors = ["#98B0E2", "#687EAA"]

explode = [0.1, 0.1]

plt.pie(values, labels=labels, colors=colors, explode = explode,  startangle=90, autopct='%.1f%%' )

plt.title("AMERICA", pad=10)
# generate the chart
plt.show()