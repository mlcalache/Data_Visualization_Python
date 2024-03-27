import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
size = [20, 5, 200, 33, 10]

chart_title = "Scatterplot chart"
x_label = "X axis"
y_label = "Y axis"

plt.title(chart_title)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.scatter(x, y, label="My points", color="m", marker="s", s=size)
plt.plot(x, y, linestyle="dashed", color="#FF9999")
plt.legend()
plt.savefig("Figure1.png")
plt.savefig("Figure1.pdf")
plt.savefig("Figure2.png", dpi=300)
plt.savefig("Figure3.png", dpi=1200)
