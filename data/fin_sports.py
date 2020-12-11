import matplotlib.pyplot as plt
import numpy as np

sports = np.array(["Skating", "Skiing", "Biathlon", "Curling", "Ice Hockey"])
account = np.array([26, 206, 16, 5, 181])

plt.bar(sports, account, color="#0E4C56", linewidth="2.0")
plt.ylabel('Account')
plt.xlabel('Sports Types')
plt.title('Finland with sports types', pad=20)
plt.show()