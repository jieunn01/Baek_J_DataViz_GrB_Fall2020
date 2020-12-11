import numpy as np
import matplotlib.pyplot as plt

n = 3
gold= (167, 315, 159)
silver= (319, 203, 171)
bronze = (167,107,127)
fig, ax = plt.subplots()
index = np.arange(n)
bar_width = 0.3
ax.bar(index, gold, bar_width, color='#C49C48',label='Gold')
ax.bar(index+bar_width, silver, bar_width, color='#C0C0C0',label='Silver')
ax.bar(index+2*bar_width, bronze, bar_width, color='#A97142', label='Bronze')
ax.set_xlabel('Countries')
ax.set_ylabel('Medal Account')
ax.set_title('MEDAL TYPES', pad=20)
ax.set_xticks(index + bar_width)
ax.set_xticklabels(('USA','CAN','NOR'))
ax.legend()
plt.show()