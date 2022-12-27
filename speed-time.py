import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = (60, 120, 180, 240, 300, 360)
y = (210, 842, 1573, 1978, 2644, 2712)

plt.title('Зависимость скорости от времени до орбиты Земли')
plt.xlabel('Время, с')
plt.ylabel('Скорость, м/c')

ax.plot(x, y, color='blue', linestyle='-', marker='o')
plt.show()
