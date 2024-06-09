import math

x1, y1 = input().split()
x2, y2 = input().split()

distancia = math.sqrt(((float(x2) - float(x1)) * (float(x2) - float(x1)))
                      + ((float(y2) - float(y1)) * (float(y2) - float(y1))))

print("%.4f" % distancia)


# Outra maneira de escrever o código:

x1, y1 = input().split()
x2, y2 = input().split()

distancia = (((float(x2) - float(x1)) ** 2)
             + ((float(y2) - float(y1)) ** 2)) ** (1/2)

print("%.4f" % distancia)
