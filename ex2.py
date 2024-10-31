# Função que verifica quantas vezes a letra aparece na palavra
def contar_letra(texto, letra):
    contagem = texto.lower().count(letra.lower())
    return f"A letra '{letra}' ocorre {contagem} vez na string digitada."


# Introdução dos dados
texto = input("Informe uma string: ")
letra = input("Informe a letra na qual será verificada: ")
print(contar_letra(texto, letra))
