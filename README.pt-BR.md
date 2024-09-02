# Detecção-de-Desordem-Cognitiva

## Visão Geral

**Detecção-de-Desordem-Cognitiva** é um projeto em Python 3.10 desenvolvido para detectar a probabilidade de um paciente ter um distúrbio cognitivo com base em seus desenhos. O projeto utiliza um modelo de aprendizado de máquina, especificamente uma Máquina de Vetores de Suporte (SVM), que foi treinado com dados de imagem para alcançar uma precisão de 73%. O foco principal é detectar comprometimento cognitivo, como Comprometimento Cognitivo Leve (CCL) ou outras desordens neurodegenerativas, usando desenhos analisados através do sistema de pontuação MoCA (Montreal Cognitive Assessment).

## Pontuações MoCA

O **Montreal Cognitive Assessment (MoCA)** é um teste de triagem cognitiva amplamente utilizado, projetado para ajudar na detecção de comprometimento cognitivo leve. O teste MoCA avalia diversos domínios cognitivos, incluindo memória, atenção, linguagem, habilidades visuoespaciais e função executiva. Uma pontuação de 26 ou superior é geralmente considerada normal, enquanto pontuações mais baixas podem indicar comprometimento cognitivo.

Neste projeto, as pontuações MoCA são inferidas com base nos desenhos dos pacientes, como desenhos de relógios, que são avaliados pelo modelo SVM treinado.

## Conjunto de Dados

As imagens usadas para treinar e testar o modelo neste projeto são obtidas a partir do seguinte repositório:

[https://github.com/cccnlab/MCI-multiple-drawings/tree/main](https://github.com/cccnlab/MCI-multiple-drawings/tree/main)

Este conjunto de dados inclui diversos desenhos que foram utilizados para avaliar comprometimento cognitivo em pacientes.

## Requisitos

Para executar este projeto, você precisará de:

- Python 3.* ou superior (3.10 é a versão recomendada)
- pip (gerenciador de pacotes do Python)

## Configuração

1. Clone o repositório e navegue até o diretório do projeto.
2. Certifique-se de que você tem Python 3.* ou superior e pip instalados no seu sistema.
3. Execute o script de configuração para preparar o ambiente:

   ```bash
   ./scripts/setup.sh
   ```
4. Após configurar o ambiente, inicie a aplicação executando:

   ```bash
   ./scripts/start.sh
   ```

## Como Funciona

- O projeto cria um ambiente virtual, instala as dependências necessárias e configura os diretórios necessários para salvar o modelo treinado e o escalonador.
- O modelo SVM é treinado com o conjunto de dados fornecido e salvo para uso posterior.
- A aplicação principal inclui uma interface de usuário simples (UI) que permite aos usuários fazer o upload de desenhos e receber uma previsão sobre se o paciente pode ter um distúrbio cognitivo, com base nos critérios de pontuação MoCA.
