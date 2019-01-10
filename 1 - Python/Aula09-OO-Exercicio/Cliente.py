class Cliente:

    def __init__(self, nome, cpf, idade):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade

    # Metodo chamado ao printar o cliente (print(cliente)) - similar ao toString do Java
    def __str__(self):
        return "Nome: " + self.nome + "\nCPF: " + self.cpf + "\nIdade: " + str(self.idade)