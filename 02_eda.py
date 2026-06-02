# =============================================================
#  02_eda.py
#  Análise Exploratória de Dados — Visualizações Iniciais
#  Acidentes de Trânsito em Rodovias Federais — 2025
#  Fonte: Polícia Rodoviária Federal (PRF)
# =============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------------
# CONFIGURAÇÃO VISUAL
# -------------------------------------------------------------
sns.set_theme(style='whitegrid')
plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.family'] = 'DejaVu Sans'

# -------------------------------------------------------------
# CARREGAMENTO E LIMPEZA (replicado para o script ser autossuficiente)
# -------------------------------------------------------------
df = pd.read_csv('datatran2025.csv', sep=';', encoding='latin1')

df['latitude']     = df['latitude'].str.replace(',', '.').astype(float)
df['longitude']    = df['longitude'].str.replace(',', '.').astype(float)
df['km']           = df['km'].str.replace(',', '.').astype(float)
df['data_inversa'] = pd.to_datetime(df['data_inversa'])
df['mes']          = df['data_inversa'].dt.to_period('M')

ordem_dias = ['segunda-feira', 'terça-feira', 'quarta-feira',
              'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

print("Dataset carregado com sucesso!")
print(f"Linhas: {df.shape[0]:,}  |  Colunas: {df.shape[1]}")

# -------------------------------------------------------------
# GRÁFICO 1 — Acidentes por UF
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 5))

contagem_uf = df['uf'].value_counts()
contagem_uf.plot(kind='bar', ax=ax, color='steelblue', edgecolor='white')

ax.set_title('Número de Acidentes por Unidade Federativa', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Estado (UF)', fontsize=11)
ax.set_ylabel('Quantidade de Acidentes', fontsize=11)
ax.tick_params(axis='x', rotation=45)
ax.bar_label(ax.containers[0], fmt='%d', fontsize=7, padding=2)

plt.tight_layout()
plt.savefig('outputs/grafico_acidentes_por_uf.png')
plt.show()

# -------------------------------------------------------------
# GRÁFICO 2 — Top 10 Causas de Acidente
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

top_causas = df['causa_acidente'].value_counts().head(10)
top_causas.sort_values().plot(kind='barh', ax=ax, color='coral', edgecolor='white')

ax.set_title('Top 10 Causas de Acidente', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Quantidade de Acidentes', fontsize=11)
ax.set_ylabel('Causa do Acidente', fontsize=11)
ax.bar_label(ax.containers[0], fmt='%d', fontsize=9, padding=3)

plt.tight_layout()
plt.savefig('outputs/grafico_top_causas.png')
plt.show()

# -------------------------------------------------------------
# GRÁFICO 3 — Distribuição de Mortos por Acidente
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))

sns.histplot(df['mortos'], bins=10, ax=ax, color='firebrick', edgecolor='white')

ax.set_title('Distribuição do Número de Mortos por Acidente', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Número de Mortos', fontsize=11)
ax.set_ylabel('Frequência (Quantidade de Acidentes)', fontsize=11)

plt.tight_layout()
plt.savefig('outputs/grafico_distribuicao_mortos.png')
plt.show()

# -------------------------------------------------------------
# GRÁFICO 4 — Acidentes por Dia da Semana
# -------------------------------------------------------------
contagem_dias = df['dia_semana'].value_counts().reindex(ordem_dias)

fig, ax = plt.subplots(figsize=(10, 5))

contagem_dias.plot(kind='bar', ax=ax, color='mediumseagreen', edgecolor='white')

ax.set_title('Acidentes por Dia da Semana', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Dia da Semana', fontsize=11)
ax.set_ylabel('Quantidade de Acidentes', fontsize=11)
ax.tick_params(axis='x', rotation=30)
ax.bar_label(ax.containers[0], fmt='%d', fontsize=9, padding=3)
ax.set_xticklabels([d.capitalize() for d in ordem_dias], ha='right')

plt.tight_layout()
plt.savefig('outputs/grafico_acidentes_dia_semana.png')
plt.show()

# -------------------------------------------------------------
# GRÁFICO 5 — Acidentes por Fase do Dia
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))

contagem_fase = df['fase_dia'].value_counts()
contagem_fase.plot(kind='bar', ax=ax, color='goldenrod', edgecolor='white')

ax.set_title('Acidentes por Fase do Dia', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Fase do Dia', fontsize=11)
ax.set_ylabel('Quantidade de Acidentes', fontsize=11)
ax.tick_params(axis='x', rotation=30)
ax.bar_label(ax.containers[0], fmt='%d', fontsize=10, padding=3)

plt.tight_layout()
plt.savefig('outputs/grafico_fase_dia.png')
plt.show()

# -------------------------------------------------------------
# GRÁFICO 6 — Evolução Mensal de Acidentes
# -------------------------------------------------------------
evolucao = df.groupby('mes').size()

fig, ax = plt.subplots(figsize=(10, 5))

evolucao.plot(kind='line', ax=ax, marker='o', color='slateblue', linewidth=2)

ax.set_title('Evolução Mensal do Número de Acidentes (2025)', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Mês', fontsize=11)
ax.set_ylabel('Quantidade de Acidentes', fontsize=11)
ax.tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.savefig('outputs/grafico_evolucao_mensal.png')
plt.show()

print("\nGráficos EDA gerados e salvos em outputs/")
