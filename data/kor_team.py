import matplotlib.pyplot as plt
import numpy as np

types = np.array(["Team", "Individual"])
account = np.array([44, 43])

plt.barh(types, account, color="#DB9F93", linewidth="2.0")

plt.ylabel("Types of event")
plt.xlabel("Total Account")
plt.title("Team event vs Individual event", pad=20)
plt.show()