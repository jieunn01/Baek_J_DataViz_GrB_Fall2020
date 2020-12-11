import matplotlib.pyplot as plt

values = [42, 45]
labels = ["Men", "Women"]
colors = ["#F9C9C2", "#FF7F6E"]

explode = (0,0.2)

plt.pie(values, labels=labels, colors=colors, explode = explode,  startangle=90, shadow = True, autopct='%.1f%%')

plt.title("Gender ratio", pad=10)
plt.show()
