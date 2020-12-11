import matplotlib.pyplot as plt

values = [192, 2, 152]
labels = ["Italy", "Spain", "France"]
colors = ['#B0DD80','#8AF40F', "#6A8251"]

plt.pie(values, labels=labels, colors=colors, startangle=90, autopct='%.1f%%' )
plt.title("Total medal counting proportion", pad=10)

plt.legend(ncol=3)
plt.show()