# Criacao de agente inteligente

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
