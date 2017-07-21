import Bases  # Importamos la libreria

print("Base32 6I es: " + str(Bases.convertirbaseadecimal("6I", 32)))  # La funcion recibe un string y regresa un entero decimal

print("124 en Octal: " + Bases.convertirdecimalabase(124, 8))  # La funcion recibe un entero decimal y devuelve un string convertido a nueva base

print("174 octal a Decimal: " + str(Bases.convertirbaseadecimal("174", 8)))