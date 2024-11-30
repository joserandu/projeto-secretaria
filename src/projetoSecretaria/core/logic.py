import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import urllib.parse
from selenium.webdriver.common.by import By

# Carregar aba "Chamada2024"
sheet_id = "1OzOHJaxg-4iS8KVFeaiFat237R25IHQD"
gid = "1619324902"  # Substitua com o gid real da aba desejada

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
df = pd.read_csv(url)

# Carregar aba "Cadastro"
gid2 = "440615686"

url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid2}"
df2 = pd.read_csv(url2)


class Aluno:

    @staticmethod
    def contar_alunos():
        i = 7
        n = 0
        for nome in df.iloc[i:, 2]:
            if pd.notna(nome):
                i += 1
                n += 1
        return n

    @staticmethod
    def conta_dias_aulas(procurado):
        i = 0
        for coluna in df.columns[7:]:  # Colunas de H em diante
            if df[coluna].eq(procurado).any():
                i += 1
        return i

    @staticmethod
    def contar_faltas_seguidas(n_aulas):

        lista_alunos_faltas = []

        for i, nome in enumerate(df.iloc[6:, 2], start=6):
            if pd.notna(nome):
                faltas = 0
                encontrou_presenca = False

                for aula in reversed(df.iloc[i, 7:7 + n_aulas]):
                    if pd.notna(aula):
                        encontrou_presenca = True
                        break
                    else:
                        if not encontrou_presenca:
                            faltas += 1

                # Adiciona o resultado para o aluno
                lista_alunos_faltas.append({'nome': nome, 'n_faltas': faltas, 'telefone': ''})  # colocar o telefone

        return lista_alunos_faltas

    @staticmethod
    def listar_faltantes(alunos_faltas):
        """Será criado um dicionário com Nome do aluno, numero de faltas e número de telefone"""

        lista_faltantes = []

        for aluno in alunos_faltas:
            if aluno['n_faltas'] > 3:
                nome = aluno['nome']
                faltas = aluno['n_faltas']
                lista_faltantes.append({'nome': nome, 'n_faltas': faltas})  # colocar o telefone

        return lista_faltantes

    @staticmethod
    def adicionar_telefone(lista_alunos):
        for aluno in lista_alunos:
            aluno_nome = aluno['nome']
            telefone = None

            for i, nome in df2.iloc[:, 19].items():
                if nome == aluno_nome:
                    telefone = df2.iloc[i, 77]
                    break

            aluno['telefone'] = telefone

        return lista_alunos

    @staticmethod
    def armazenar_faltantes(alunos_faltantes):

        """
        Prioridade Média:

        Seria interessante que aqui fosse feita alguma lógica para armazenar esses dados em uma planilha
        """

        historico = []

        for aluno in alunos_faltantes:
            historico.append({aluno['nome'], aluno['n_faltas'], aluno['telefone']})  # colocar o telefone

        return historico

    @staticmethod
    def enviar_mensagem(alunos_faltantes):
        """Aqui será realizado o loop para o envio das mensagens"""

        # Inicializa o navegador
        navegador = webdriver.Chrome()

        # Abre a página do WhatsApp Web
        navegador.get("https://web.whatsapp.com/")

        # Verificação se estamos na página do WhatsApp, id="side" é o da barra lateral de conversas
        while len(navegador.find_elements(By.ID, "side")) < 1:
            time.sleep(1)

        for aluno in alunos_faltantes:

            telefone = aluno.get('telefone')

            if not telefone:
                # Se o telefone é None, string vazia, ou 0, ignorar e passar para o próximo aluno
                continue

            try:

                # Define o número de telefone e a mensagem
                telefone = aluno['telefone']

                nome = aluno['nome']
                mensagem = f"""
Sentimos sua falta!

Bom dia/Boa tarde, {nome},

Esperamos que você esteja bem.

Notamos que sua frequência no cursinho tem sido baixa e gostaríamos de saber se há algo com o qual  possamos ajudar. Entendemos que imprevistos acontecem e estamos aqui para oferecer suporte, seja ele acadêmico ou até mesmo pessoal.

Sua presença é muito importante para nós, pois acreditamos em você e na sua capacidade de conseguir alcançar seus sonhos e objetivos. 

Se houver algum problema ou dificuldade que você esteja enfrentando, por favor, não deixe de nos contatar. Estamos disponíveis para conversar e encontrar soluções que possam facilitar sua participação nas aulas.

Aguardamos o seu retorno e desejamos que você possa retomar suas atividades conosco o mais breve possível.

Um abraço,

Cursinho Comunitário Bonsucesso.
                """
                mensagem = "Sentimos sua falta!\n\nBom dia/Boa tarde, [Nome do Aluno],\nEsperamos que você esteja bem.\n\nNotamos que sua frequência no cursinho tem sido baixa e gostaríamos de saber se há algo com o qual possamos ajudar. Entendemos que imprevistos acontecem e estamos aqui para oferecer suporte, seja ele acadêmico ou até mesmo pessoal.\n\nSua presença é muito importante para nós, pois acreditamos em você e na sua capacidade de conseguir alcançar seus sonhos e objetivos.\n\nSe houver algum problema ou dificuldade que você esteja enfrentando, por favor, não deixe de nos contatar. Estamos disponíveis para conversar e encontrar soluções que possam facilitar sua participação nas aulas. \n\nAguardamos o seu retorno e desejamos que você possa retomar suas atividades conosco o mais breve possível.\n\nUm abraço,\n\nCursinho Comunitário Bonsucesso."

