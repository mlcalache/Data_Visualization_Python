import matplotlib.pyplot as plt

x = [1, 2, 5, 10, 15]
y = [2, 3, 4, 5, 6]

plt.title("My first chart with Python")

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.plot(x, y)
plt.show()
