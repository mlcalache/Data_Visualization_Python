import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

chart_title = "Scatterplot chart"
x_label = "X axis"
y_label = "Y axis"

plt.title(chart_title)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.scatter(x, y, label="My points", color="r")  # r = red
plt.plot(x, y)
plt.legend()
plt.show()
