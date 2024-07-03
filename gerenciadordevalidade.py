from datetime import datetime, timedelta
import webbrowser
from urllib.parse import quote

# Classe para representar um alimento com nome, quantidade e data de validade
class Alimento:
  def __init__(self, nome, quantidade, data_validade):
    self.nome = nome
    self.quantidade = quantidade
    self.data_validade = datetime.strptime(data_validade, "%d/%m/%Y")

# Função para obter a quantidade de um alimento do usuário
def obter_quantidade():
  while True:
    try:
      quantidade = int(input("Digite quantidade do alimento: "))
      return quantidade
    except ValueError:
      print("Quantidade inválida. Tente novamente.")

# Função para obter a data de validade de um alimento do usuário
def obter_validade():
  while True:
    data = input("Digite a data de validade (formato DD/MM/AAAA): ")
    try:
      data_validade = datetime.strptime(data, "%d/%m/%Y")
      return data_validade
    except ValueError:
      print("Data inválida. Tente novamente.")

# Função para adicionar alimentos à lista de alimentos
def adicionar_alimento(lista_alimentos):

  print("\nADICIONAR ALIMENTO:\n")
  print("OBS.: Se houver mais de um alimento igual com datas de validade diferentes, registre-o separadamente.")

  while True:
    try:
      nome = input("\nDigite o nome do alimento (ou 'sair' para terminar): ")
      if nome.lower() == 'sair':
          print("")
          break

      data_validade = obter_validade()
      quantidade = obter_quantidade()
      alimento = Alimento(nome, quantidade, data_validade.strftime("%d/%m/%Y"))

      lista_alimentos.append(alimento)

    except ValueError:
      print("ERRO! Tente Novamente.")

  return lista_alimentos

# Função para verificar quais alimentos estão próximos de vencer
def verificar_validade(lista_alimentos, dias_antes=15):

  hoje = datetime.today()
  prazo = hoje + timedelta(days=dias_antes)
  proximos_de_vencer = []

  for alimento in lista_alimentos:
      if alimento.data_validade <= prazo:
          proximos_de_vencer.append(alimento)

  return proximos_de_vencer

# Função para exibir alimentos próximos de vencer
def exibir_alimentos(alimentos):
  if alimentos:
    print("\nOs seguintes alimentos estão próximos de vencer:\n")
    for alimento in sorted(alimentos, key=lambda x: x.data_validade):
      print(f"{alimento.nome} ({alimento.quantidade}x) - Data de validade: {alimento.data_validade.strftime('%d/%m/%Y')}\n")
  else:
    print("\nNenhum alimento está próximo de vencer.\n")

# Função para exibir todos os alimentos em ordem de validade
def exibir_todos_alimentos(alimentos):
  if alimentos:
    print("\nTodos os alimentos em ordem de validade:\n")
    for alimento in sorted(alimentos, key=lambda x: x.data_validade):
        print(f"{alimento.nome} ({alimento.quantidade}x) - Data de validade: {alimento.data_validade.strftime('%d/%m/%Y')}\n")
  else:
    print("\nNenhum alimento registrado.\n")

# Função para apresentar receitas com base nos alimentos próximos de vencer
def apresentar_receitas(proximos_de_vencer):
  if proximos_de_vencer:
    print("\nReceitas sugeridas para os alimentos próximos de vencer:\n")
    for alimento in proximos_de_vencer:
        nome_formatado = quote(alimento.nome)
        link = f"https://www.tudogostoso.com.br/busca?q={nome_formatado}"
        print(f"Receitas para {alimento.nome}: {link}\n")
        webbrowser.open(link)
  else:
    print("\nNenhum alimento próximo de vencer para sugerir receitas.\n")

# Função principal para exibir o menu e executar ações com base na escolha do usuário
def menu():
  lista_alimentos = []
  print("Bem-vindo ao Gerenciador de Validade de Alimentos!\n")

  while True:
    print("1. Adicionar alimento")
    print("2. Verificar quais estão próximos de vencer")
    print("3. Exibir todos os alimentos")
    print("4. Apresentar receitas para alimentos próximos de vencer")
    print("5. Sair")

    try:
      acao = int(input("\nDigite qual ação deseja realizar: "))

      if acao == 1:
          lista_alimentos = adicionar_alimento(lista_alimentos)

      elif acao == 2:
          proximos_de_vencer = verificar_validade(lista_alimentos)
          exibir_alimentos(proximos_de_vencer)

      elif acao == 3:
          exibir_todos_alimentos(lista_alimentos)

      elif acao == 4:
          proximos_de_vencer = verificar_validade(lista_alimentos)
          apresentar_receitas(proximos_de_vencer)

      elif acao == 5:
          print("Fechando programa...")
          break

      else:
          print("ERRO. Digite apenas números de 1 à 5.")

    except ValueError:
        print("ERRO. Digite apenas números de 1 à 5.")

menu()
