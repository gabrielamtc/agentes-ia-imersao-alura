# ☀️ Planejador de Fim de Semana Inteligente (FDS.IA)

[![Status do Projeto](https://img.shields.io/badge/status-concluído-brightgreen)](https://www.google.com/search?q=status+do+projeto)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue)](https://www.python.org/downloads/)
[![Licença](https://img.shields.io/badge/licença-MIT-green)](https://opensource.org/licenses/MIT)
## 🏆 Projeto Submetido à 2ª Imersão Alura+Google

**Descubra o seu fim de semana ideal com o FDS.IA!** Uma solução inovadora que utiliza agentes de inteligência artificial para planejar seus momentos de lazer, levando em consideração o seu perfil e a sua localização.

## 💡 Ideia Central

Cansado de passar o fim de semana sem saber o que fazer? O FDS.IA surge como um assistente inteligente capaz de gerar planos personalizados para o seu fim de semana. Ao compreender o perfil das pessoas envolvidas e a cidade onde estão, o sistema utiliza agentes de IA para identificar critérios importantes, buscar eventos relevantes e, finalmente, propor um cronograma otimizado.

A motivação principal deste projeto é simplificar o processo de planejamento do lazer, oferecendo sugestões que realmente correspondam aos interesses e necessidades dos usuários, explorando o potencial da inteligência artificial para tornar os momentos de descanso mais prazerosos e significativos.

## 🚀 Funcionalidades Principais

1.  **Identificação Inteligente de Público Alvo:** Um agente de IA analisa o perfil das pessoas (fornecido pelo usuário) e define critérios essenciais para um bom passeio, como tipo de ambiente (aberto/fechado), nível de ruído, acessibilidade, permissões (animais, fumantes, crianças) e outros.
2.  **Busca Dinâmica de Eventos:** Com base nos critérios definidos e na cidade do usuário, outro agente realiza uma busca inteligente na internet por eventos e locais que correspondam a essas preferências. O sistema considera promoções, novidades e a previsão do tempo para o fim de semana, além de priorizar locais com boas avaliações.
3.  **Planejamento Personalizado do Fim de Semana:** Um agente planejador organiza os eventos encontrados em um cronograma coerente para o fim de semana (sexta, sábado e domingo), sugerindo no máximo 2 ou 3 atividades para evitar um roteiro exaustivo. O planejamento leva em conta restrições de locomoção e religiosas, buscando um equilíbrio entre as preferências do grupo.

## ⚙️ Tecnologias Utilizadas

Este projeto utiliza as seguintes tecnologias e bibliotecas Python:

* **`google-genai`**: A biblioteca do Gemini API é o motor por trás da inteligência dos agentes, permitindo a geração de texto, compreensão de linguagem natural e a tomada de decisões informadas para o planejamento do fim de semana.
* **`google-adk`**: O Android Development Kit (ADK) é utilizado como o framework para a criação e orquestração dos agentes de IA, facilitando a definição de suas instruções, ferramentas e fluxos de trabalho.
* **`google-api-python-client`**: Embora não explicitamente utilizado no código fornecido, esta biblioteca pode ter sido considerada para interagir com outras APIs do Google (como Places API para detalhes de locais), o que demonstra uma visão de expansibilidade do projeto. *(Gabriela, se você explorou essa biblioteca para alguma finalidade, mesmo que não finalizada, mencione aqui!)*
* **`requests`**: Utilizada para realizar requisições HTTP, possivelmente para buscar informações adicionais sobre eventos ou para integrar com outras APIs de terceiros.
* **`ipython`**: Usado no ambiente de desenvolvimento (Google Colab) para uma interação facilitada com o código e visualização dos resultados.
* **`datetime`**: Biblioteca padrão do Python para manipulação de datas, essencial para determinar o dia atual e planejar o fim de semana.
* **`textwrap`**: Utilizada para formatar a saída de texto, melhorando a legibilidade das respostas dos agentes.
* **`IPython.display`**: Módulo do IPython para exibir conteúdo formatado (como Markdown) no ambiente Colab, crucial para apresentar os resultados dos agentes de forma clara.

## 🛠️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter o seguinte instalado:

* Python 3.9 ou superior ([Link para download do Python](https://www.python.org/downloads/))
* pip (geralmente instalado com o Python)
* Uma chave de API do Google Gemini configurada no Google Colab (conforme demonstrado no código).

## ⚙️ Instalação

1.  Clone este repositório (se estiver compartilhando o código):
    ```bash
    git clone [https://link-do-seu-repositorio]
    cd planejador_fds
    ```
2.  No Google Colab, siga as instruções no código para configurar a sua chave de API do Google Gemini utilizando o `userdata`.
3.  As dependências necessárias são instaladas diretamente no ambiente Colab através do comando `%pip install -q google-genai` e `!pip install -q google-adk`.

## 🕹️ Como Executar

Este projeto foi desenvolvido principalmente para ser executado em um ambiente Google Colab. Para utilizá-lo:

1.  Abra o notebook do Google Colab onde o código foi desenvolvido.
2.  Certifique-se de ter configurado a sua chave de API do Google Gemini conforme as instruções no código.
3.  Execute as células de código em sequência. O sistema irá solicitar as informações sobre as pessoas e a cidade no prompt.
4.  Os resultados do planejamento serão exibidos no formato Markdown, mostrando os critérios identificados, os eventos encontrados e o plano para o fim de semana.

## 🧪 Próximos Passos e Melhorias

Algumas ideias para aprimoramento futuro incluem:

* **Interface de Usuário Mais Amigável:** Desenvolver uma interface gráfica (web ou mobile) para facilitar a interação do usuário, eliminando a necessidade de inserir dados via linha de comando.
* **Integração com Calendários:** Permitir que o plano gerado seja integrado diretamente ao calendário do usuário.
* **Recomendação de Locais:** Adicionar um agente que possa recomendar restaurantes, parques e outros locais de interesse com base no perfil do usuário e nos eventos planejados.
* **Aprendizado Contínuo:** Implementar um sistema de feedback para que o agente aprenda com as preferências do usuário ao longo do tempo, tornando as recomendações cada vez mais precisas.
* **Consideração de Orçamento:** Adicionar um parâmetro de orçamento para refinar a busca de eventos e locais.

## 🧑‍💻 Desenvolvedora

**Gabriela Chaves**

[GitHub] (https://github.com/gabrielamtc)
[LinkedIn] (https://www.linkedin.com/in/gabriela-muniz-telo-chaves)
