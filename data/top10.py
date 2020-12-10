import matplotlib.pyplot as plt
import numpy as np

countries = np.array(['RUS', 'AUT', 'SUI', 'GER', 'SWE', 'FIN', 'URS', 'NOR', 'CAN', 'USA'])
account = np.array([263, 280, 285, 360, 433, 434, 440, 457, 625, 653 ])

plt.barh(countries, account, color=(0/255, 100/255, 100/255), linewidth = 0.2)
plt.ylabel("Countries")
plt.xlabel("Medal Account")
plt.show()