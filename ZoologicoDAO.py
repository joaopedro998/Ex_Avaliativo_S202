import numpy as np
import Habitat
import Animal

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Escolha uma opçao: ")
            if command == "0":
                print("Voce saiu !!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Esse codigo nao existe, tente novamente.")


class ZoologicoCLI(SimpleCLI):
    def __init__(self, animal_model):
        super().__init__()
        self.animal_model = animal_model
        self.add_command("1", self.criar_animal)
        self.add_command("2", self.ler_animal)
        self.add_command("3", self.atualizar_animal)
        self.add_command("4", self.deletar_animal)

    def criar_animal(self):
        nomeanimal = input("Entre com o nome do animal: ")
        especie = input("Entre com a especie do animal: ")
        idade = int(input("Entre com a idade do animal: "))
        id = int(input('Entre com o id do Habitat: '))
        nome = input('Entre com o nome do Habitat: ')
        tipoAmbiente = input('Entre com o tipo de ambiente do habitat: ')
        idCuidador = int(input('Entre com o id do cuidador: '))
        nomeCuidador = input('Entre com o nome do cuidador: ')
        documento = input('Entre com o documento: ')

        habitat = [
            {
            "id" : id,
            "nome": nome,
            "tipoAmbiente": tipoAmbiente,

            "cuidador": [{
                "id": idCuidador,
                "nome": nomeCuidador,
                "documento": documento
            }]
            }
        ]

        self.animal_model.criar_animal(nomeanimal, especie, idade, habitat)

    def ler_animal(self):
        id = input("Entre com o id: ")
        animal = self.animal_model.read_animal_by_id(id)
        if animal:
            print(f"Nome: {animal['nome']}")
            print(f"especie: {animal['especie']}")
            print(f"idade: {animal['idade']}")
            print(f"habitat: {animal['habitat']}")

    def atualizar_animal(self):
        id = input("Entre com o id : ")
        nome = input("Entre com o novo nome: ")
        especie = input("Enter com a nova especie: ")
        idade = int(input("Entre com a idade nova: "))
        habitat = input("Entre com o novo habitat: ")
        self.animal_model.atualizar_animal(id, nome, especie, idade, habitat)

    def deletar_animal(self):
        id = input("Enter the id: ")
        self.animal_model.deletar_animal(id)

    def run(self):
        print("Bem vindo ao Zoologico")
        print("Escolha uma das opcoes")
        print("1-Adicionar novo animal")
        print("2-Ver animal existente")
        print("3-Atualizar animal")
        print("4-Excluir Animal")
        print("0-Sair")
        super().run()