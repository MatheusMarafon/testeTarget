
# Função que confere se o número pertence ou não
def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n or n == 0:
        return f"O número {n} pertence a sequencia de Fibonacci."
    else:
        return f"O número {n} não pertence a sequência de Fibonacci."


# Introdução do número
numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))
