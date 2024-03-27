import matplotlib.pyplot as plt

data = open("brazilian_population.csv").readlines()

x = []
y = []

for i in range(len(data)):
    if i != 0:
        line = data[i].split(";")
        x.append(int(line[0]))
        y.append(int(line[1]))

print(x)
print(y)

chart_title = "Brazilian Population 1980-2016"
x_label = "Years"
y_label = "Population"

plt.title(chart_title)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.plot(x, y)
plt.show()
