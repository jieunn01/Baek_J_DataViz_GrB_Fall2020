import matplotlib.pyplot as plt


labels = ['USA', 'CAN', 'NOR']
men = [410, 286, 359]
women= [243, 239, 98]
width = [0.35]     


plt.bar(labels, men, width=width, label='Men', color="#738EA8")
plt.bar(labels, women, width=width,  bottom=men, label='Women', color="#A6BDD1")

plt.ylabel('Medal Account')
plt.xlabel('Countries')
plt.title('GENDER RATIO', pad=20)
plt.legend()

plt.show()