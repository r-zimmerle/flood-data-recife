import pandas as pd

# Carregar a planilha CSV
df = pd.read_csv('data/solicitacoes.csv')  # Planilha de solicitações

# Lista de palavras relacionadas a alagamento
keywords = ['alagamento', 'alagou', 'alagada', 'alagar', 'alago', 'inundação', 'inundou', 'inundar']

# Criar um padrão regex com todas as palavras
pattern = '|'.join(keywords)

# Filtrar as linhas que contenham qualquer uma das palavras-chave e que sejam a partir do ano de 2019
filtered_df = df[(df['solicitacao_descricao'].str.contains(pattern, case=False, na=False)) & (df['ano'] >= 2019)]

# Remover duplicatas com base na coluna 'processo_numero'
filtered_df = filtered_df.drop_duplicates(subset='processo_numero')

# Carregar a planilha de validação
df_validation = pd.read_csv('data/tipo-ocorrencia.csv')

# Fazer o merge das duas planilhas com base no número do processo
df_merged = pd.merge(filtered_df, df_validation[['processo_numero', 'processo_ocorrencia']], on='processo_numero', how='left')

# Filtrar apenas as ocorrências confirmadas como "Alagamentos" ou "Imoveis Alagados"
confirmados = df_merged[df_merged['processo_ocorrencia'].isin(['Alagamentos', 'Imoveis Alagados'])]

# Salvar o resultado em um novo CSV
confirmados.to_csv('output/alagamentos_confirmados.csv', index=False)

print("Arquivo de alagamentos confirmados foi criado com sucesso!")
