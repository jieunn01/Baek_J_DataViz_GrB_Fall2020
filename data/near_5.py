import matplotlib.pyplot as plt

values = [63, 87, 82]
labels = ["Japan", "Korea", "China"]
colors = ['#FFF9D9','#E8D782', "#E2C744"]

plt.pie(values, labels=labels, colors=colors, startangle=90, autopct='%.1f%%' )
plt.title("Total medal counting proportion", pad=10)

plt.legend(ncol=3)
plt.show()