import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):
    def especial(self, inimigo):
        dano = 30
        inimigo.vida -= dano
        print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome} e Causa {dano} de Dano!")

class Mago(Personagem):
    def especial(self):
        cura = 25
        self.vida += cura
        print(f"{self.nome} usa Cura e Ganha {cura} Pontos de Vida!")

class Arqueiro(Personagem):
    def especial(self, inimigos):
        dano = 15
        for inimigo in inimigos:
            inimigo.vida -= dano
            
        print(f"{self.nome} usa Chuva de Flechas e Causa {dano} de Dano a Todos os Inimigos!")

def importar_personagens(caminho):
    """
        Função que importa personagens a partir de um ficheiro JSON.
        O ficheiro contém uma lista de personagens com informações de nome, vida, ataque e classe.
        - caminho: Caminho para o ficheiro JSON que contém os dados dos personagens.
        Retorna:
        - lista de personagens.
        - quantidade total de personagens importados.
    """
    with open(caminho, 'r') as file:
        dados = json.load(file)

    personagens = []
    for dado in dados:
        if dado['classe'] == 'Guerreiro':
            personagens.append(Guerreiro(dado['nome'], dado['vida'], dado['ataque']))
        elif dado['classe'] == 'Mago':
            personagens.append(Mago(dado['nome'], dado['vida'], dado['ataque']))
        elif dado['classe'] == 'Arqueiro':
            personagens.append(Arqueiro(dado['nome'], dado['vida'], dado['ataque']))

    return personagens, len(personagens)

def ordenar_personagens_por_vida(personagens):
    """
        Função que ordena a lista de personagens de acordo com os pontos de vida (do menor para o maior).
        - personagens: Lista de personagens.
        Retorna:
        - lista de personagens ordenada por vida.
    """
    return sorted(personagens, key=lambda p: p.vida)

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[2]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])