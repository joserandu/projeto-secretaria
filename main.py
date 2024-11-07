import pandas as pd


# Função para contar o número de dias de aula
# Função para contar o número de dias de aula
def conta_dias_aulas(df, target_value):
    i = 0
    for column in df.columns[7:]:  # Colunas de H em diante
        if df[column].eq(target_value).any():
            i += 1
    return i


# Carregar o DataFrame do URL
sheet_id = "1OzOHJaxg-4iS8KVFeaiFat237R25IHQD"
gid = "1619324902"  # Substitua com o gid real da aba desejada

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
df = pd.read_csv(url)
# Número de dias de aula
n_aulas = conta_dias_aulas(df, "x")
print(f"Número de dias de aula: {n_aulas}")

# Número da última coluna a ser verificada (coluna H é a 8ª coluna no Excel)
ultima_coluna = 7 + n_aulas  # H é a 8ª coluna (índice 7)

# Selecionar apenas as colunas de interesse (H até a última coluna determinada)
selected_columns = df.iloc[7:131, 7:ultima_coluna]  # Linhas 8 a 130, Colunas H até a última coluna

# Adicionar a coluna de nomes dos alunos
nomes_alunos = df.iloc[7:131, 2]  # Coluna C, Linhas 8 a 130

# Contar o número de faltas consecutivas para cada aluno
for index, row in selected_columns.iterrows():
    faltas_consecutivas = 0
    encontrou_presenca = False
    for value in reversed(row):  # Itera da última aula para a primeira
        if value == "x" or value == "X":
            encontrou_presenca = True
            break
        else:
            faltas_consecutivas += 1

    nome_aluno = nomes_alunos.iloc[index]
    if encontrou_presenca:
        print(f"Nome do aluno: {nome_aluno}\nNúmero de faltas consecutivas: {faltas_consecutivas}")
    else:
        print(f"Nome do aluno: {nome_aluno}\nNúmero de faltas consecutivas: {faltas_consecutivas} (nenhuma presença "
              f"registrada)")
