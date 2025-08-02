import numpy as np
import matplotlib.pyplot as plt
print("*"*10, "Função", "*"*10)
print("**"," "*22,"**")

def equacao2(x):

    return 6* x ** 2 + 4 * x -6

x = np.linspace(-10, 10, 500)

y = equacao2(x)

for yLine in y:
    print(yLine)

plt.plot(x,y)
plt.show()



