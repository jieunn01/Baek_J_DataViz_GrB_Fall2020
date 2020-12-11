import matplotlib.pyplot as plt
import numpy as np

sports = np.array(["Skating", "Skiing", "Biathlon", "Curling", "Ice Hockey"])
account = np.array([83, 297, 62, 15, 0])

plt.bar(sports, account, color="#7FBCC6", linewidth="2.0")
plt.ylabel('Account')
plt.xlabel('Sports Types')
plt.title('Norway with sports types', pad=20)
plt.show()