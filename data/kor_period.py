import matplotlib.pyplot as plt

years = [1992, 1994, 1998, 2002, 2006, 2010, 2014]

awards = [7,10,12,7,19,18,14]

plt.plot(years, awards, color="#A33D2F", linewidth=3.0)

# add some labels
plt.ylabel("Awards")
plt.xlabel("Years")
plt.title("Period records", pad=20)

plt.show()