# Esse código apareceu do nada, depois ver o que é
# >>>>>>> 85d31270fb5377ed86e5b765b1e586778139c7c3

                # Codifica a mensagem para URL encoding
                texto = urllib.parse.quote(mensagem)
                link = f"{telefone}?text={texto}"

                # Abrir o link com a mensagem
                navegador.get(link)

                while len(navegador.find_elements(By.ID, "action-button")) < 1:
                    time.sleep(1)

                navegador.find_element(By.ID, "action-button").click()

                while len(navegador.find_elements(By.LINK_TEXT, "usar o WhatsApp Web")) < 1:
                    time.sleep(1)

                navegador.find_element(By.LINK_TEXT, "usar o WhatsApp Web").click()

                # Verificação se a conversa foi aberta, id="main" é o da área principal de conversas
                while len(navegador.find_elements(By.ID, "main")) < 1:
                    time.sleep(1)

                # Enviar a mensagem
                campo_de_mensagem = navegador.find_element(By.XPATH,
                                                           '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/'
                                                           'div/div/p')
                campo_de_mensagem.send_keys(Keys.ENTER)

                # Mantém o navegador aberto por um tempo para garantir que a mensagem seja enviada
                time.sleep(15)

            except Exception as e:
                print(f"Erro ao enviar mensagem para o telefone {telefone}: {e}")

        # Fecha o navegador
        navegador.quit()


# Main

def main():

    n_aulas = Aluno.conta_dias_aulas("x")
    print(f"Número de dias de aula: {n_aulas}")

    n_alunos = Aluno.contar_alunos()
    print(f"Número de alunos: {n_alunos}")

    lista_alunos = Aluno.contar_faltas_seguidas(n_aulas)

    # for aluno in lista_alunos:
    #     print(f"Aluno: {aluno['nome']} \t \t \t \t \t \t \t Número de faltas consecutivas: {aluno['n_faltas']}")

    alunos_faltas = Aluno.adicionar_telefone(lista_alunos)

    for aluno in alunos_faltas:
        print(f"Aluno: {aluno['nome']} \t \t \t Número de faltas consecutivas: {aluno['n_faltas']}"
              f"\t \t \tTelefone: {aluno.get('telefone')}")

    print("\nAlunos faltantes --------------------------------------------------------------------------------------\n")

    alunos_faltantes = Aluno.listar_faltantes(lista_alunos)
    alunos_faltantes = Aluno.adicionar_telefone(alunos_faltantes)

    for aluno in alunos_faltantes:
        print(f"Aluno: {aluno['nome']} \t \t \t Número de faltas consecutivas: {aluno['n_faltas']}"
              f"\t \t \tTelefone: {aluno['telefone']}")

    Aluno.enviar_mensagem(alunos_faltantes)
