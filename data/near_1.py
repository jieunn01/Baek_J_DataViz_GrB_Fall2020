import matplotlib.pyplot as plt
import numpy as np

types = np.array(["Kazakhstan", "Uzebekistan"])
account = np.array([7, 1])

plt.bar(types, account, color="#B0CC97", linewidth="3.0")

plt.ylabel("Total Account")
plt.xlabel("Countries")
plt.title("Kazakhstan vs Uzebekistan total medal", pad=20)
plt.show()