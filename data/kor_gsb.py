import matplotlib.pyplot as plt
import numpy as np

medal = np.array(["Gold", "Silver", "Bronze"])
account = np.array([51, 26, 10])

plt.bar(medal, account, color="#CE5A4A", linewidth="2.0")
plt.ylabel('Account')
plt.xlabel('Medal Types')
plt.title('Medal types', pad=20)
plt.show()