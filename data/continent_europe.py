import matplotlib.pyplot as plt

values = [457, 280, 285, 433, 360, 434]
labels = ["Norway", "Austria", "Switzerland", "Sweden", "Germany", "Finland"]
colors = ['#992B89','#A54C99', "#BA65AE", "#D388C8", "#EAACE1", "#FCCDF5"]

explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

plt.pie(values, labels=labels, colors=colors, explode = explode,  startangle=90, autopct='%.1f%%' )
plt.title("EUROPE", pad=10)
# generate the chart
plt.show()