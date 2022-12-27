import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = (0, 60, 180, 300, 600, 720)
y = (578, 411, 174, 125, 52, 50)

plt.title('Изменение массы ракеты')
plt.xlabel('Время, с')
plt.ylabel('Масса, тонны')

ax.plot(x, y, color='green', linestyle='-', marker='o')
plt.show()