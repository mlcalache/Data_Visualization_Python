import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

chart_title = "My bar chart comparison"
x_caption = "X axis"
y_caption = "Y axis"

plt.title(chart_title)
plt.xlabel(x_caption)
plt.ylabel(y_caption)

plt.bar(x1, y1, label="Group of Evens")
plt.bar(x2, y2, label="Group of Odds")
plt.legend()
plt.show()
