"""
Números naturais : Inteiros e maior que 0
Inteiros: negativos e positivos
racionais - fracionarios
irracionais: não fracionarios
"""

from fractions import Fraction
import math
num = 3 ** 0.5

ehUmNumero = ""
if (num % 1 == 0):
    
    if(int(num) >= 0):

        ehUmNumero = "Natural"
    else:
        ehUmNumero = "Inteiro"

else:

    frac = Fraction(num).limit_denominator(10 ** 3)
    denominador = frac.denominator
    numerador = frac.numerator
    res = numerador / denominador

    if (math.isclose(res, num, rel_tol=1e-9)):
        ehUmNumero = "Racional"
    else:
        ehUmNumero = "Irracional"
    print(numerador)
   
print(f"{num} é um número {ehUmNumero}")

