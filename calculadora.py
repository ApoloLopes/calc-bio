p = 0.40  # proporção da fase gasosa desejada
R = 1.0  # raio da bolsa plastica
L = 6.645  # comprimento do biodigestor
import numpy as np
P = 2.0*np.pi*R
A = 0.621*p**2 - 0.042*p + 0.352
#print(0.231*45.0, "volume util")
#print(2.0*np.pi*R, "perimetro total transversal")

#print((((2.033+1.184)*1.126)/2.0)*6.645)

#print((-1*A/3 + 1/3)*P)
#print(0.951*(-1*A/3 + 1/3)*P)
print(2*1.8538 + 2*4.9716 + 3.5105)
print(2.0*np.pi*R**2 + 2.0*np.pi*R*5.95)
print((2.0*np.pi*R**2 + 2.0*np.pi*R*5.95)-(2*1.8538 + 2*4.9716 + 3.5105))