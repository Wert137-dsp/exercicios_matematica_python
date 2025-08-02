import matplotlib.pyplot as plt
import numpy as np
coord1 = input("Digite a 1º coordenada: ").split(",")
coord2 = input("Digite a 2º coordenada: ").split(",")

# x1 = abs(float(x1))
# x2 = abs(float(x2))
# y1 = abs(float(y1))
# y2 = abs(float(y2))

# distancia = (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** 0.5

# print(distancia)

for i in range(len(coord1)):

    coord1[i] = float(coord1[i])
    coord2[i] = float(coord2[i])


A = np.array(coord1)
B = np.array(coord2)

dist = np.linalg.norm(B - A)

plt.scatter(*A, color = "blue", label = "Coordenada1")
plt.scatter(*B, color = "blue", label = "Coordenada2")


plt.plot([A[0], B[0]], [A[1], B[1]], label = f"Distancia {dist}")
plt.plot([A[1], B[1]], label = f"Distancia {dist}")


plt.grid(True)
plt.axis('equal')
plt.legend()

plt.show()
