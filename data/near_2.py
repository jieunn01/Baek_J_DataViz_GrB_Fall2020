import numpy as np
import matplotlib.pyplot as plt

n = 3
gold= (159, 127, 66)
silver= (171, 129, 147)
bronze = (127,177,221)
fig, ax = plt.subplots()
index = np.arange(n)
bar_width = 0.3
ax.bar(index, gold, bar_width, color='#C49C48',label='Gold')
ax.bar(index+bar_width, silver, bar_width, color='#C0C0C0',label='Silver')
ax.bar(index+2*bar_width, bronze, bar_width, color='#A97142', label='Bronze')
ax.set_xlabel('Countries')
ax.set_ylabel('Medal Account')
ax.set_title('Medal colors with 3 nearby countries', pad=20)
ax.set_xticks(index + bar_width)
ax.set_xticklabels(('NOR','SWE','FIN'))
ax.legend(ncol=3)
plt.show()