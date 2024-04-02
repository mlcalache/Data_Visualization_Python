import matplotlib.pyplot as plt
import random

array = []

for i in range(10):
    random_number = random.randint(0, 100000)
    array.append(random_number)

array.append(100)  # to add an outlier, as all other numbers are between 0 and 50

plt.boxplot(array)
plt.title("Boxplot")
plt.show()
