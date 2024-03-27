import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

chart_title = "My bar chart"
x_caption = "X axis"
y_caption = "Y axis"

plt.title(chart_title)
plt.xlabel(x_caption)
plt.ylabel(y_caption)

plt.bar(x, y)
plt.show()
