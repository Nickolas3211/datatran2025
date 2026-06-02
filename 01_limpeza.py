# =============================================================
#  01_limpeza.py
#  Carregamento e limpeza dos dados
#  Acidentes de Trânsito em Rodovias Federais — 2025
#  Fonte: Polícia Rodoviária Federal (PRF)
# =============================================================

import pandas as pd

# -------------------------------------------------------------
# CARREGAMENTO
# -------------------------------------------------------------
df = pd.read_csv('datatran2025.csv', sep=';', encoding='latin1')

print("=== DADOS BRUTOS ===")
print(f"Linhas: {df.shape[0]:,}  |  Colunas: {df.shape[1]}")
print()
print(df.dtypes)
print()
print("Valores nulos por coluna:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# -------------------------------------------------------------
# LIMPEZA E CONVERSÃO DE TIPOS
# -------------------------------------------------------------

# Latitude e longitude chegam como texto com vírgula decimal
df['latitude']  = df['latitude'].str.replace(',', '.').astype(float)
df['longitude'] = df['longitude'].str.replace(',', '.').astype(float)

# km também usa vírgula decimal
df['km'] = df['km'].str.replace(',', '.').astype(float)

# Converter data para o tipo datetime (permite cálculos e agrupamentos por período)
df['data_inversa'] = pd.to_datetime(df['data_inversa'])

# Criar coluna auxiliar de mês para análises temporais
df['mes'] = df['data_inversa'].dt.to_period('M')

# -------------------------------------------------------------
# SUBCONJUNTO FILTRADO
# Usado nas análises meteorológicas:
# remove categorias com volume irrisório (Neve, Ignorado)
# -------------------------------------------------------------
df_filtrado = df[~df['condicao_metereologica'].isin(['Ignorado', 'Neve'])]

# -------------------------------------------------------------
# VARIÁVEIS AUXILIARES REUTILIZADAS NOS SCRIPTS SEGUINTES
# -------------------------------------------------------------
ordem_dias = ['segunda-feira', 'terça-feira', 'quarta-feira',
              'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

dias_label = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

# -------------------------------------------------------------
# VERIFICAÇÃO FINAL
# -------------------------------------------------------------
print()
print("=== DADOS APÓS LIMPEZA ===")
print(f"Linhas totais:    {df.shape[0]:,}")
print(f"Linhas filtradas: {df_filtrado.shape[0]:,}")
print(f"Período:          {df['data_inversa'].min().date()} a {df['data_inversa'].max().date()}")
print()
print(df.dtypes)
