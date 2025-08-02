import numpy as np

vetA = np.array([3,1])
vetB = np.array([2,3])
a = -3
#Norma Vetorial
print("1) ||vetA|| ",np.linalg.norm(vetA))

#Produto Escalar
print("2) || avetA|| = ", np.linalg.norm(a * vetA))

print(f"3) {np.linalg.norm(vetA + vetB)} <= {(np.linalg.norm(vetA) + np.linalg.norm(vetB))}")

vetC = np.array(0)
print(f"4) {np.linalg.norm(vetC)} = 0 quando vetC = {vetC}")

#Produto Interno

print(f"Produto Interno: {np.dot(vetA, vetB)}")

#Condição Ortogonal

vetA = np.array([2,1])
vetB = np.array([-1,2])

print(f"Condição Ortogonal quando A + B = 0 : {np.dot(vetA, vetB)}")
