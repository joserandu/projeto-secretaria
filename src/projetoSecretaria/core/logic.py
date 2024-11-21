import pandas as pd

# Carregar o DataFrame do URL
sheet_id = "1OzOHJaxg-4iS8KVFeaiFat237R25IHQD"
gid = "1619324902"  # Substitua com o gid real da aba desejada

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
df = pd.read_csv(url)


class Aluno:
    def __init__(self, nome, n_faltas, telefone):
        self.__nome = nome
        self.__n_faltas = n_faltas
        self.__telefone = telefone

    @staticmethod
    def contar_alunos(df):
        i = 7
        n = 0
        for nome in df.iloc[i:, 2]:
            if pd.notna(nome):
                i += 1
                n += 1
        return n

    @staticmethod
    def conta_dias_aulas(df, procurado):
        i = 0
        for coluna in df.columns[7:]:  # Colunas de H em diante
            if df[coluna].eq(procurado).any():
                i += 1
        return i

    @staticmethod
    def contar_faltas_seguidas(df, n_aulas):
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
                lista_alunos_faltas.append({'nome': nome, 'n_faltas': faltas})

        return lista_alunos_faltas

    def armazenar_faltantes(self):
        """Será criado um dicionário com Nome do aluno, numero de faltas e número de telefone"""
        pass

    def enviar_mensagem(self):
        """Aqui será realizado o loop para o envio das mensagens"""

        pass


n_aulas = Aluno.conta_dias_aulas(df, "x")
print(f"Número de dias de aula: {n_aulas}")

n_alunos = Aluno.contar_alunos(df)
print(f"Número de alunos: {n_alunos}")

alunos_faltas = Aluno.contar_faltas_seguidas(df, n_aulas)

for aluno in alunos_faltas:
    print(f"Aluno: {aluno['nome']} \t \t \t \t \t \t \t Número de faltas consecutivas: {aluno['n_faltas']}")

"""
        for aula in df.iloc[i:, j:]:
            if pd.notna(aula):
                faltas += 1
                j -= 1
                if j == 0:
                    i += 1
            else:
                i += 1
                aluno = {'nome': df.iloc[i, 2], 'n_faltas': faltas}
                lista_alunos_faltas.append(aluno)

        return lista_alunos_faltas
"""
