import math

# Constantes
G = 6.6743e-11  # Constante gravitacional em metros cúbicos por quilograma segundo ao quadrado
Msol = 1.989e30  # Massa do Sol em quilogramas
Asol = 1.496e11  # Distância média da Terra ao Sol em metros
year = 365.25 * 24 * 3600  # Um ano em segundos

# Entrada de dados
a = float(input("Insira o semi-eixo maior da órbita (em UA): "))
P = float(input("Insira o período da órbita (em anos): "))

# Conversão de unidades
a = a * Asol  # Converter para metros
P = P * year  # Converter para segundos

# Cálculo da massa
M = ((4 * math.pi**2 * a**3) / (G * P**2)) / Msol

# Saída de dados
print("A massa estimada da estrela é de {:.2f} massas solares.".format(M))
