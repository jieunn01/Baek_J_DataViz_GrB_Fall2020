import matplotlib.pyplot as plt
import numpy as np

sports = np.array(["Skating", "Skiing", "Biathlon", "Curling", "Ice Hockey"])
account = np.array([20, 146, 16, 33, 218])

plt.bar(sports, account, color="#5DAF86", linewidth="2.0")
plt.ylabel('Account')
plt.xlabel('Sports Types')
plt.title('Sweden with sports types', pad=20)
plt.show()