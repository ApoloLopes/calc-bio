import numpy as np

p = 0.40  # proporção da fase gasosa desejada
R = 1.0  # raio da bolsa plastica
L = 5.59  # comprimento do biodigestor

cd = 0.2168 #[m³/dia]
trh = 45.0                 #[dia^-1]

bio_vol = cd*trh
per_trans = 2.0*np.pi*R
A = 0.621*p**2.0 - 0.042*p + 0.352
b = (-1*A/3 + 1/3)*per_trans
a = 1.618*b
h = 0.951*b
a_calc = ((b + a)*h)/2.0
Af = 0.4755*(a + b)*b
At = Af / (1 - p)
Ag = At - Af
Vt = At*L
Vf = Af*L
Vg = Ag*L

print("volume util do biodigestor", bio_vol)
print("perimetro transversal", per_trans)
print("porcentagem do perimetro transvelsal", A)
print("base menor do biodigestor", b)
print("base maior do biodigestor", a)
print("profundidade do biodigestor", h)
print("Area transversal liquida da fossa ", Af)
print("Area total transversal", At)
print("Area transversal destinada ao gás", Ag)
print("comprimento do biodigestor", bio_vol / Af)


