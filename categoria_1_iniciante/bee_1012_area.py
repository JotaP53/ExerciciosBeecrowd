A, B, C = input().split()
pi = 3.14159

# Área do Triângulo Retângulo
# Fórmula: (A * C) / 2

TRIANGULO = (float(A) * float(C)) / 2

# Área do Círculo
# Fórmula: pi * C * C

CIRCULO = pi * float(C) * float(C)

# Área do Trapézio
# Fórmula: (A + B) * C / 2

TRAPEZIO = (float(A) + float(B)) * float(C) / 2

# Área do Quadrado
# Fórmula: B ** 2

QUADRADO = float(B) ** 2

# Área do Retângulo
# Fórmula: A * B

RETANGULO = float(A) * float(B)

print("TRIANGULO: %.3f" % TRIANGULO)
print("CIRCULO: %.3f" % CIRCULO)
print("TRAPEZIO: %.3f" % TRAPEZIO)
print("QUADRADO: %.3f" % QUADRADO)
print("RETANGULO: %.3f" % RETANGULO)