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

# plt.plot(x, y, linestyle="dashed")
# plt.scatter(x, y, label="My points", color="m", marker="s", s=100)
plt.scatter(x, y, label="My points", color="m", marker="s", s=size)
# plt.plot(x, y, 'go--', linewidth=2, markersize=12)
# plt.plot(x, y, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.plot(x, y, linestyle="dashed", color="#FF9999")
plt.legend()
plt.show()

# Official documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# Markers
# '.' point marker
# ',' pixel marker
# 'o' circle marker
# 'v' triangle_down marker
# '^' triangle_up marker
# '<' triangle_left marker
# '>' triangle_right marker
# '1' tri_down marker
# '2' tri_up marker
# '3' tri_left marker
# '4' tri_right marker
# '8' octagon marker
# 's' square marker
# 'p' pentagon marker
# 'P' plus (filled) marker
# '*' star marker
# 'h' hexagon1 marker
# 'H' hexagon2 marker
# '+' plus marker
# 'x' x marker
# 'X' x (filled) marker
# 'D' diamond marker
# 'd' thin_diamond marker
# '|' vline marker
# '_' hline marker

# Line Styles
# '-' solid line style
# '--' dashed line style
# '-.' dash-dot line style
# ':' dotted line style

# Colors
# 'b' blue
# 'g' green
# 'r' red
# 'c' cyan
# 'm' magenta
# 'y' yellow
# 'k' black
# 'w' white
