"""
Implementação de um agente Inteligente em Python.

Objetivo:
Implementar um agente inteligente simples que tomará decisões em um
ambiente simulado. O agente será capaz de navegar em um grid 2D para
encontrar um objetivo (como um tesouro) enquanto evita obstáculos.

Componentes:
:1. Classificação do Ambiente:
    - Crie um grid 2D, obstáculos e posição do objetivo.
    - Recebe as ações do agente, ajusta sua situação interna e envia a próxima percepção

:2. Agente de classe:
    - Tem a capacidade de se mover no grid e tomar decisões com base na maneira como percebe o ambiente.
    - Usando uma política de movimento simples, atualize seu estado interno e retorne sua próxima ação.

3o. Função de simulação:
    - Executa a simulação, permitindo que o agente interaja com o ambiente até descobrir o objetivo ou até completar o número máximo de passos.

Como usar:
1. Defina os parâmetros do ambiente (largura, altura, número de obstáculos e posição do objetivo).
2. Crie instâncias de Ambiente e agente.
3. Execute a simulação chamando a função simulate.

"""
import random
import time
import os

class Ambiente:
    def __init__(self, largura, altura, num_obstaculos, objetivo_final):
        
        #Inicializa o ambiente com o grid 2D, obstáculos e a posição do objetivo.
        
        self.largura = largura
        self.altura = altura
        # Cria uma matriz 2D para representar o grid, inicialmente vazio
        self.grid = [[' ' for _ in range(largura)] for _ in range(altura)]
        self.objetivo_final = objetivo_final
        self.agente_posicao = (0, 0)  # Posição inicial do agente
        
        # Colocar obstáculos no grid
        self.obstaculos = set()
        while len(self.obstaculos) < num_obstaculos:
            # Gera posições aleatórias para os obstáculos
            obstaculo_posicao = (random.randint(0, altura - 1), random.randint(0, largura - 1))
            # Garante que a posição do obstáculo não coincida com a do agente ou a do objetivo
            if obstaculo_posicao != self.agente_posicao and obstaculo_posicao != self.objetivo_final:
                self.obstaculos.add(obstaculo_posicao)
        
        # Marca os obstáculos no grid
        for obstaculo in self.obstaculos:
            self.grid[obstaculo[0]][obstaculo[1]] = 'X'
        
        # Define a posição do objetivo no grid
        self.grid[objetivo_final[0]][objetivo_final[1]] = 'G'
        # Define a posição inicial do agente no grid
        self.grid[self.agente_posicao[0]][self.agente_posicao[1]] = 'A'
    
    def display(self):
        """
        Exibe o grid no console.
        """
        for row in self.grid:
            print(' '.join(row))
        print()

    def update_agente_posicao(self, nova_posicao):
        #Atualiza a posição do agente no grid.

        # Limpa a posição antiga do agente
        self.grid[self.agente_posicao[0]][self.agente_posicao[1]] = ' '
        self.agente_posicao = nova_posicao
        # Define a nova posição do agente no grid
        self.grid[self.agente_posicao[0]][self.agente_posicao[1]] = 'A'
    
    def get_percepcao(self):
        """
        Retorna a percepção do ambiente pelo agente.

        :return: Tupla contendo a posição atual do agente, a posição do objetivo e o conjunto de obstáculos.
        """
        return self.agente_posicao, self.objetivo_final, self.obstaculos


class agente:
    def __init__(self, ambiente):
        
        #Inicializa o agente com o ambiente fornecido e define a posição inicial.

        self.ambiente = ambiente
        self.posicao = (0, 0)  # Posição inicial do agente
        self.historico = set()  # Histórico de posições visitadas
        self.historico.add(self.posicao)  # Adiciona a posição inicial ao histórico
    
    def select_action(self, percepcao):
        """
        Seleciona a próxima ação do agente com base na percepção do ambiente.

        :return: Nova posição do agente após a ação selecionada.
        """
        agente_posicao, objetivo_final, obstaculos = percepcao
        agente_x, agente_y = agente_posicao
        objetivo_x, objetivo_y = objetivo_final

        # Movimentos possíveis
        movimentos_possiveis = [
            (agente_x + 1, agente_y),  # Mover para baixo
            (agente_x - 1, agente_y),  # Mover para cima
            (agente_x, agente_y + 1),  # Mover para a direita
            (agente_x, agente_y - 1)   # Mover para a esquerda
        ]
        
        # Filtra movimentos que são dentro dos limites do grid e não colidem com obstáculos
        movimentos_validos = [move for move in movimentos_possiveis 
                       if (0 <= move[0] < self.ambiente.altura and 
                           0 <= move[1] < self.ambiente.largura and 
                           move not in obstaculos and 
                           move not in self.historico)]

        # Ordena os movimentos válidos por proximidade ao objetivo
        movimentos_validos.sort(key=lambda pos: abs(pos[0] - objetivo_x) + abs(pos[1] - objetivo_y))

        # Se houver movimentos válidos, retorna o que está mais próximo do objetivo
        if movimentos_validos:
            return movimentos_validos[0]
        
        # Se não houver movimentos válidos, tenta retornar a uma posição anterior
        if self.historico:
            return self.historico.pop()
        
        # Se não houver movimentos válidos e o histórico estiver vazio, permanece na posição atual
        return agente_posicao
    
    def update_state(self, nova_posicao):
        """
        Atualiza o estado interno do agente com a nova posição e adiciona a posição ao histórico.

        :param nova_posicao: Nova posição do agente.
        """
        self.historico.add(self.posicao)  # Adiciona a posição atual ao histórico
        self.posicao = nova_posicao





def simulate(ambiente, agente, max_passos=150):
    """
    Executa a simulação, permitindo que o agente interaja com o ambiente até encontrar o objetivo
    ou até que um número máximo de passos seja alcançado.
    """
    passos = 0  # Inicializa o contador de passos
    while passos < max_passos:
        # Limpa o console para exibir a nova posição do agente
        os.system('cls' if os.name == 'nt' else 'clear')
        # Obtém a percepção do ambiente pelo agente
        percepcao = ambiente.get_percepcao()
        # Seleciona a próxima ação do agente com base na percepção
        nova_posicao = agente.select_action(percepcao)
        # Atualiza o estado interno do agente com a nova posição
        agente.update_state(nova_posicao)
        # Atualiza a posição do agente no ambiente
        ambiente.update_agente_posicao(nova_posicao)
        # Exibe o estado atual do ambiente
        ambiente.display()

        # Verifica se o agente encontrou o objetivo
        if nova_posicao == ambiente.objetivo_final:
            print("agente encontrou o objetivo em", passos, "passos!")
            break
        
        passos += 1  # Incrementa o contador de passos
        time.sleep(0.1)  # Pausa para tornar a simulação visível
    
    # Se o número máximo de passos for alcançado sem encontrar o objetivo
    if passos >= max_passos:
        print("Número máximo de passos alcançado sem encontrar o objetivo.")


# Parâmetros do ambiente
largura = 50
altura = 30
num_obstaculos = 150

objetivo_final = (27, 40)

# Criação do ambiente e do agente
ambiente = Ambiente(largura, altura, num_obstaculos, objetivo_final)
agente = agente(ambiente)

# Exibição inicial do ambiente
ambiente.display()

# Execução da simulação com um número máximo de 150 passos
simulate(ambiente, agente, max_passos=150)
