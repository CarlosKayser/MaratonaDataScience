"""
- Aula 10 - Entrada e saída de arquivos

"""

# Caso necessário use // para dividir os diretórios
#open('arquivo.txt', '') # argumento 1 é o arquivo
                         # argumento 2 é o modo de abertura
                         # Modo w ou a é escrita
                         # Modo r é de leitura
                         # Modo r+ é de leitura e escrita
                         # Modo binário use b 

arquivo = open('arquivo.txt', 'r+')

type(print(arquivo))
print(arquivo)
print("")

for i in range(0, 1000):
    # .write() para escrever dentro do arquivo
    arquivo.write('Numero: '+str(i)+'\n')

#print(arquivo.read())

for linha in arquivo:
    print(linha)

# Fechando o arquivo
arquivo.close()