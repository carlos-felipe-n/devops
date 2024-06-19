from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir(self):
        print(self.nome, self.email, self.idade)

felipe = Cliente(nome='Felipe', email='teste@teste', idade=32)

print(felipe.exibir())
