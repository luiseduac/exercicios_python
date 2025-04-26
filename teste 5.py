n = input('Digite um valor:')

try:
    n = int(n)  # Tenta converter a entrada para um número inteiro
    print(n, "é um número")
except ValueError:
    print(n, "não é número")