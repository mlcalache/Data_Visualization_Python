import matplotlib.pyplot as plt
import pandas as pd

chart_title = "Brazilian Population"
x_label = "Years"
y_label = "Population"

plt.title(chart_title)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.rcParams["figure.figsize"] = [10.00, 5.00]
plt.rcParams["figure.autolayout"] = True
columns = ["year", "population"]
df = pd.read_csv("brazilian_population.csv", usecols=columns, sep=';')
print("Contents in csv file:", df)
plt.plot(df.year, df.population)
plt.bar(df.year, df.population, color="r")
plt.show()
