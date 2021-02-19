p = 0.40  # proporção da fase gasosa desejada
R = 1.0  # raio da bolsa plastica
L = 5.97  # comprimento do biodigestor
import numpy as np
P = 2.0*np.pi*R
A = 0.621*p**2 - 0.042*p + 0.352
#print(0.231*45.0, "volume util")
#print(2.0*np.pi*R, "perimetro total transversal")

#print((((2.033+1.184)*1.126)/2.0)*6.645)

#print((-1*A/3 + 1/3)*P)
#print(0.951*(-1*A/3 + 1/3)*P)
print(2*1.8453 + 2*4.6662 + 3.2981, "area da fossa") # area da fossa
print(2.0*np.pi*R**2 + 2.0*np.pi*R*5.59, "area total") # area tottal
print((2.0*np.pi*R**2 + 2.0*np.pi*R*5.59)-(2*1.8453 + 2*4.6662 + 3.2981), "Area do gasometro") # area do gasometro