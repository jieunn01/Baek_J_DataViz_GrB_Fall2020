import matplotlib.pyplot as plt
import numpy as np

countries = np.array(['GER', 'DEN', 'BEL', 'POL'])
account = np.array([360, 5, 13, 27])

plt.barh(countries, account, color="#5B7A4B", linewidth = 0.2)
plt.ylabel("Countries")
plt.xlabel("Medal Account")
plt.show()