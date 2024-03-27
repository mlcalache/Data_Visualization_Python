import matplotlib.pyplot as plt
import pandas as pd

chart_title = "Brazilian Population 1980-2016"
x_label = "Years"
y_label = "Population (x100.000.000)"

plt.rcParams["figure.figsize"] = [10.00, 5.00]
plt.rcParams["figure.autolayout"] = True
columns = ["year", "population"]
data = pd.read_csv("brazilian_population.csv", usecols=columns, sep=';')
print("Contents in csv file:", data)

fig, ax = plt.subplots()

plt.plot(data.year, data.population, color="r")
plt.bar(data.year, data.population, color="#999999")

plt.title(chart_title)
plt.xlabel(x_label)
plt.ylabel(y_label)

ax.grid(axis='y')

plt.show()
