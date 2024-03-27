import pandas as pd
import matplotlib.pyplot as plt

chart_title = "TTT"
x_label = "XXX"
y_label = "YYY"

# create DataFrame
df = pd.DataFrame({'team': ['Mavs', 'Nets', 'Spurs', 'Warriors'],
                   'points': [105, 99, 112, 100]})

# define plot
fig, ax = plt.subplots()

# create bar plot
df.plot(kind='bar', ax=ax)

# add horizontal gridlines
ax.grid(axis='y')

plt.title(chart_title)
plt.xlabel(x_label)
plt.ylabel(y_label)

# display plot
plt.show()
