from random import randint

class Jogador():
    def __init__(self, 
                 nome, idade, altura, fisico,
                 posicao, velocidade, agilidade, hab_gol,
                 hab_defesa, hab_armacao, hab_ataque,
                 nervosismo, respeito, momento):
        self.nome = nome 
        self.idade = idade
        self.altura = altura
        self.fisico = fisico
        self.posicao = posicao
        self.velocidade = velocidade
        self.agilidade = agilidade
        self.hab_gol = hab_gol
        self.hab_defesa = hab_defesa
        self.hab_armacao = hab_armacao
        self.hab_ataque = hab_ataque
        self.nervosismo = nervosismo
        self.respeito = respeito
        self.momento = momento

    # essas funcoes retornam os valores em string

    def __str__(self): 
        return "{}@{}@{}@{}@{}@{}@{}@{}@{}@{}@{}@{}@{}@{}".format(
            self.nome, self.idade, self.altura, self.fisico, self.posicao,
            self.velocidade, self.agilidade, self.hab_gol, self.hab_defesa,
            self.hab_armacao, self.hab_ataque, self.nervosismo, self.respeito, self.momento)

        
class Treinador():
    def __init__(self, nome, idade,
                 hab_social, hab_tatica, temperamento):
        self.nome = nome
        self.idade = idade
        self.hab_social = hab_social
        self.hab_tatica = hab_tatica
        self.temperamento = temperamento

    def __str__(self): 
        return "{}@{}@{}@{}@{}@".format(
            self.nome, self.idade, self.hab_social, self.hab_tatica, self.temperamento)

class Time():
    def __init__(self, nome, pais, confederacao,
                 reputacao, momento, tecnico,
                 jogadores):
        self.nome = nome
        self.pais = pais
        self.confederacao = confederacao
        self.reputacao = reputacao
        self.momento = momento
        self.tecnico = tecnico
        self.jogadores = jogadores

    def __str__(self): 
        return "{}@{}@{}@{}@{}@{}@{}@".format(
            self.nome, self.pais, self.confederacao, self.reputacao, 
            self.momento, self.tecnico, self.jogadores)

# gerador de time aleatório
def time_aleatorio():
    # listas    
    lista_jog = [] # preciso criar uma lista vazia antes do for dos jogadores
    nomes_jog = ["Gustavo", "Luan", "Rafael", "Victor", "Marcelo",
                 "Dani", "Alves", "Santos", "Pedro", "Gabriel",
                 "Ricardo", "Oliveira", "Weverton", "Ederson", "Alisson",
                 "Marcos", "Rocha", "Léo", "Adriano", "Ronaldo", "Gerson",
                 "Alex", "Alexandre", "Clemente", "Rodriguez", "Gatito", 
                 "Fernandes", "Fernando", "Diogo", "Diego", "Filipe", "Luis",
                 "Matheus", "Cunha", "Mateus", "Romário", "Roberto"]
    nomes_tec = ["Abel", "Ferreira", "Vitor", "Pereira", "Jorge", "Jesus",
                 "Dorival", "Júnior", "Rogério", "Menezes", "Adenor",
                 "Santana", "Mario"]
    nomes_time = ["SE Coqueiros", "Nacional - RS", "Carioca FC", "CR Flamingo"]
    posicoes = ["Goleiro", "Zagueiro", "Lateral Esquerdo",
                "Lateral Direito", "Volante", "Meia",
                "Atacante", "Centroavante"]

    # loop dos jogadores
    for i in range (0, 22):
        posicoes_loop = ["Goleiro", "Goleiro", "Goleiro",
                         "Lateral Esquerdo", "Lateral Esquerdo",
                         "Zagueiro", "Zagueiro", "Zagueiro", "Zagueiro",
                         "Lateral Direito", "Lateral Direito",
                         "Volante", "Volante",
                         "Meia", "Meia", "Meia",
                         "Atacante", "Atacante", "Atacante", "Atacante",
                         "Centroavante", "Centroavante"]
        atributos = [nomes_jog[randint(0, len(nomes_jog) - 1)],
                     randint(18 - randint(-3, 3), 40 - randint(-3, 3)),
                     randint(160 - randint(-10, 10), 190 - randint(-10, 10)),
                     randint(1, 99),
                     posicoes_loop[i],
                     randint(1, 99),
                     randint(1, 99),
                     randint(1, 99),
                     randint(1, 99),
                     randint(1, 99),
                     randint(1, 99),
                     randint(1, 99),
                     randint(1, 99),
                     randint(1, 99)
                    ]
        jog = Jogador(*atributos)
        lista_jog.append(jog)

        i += 1

    # treinador
    atributos = [nomes_tec[randint(0, len(nomes_tec) - 1)],
                 randint(30, 75),
                 randint(1, 99),
                 randint(1, 99),
                 randint(1, 99)]
    tec = Treinador(*atributos)

    # time

    atributos = [nomes_time[randint(0, len(nomes_time) - 1)],
                 "Brasil",
                 "CONMEBOL",
                 randint(0, 99),
                 randint(0, 99),
                 tec,
                 lista_jog
                ]
                
    tim = Time(*atributos)

    return tim

# zona de testes
if __name__ == '__main__':
    time_teste = time_aleatorio()
    print("O nome do time é", time_teste)
    print(time_teste.nome)
    print("País:")
    print(time_teste.pais)
    print("Confederação:")
    print(time_teste.confederacao)
    print("Reputação (1 a 99)")
    print(time_teste.reputacao)
    print("Momento (1 a 99)")
    print(time_teste.momento)
    print("Técnico:")
    texto = """
            Nome: {}
            Idade:{} 
            Habilidade Social: {}
            Habilidade Tática: {}
            Temperamento: {}
            """.format(str(time_teste.tecnico).split('@')[0],
                       str(time_teste.tecnico).split('@')[1],
                       str(time_teste.tecnico).split('@')[2],
                       str(time_teste.tecnico).split('@')[3],
                       str(time_teste.tecnico).split('@')[4])
    print(texto)
    print(str(time_teste.tecnico).split('@'))
    print("Elenco:")
    for i in range(0, len(time_teste.jogadores)):
        jogador = str(time_teste.jogadores[i])
#        print(type(jogador))
#        print(jogador.split('@'))
        texto = """
                Nome: {}
                Idade:{} 
                Altura (cm): {}
                Físico: {}
                Posição: {}
                Velocidade:{}
                Agilidade: {}
                Habilidade no gol: {}
                Habilidade na defesa: {}
                Habilidade no ataque: {}
                Nervosismo: {}
                Respeito: {}
                Momento:{}
                """.format(jogador.split('@')[0],
                        jogador.split('@')[1],
                        jogador.split('@')[2],
                        jogador.split('@')[3],
                        jogador.split('@')[4],
                        jogador.split('@')[5],
                        jogador.split('@')[6],
                        jogador.split('@')[7],
                        jogador.split('@')[8],
                        jogador.split('@')[9],
                        jogador.split('@')[10],
                        jogador.split('@')[11],
                        jogador.split('@')[12])
        print(texto)

# obs: parece que a função __str__ dentro da classe Time precisa apenas
# existir para retornar os prints corretamente. Não faço ideia de como está
# funcionando