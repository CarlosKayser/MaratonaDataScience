print("Hello World")
print("Segundo print!")
print("Pulando de linha\nNova linha")
print("Tabulação de linha!\tLinha tabulada")

# Variaveis sempre com letras iniciais minusculas

nome = 'Carlos'
idade = 20
altura = 1.85 # Não usar vírgula

print(nome) # Printar o conteúdo da variavel nome
print(idade) # Printar o conteúdo da variavel idade
print(altura)

tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)

print(tipo_nome) # Printar o tipo da variavel
print(tipo_idade) # Printar o tipo da variavel
print(tipo_altura) # Printar o tipo da variavel

# Concatenar valores em python
print(nome, "tem", idade , "anos e", altura , "de altura!")
# Concatenar valores com +
print(nome + " tem " + str(idade) + " anos e " + str(altura) + " de altura!")

# Calculos
resultado = 10 ** 2 # 10^2

print(resultado)