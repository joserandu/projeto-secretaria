import pandas as pd

# Carregar aba "Chamada2024"
sheet_id = "1OzOHJaxg-4iS8KVFeaiFat237R25IHQD"
gid = "1619324902"  # Substitua com o gid real da aba desejada

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
df = pd.read_csv(url)

# Carregar aba "Cadastro"
sheet_id2 = "1OzOHJaxg-4iS8KVFeaiFat237R25IHQD"
gid2 = "440615686"

url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id2}/export?format=csv&gid={gid2}"
df2 = pd.read_csv(url2)


class Aluno:
    def __init__(self, nome, n_faltas, telefone):
        self.__nome = nome
        self.__n_faltas = n_faltas
        self.__telefone = telefone

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
        """
        last -> n_aulas
        A partir do contar_dias_aulas, vamos obter um índice, e para esse índice, contaremos dele até acharmos um x
        """
        lista_alunos_faltas = []

        # Itera sobre as linhas a partir da linha 7 (onde estão os alunos)
        for i, nome in enumerate(df.iloc[6:, 2], start=6):  # Coluna C contém os nomes
            if pd.notna(nome):  # Ignorar linhas vazias na coluna de nomes
                faltas = 0
                encontrou_presenca = False  # Flag para identificar a última presença

                # Itera pelas colunas de presença (da última aula até a primeira)
                for aula in reversed(df.iloc[i, 7:7 + n_aulas]):  # Colunas de H em diante
                    if pd.notna(aula):  # Se encontrar uma presença (x)
                        encontrou_presenca = True
                        break  # Parar o loop ao encontrar a última presença
                    else:
                        if not encontrou_presenca:  # Contar apenas antes da última presença
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
    def pegar_telefone(lista_alunos):
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

        """Seria interessante que aqui fosse feita alguma lógica para armazenar esses dados em uma planilha"""

        historico = []

        for aluno in alunos_faltantes:
            historico.append({aluno['nome'], aluno['n_faltas']})  # colocar o telefone

        return historico

    @staticmethod
    def enviar_mensagem(alunos_faltantes):
        """Aqui será realizado o loop para o envio das mensagens"""
        pass


n_aulas = Aluno.conta_dias_aulas("x")
print(f"Número de dias de aula: {n_aulas}")

n_alunos = Aluno.contar_alunos()
print(f"Número de alunos: {n_alunos}")

lista_alunos = Aluno.contar_faltas_seguidas(n_aulas)

# for aluno in lista_alunos:
#     print(f"Aluno: {aluno['nome']} \t \t \t \t \t \t \t Número de faltas consecutivas: {aluno['n_faltas']}")

alunos_faltas = Aluno.pegar_telefone(lista_alunos)

for aluno in alunos_faltas:
    print(f"Aluno: {aluno['nome']} \t \t \t Número de faltas consecutivas: {aluno['n_faltas']}"
          f"\t \t \tTelefone: {aluno.get('telefone')}")

print("\nAlunos faltantes ----------------------------------------------------------------------------------------\n")

alunos_faltantes = Aluno.listar_faltantes(lista_alunos)

for aluno in alunos_faltantes:
    print(f"Aluno: {aluno['nome']} \t \t \t \t \t \t \t Número de faltas consecutivas: {aluno['n_faltas']}"
          f"\t \t \t \t \t \t \tTelefone: {aluno.get('telefone')}")
