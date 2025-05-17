######################################

# Planejador FDS #

######################################

# Este código tem por objetivo criar agentes de IA que auxiliem
# o usuário a planejar um bom fim de semana (FDS),
# dado o perfil das pessoas e a cidade onde estão.

######################################

# Feito por: Gabriela Chaves
# Divirta-se! :)

######################################

%pip -q install google-genai

# Configura a API Key do Google Gemini

import os
from google.colab import userdata

os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')

# Configura o cliente da SDK do Gemini

from google import genai

client = genai.Client()

MODEL_ID = "gemini-2.0-flash"

# Instala o framework de agentes do Google
!pip install -q google-adk

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types  # Para criar conteúdos (Content e Part)
from datetime import date
import textwrap # Para formatar melhor a saída de texto
from IPython.display import display, Markdown # Para exibir texto formatado no Colab
import requests # Para fazer requisições HTTP
import warnings

warnings.filterwarnings("ignore")

# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def call_agent(agent: Agent, message_text: str) -> str:
    # Cria um serviço de sessão em memória
    session_service = InMemorySessionService()
    # Cria uma nova sessão (você pode personalizar os IDs conforme necessário)
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    # Cria um Runner para o agente
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Cria o conteúdo da mensagem de entrada
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    # Itera assincronamente pelos eventos retornados durante a execução do agente
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response
    
# Função auxiliar para exibir texto formatado em Markdown no Colab
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
  
##########################################
# Agente 1: Identificador de público alvo #
##########################################
def agente_identificador(lista_pessoas):

    identificador = Agent(
        name="agente_identificador",
        model="gemini-2.0-flash",
        instruction="""
        Você deve saber quais os critérios um bom passeio deve ter, com base no público que quer agradar.
        Por exemplo, se o seu público é uma família com bebê pequeno, sabe que um critério de um bom passeio de fim de semana é que ele tenha um local apropriado para trocar fraldas.
        Se o seu público são jovens que gostam de beber, um bar animado é a cena ideal.
        Você deve definir esses critérios com base no público alvo.
        Esses critérios devem ser: se o ambiente é aberto ou fechado, se é barulhento, se permite animais, se permite fumantes, se tem ambiente para crianças, se é acessível (uma trilha, por exemplo, não seria indicado para cadeirantes), entre outros.
        """,
        description="Agente que define critérios para um bom passeio de fim de semana"
    )

    entrada_do_agente_identificador = f"Pessoas: {lista_pessoas}\n"

    criterios = call_agent(identificador, entrada_do_agente_identificador)
    return criterios
    
################################################
# Agente 2: Buscador de eventos na internet #
################################################
def agente_buscador(criterios, cidade):
    buscador = Agent(
        name="agente_buscador",
        model="gemini-2.0-flash",
        instruction="""
        Você é um especialista em buscar eventos na sua cidade.
        Ao saber dos critérios do seu público alvo, como se é lugar aberto ou fechado, qual o tempo de duração, etc, você deve buscar na internet por eventos que atendam a esses critérios.
        Por exemplo, se é um evento para crianças e de curta duração, você pode propor um circo. Se é para idosos, pode propor um teatro. E assim por diante.
        Considere sempre buscar descontos e novidades na cidade, usando palavras chave como "promoções", "descontos", "novidades", "somente neste fim de semana".
        Você também deve verificar se no próximo final de semana vai chover, buscando no google.
        Considere eventos e locais que tenham uma boa avaliação no Google.
        """,
        description="Agente que busca eventos no Google",
        tools=[google_search]
    )

    entrada_do_agente_buscador = f"""
        Critérios de aceitação: {criterios}
        Cidade: {cidade}
        """

    # Executa o agente
    eventos = call_agent(buscador, entrada_do_agente_buscador)
    return eventos
    
######################################
# Agente 3: Planejador do fim de semana #
######################################
def agente_planejador(eventos, lista_pessoas, data_de_hoje):
    planejador = Agent(
        name="agente_planejador",
        model="gemini-2.0-flash",
        instruction="""
            Você é ótimo em planejar finais de semana.
            Seja para uma família, seja para amigos que buscam eventos animados, o seu trabalho é entender o público alvo, verificar os eventos disponíveis na cidade e propor um cronograma para o final de semana.
            Considere planejar apenas 2 ou 3 eventos num fim de semana, para não ficar cansativo.
            Considere eventos e restrições religiosas, além de restrições de locomoção.
            Seu plano deve conter: dia (sexta, sábado ou domingo), turno (manhã, tarde, noite) ou horário (caso o evento tenha horário certo para começar) e o nome do evento, além do endereço.
            Lembre-se se fazer no máximo 3 eventos, por exemplo, 1 evento no turno da noite de sexta, 1 evento no turno da noite de sábado e 1 evento no turno da manhã de domingo.
            """,
        description="Agente planejador de eventos de fins de semana",
    )
    entrada_do_agente_planejador = f"""
        Eventos da cidade neste fim de semana: {eventos}
        Pessoas: {lista_pessoas}\n
        """
    
    # Executa o agente
    plano = call_agent(planejador, entrada_do_agente_planejador)
    return plano
    
# Formata a data de hoje
data_de_hoje = date.today().strftime("%d/%m/%Y")

# Uma mensagem inicial ao usuário do agente
print("Iniciando sistema de agentes de IA capazes de planejar o fim de semana ideal, eventos na cidade indicada.")

# Ler os dados do usuário: pessoas envolvidas e a cidade
lista_pessoas = input("Por favor, indique quantas e quais são as pessoas que irão aos eventos. Diga se elas possuem limitações de locomoção ou religiosas. Quanto mais informações forem fornecidas ao modelo, mais específico ele será. Como sugestão, use o modelo: Número de pessoas: [número inteiro], Perfil das pessoas: [exemplo: "adulto jovem solteiro", "família com bebê"], Restrições: [exemplo: mobilidade reduzida, religião, restrição alimentar].")
cidade = input("Por favor, diga o CEP de onde você mora. (evite colocar seu endereço completo por questões de tratamento de dados sensíveis)")

# Tratamento de dados
if not lista_pessoas:
  print("Por favor, precisamos dos dados das pessoas que serão envolvidas nos eventos.")
elif not cidade:
  print("Por favor, precisamos do CEP da cidade.")
elif len(cidade) != 8:
  print("Por favor, insira um CEP válido.")
else:
  try:

# Lógica dos agentes
    criterios = agente_identificador(lista_pessoas)
    print("\n--- 📝 Resultado do Agente 1 (Identificador) ---\n")
    display(to_markdown(criterios))
    print("--------------------------------------------------------------")

    eventos = agente_buscador(criterios, cidade)
    print("\n--- 📝 Resultado do Agente 2 (Buscador) ---\n")
    display(to_markdown(eventos))
    print("--------------------------------------------------------------")

    plano = agente_planejador(eventos, lista_pessoas, data_de_hoje)
    print("\n--- 📝 Resultado do Agente 3 (Planejador) ---\n")
    display(to_markdown(plano))
    print("--------------------------------------------------------------") 

# Exceptions caso algum dado de entrada não seja válido
  except ValueError:
      print("Erro: Por favor, insira valores numéricos válidos.")
  except IndexError:
      print("Erro: Problema ao processar os dados de entrada.")

