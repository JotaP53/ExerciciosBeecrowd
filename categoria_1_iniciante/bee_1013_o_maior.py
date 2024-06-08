a, b, c = input().split()

maiorAB = (int(a) + int(b) + abs(int(a) - int(b))) / 2
maiorABC = (maiorAB + int(c) + abs(maiorAB - int(c))) / 2

print(int(maiorABC),"eh o maior")

### Outra maneira de responder:

a, b, c = input().split()

# Eu sou noob e meu amigo Anewton me deu essa dica de colocar a função 'max()' para não precisar fazer toda a fórmula.
maiorABC = max(int(a), int(b), int(c))

print(int(maiorABC),"eh o maior")