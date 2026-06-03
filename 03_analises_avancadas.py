# =============================================================
#  03_analises_avancadas.py
#  Correlações, Heatmaps e Análise de Severidade
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
URL = 'https://raw.githubusercontent.com/Nickolas3211/datatran2025/master/datatran2025.csv'

df = pd.read_csv(URL, sep=';', encoding='latin1')

df['latitude']     = df['latitude'].str.replace(',', '.').astype(float)
df['longitude']    = df['longitude'].str.replace(',', '.').astype(float)
df['km']           = df['km'].str.replace(',', '.').astype(float)
df['data_inversa'] = pd.to_datetime(df['data_inversa'])

# Subconjunto sem categorias meteorológicas irrelevantes
df_filtrado = df[~df['condicao_metereologica'].isin(['Ignorado', 'Neve'])]

ordem_dias = ['segunda-feira', 'terça-feira', 'quarta-feira',
              'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
dias_label  = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

print("Dataset carregado com sucesso!")
print(f"Linhas: {df.shape[0]:,}  |  Linhas filtradas: {df_filtrado.shape[0]:,}")

# -------------------------------------------------------------
# GRÁFICO 7 — Taxa de Mortalidade por Condição Meteorológica
# -------------------------------------------------------------
grupo = df_filtrado.groupby('condicao_metereologica').agg(
    total_mortos=('mortos', 'sum'),
    total_pessoas=('pessoas', 'sum')
)
grupo['taxa_mortalidade'] = (grupo['total_mortos'] / grupo['total_pessoas'] * 100).round(3)
grupo = grupo.sort_values('taxa_mortalidade', ascending=True)

cores = sns.color_palette('YlOrRd', len(grupo))

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(grupo.index, grupo['taxa_mortalidade'], color=cores, edgecolor='white')

ax.set_title('Taxa de Mortalidade por Condição Meteorológica\n(mortos por 100 pessoas envolvidas em acidentes)',
             fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Taxa de Mortalidade (%)', fontsize=11)
ax.set_ylabel('Condição Meteorológica', fontsize=11)
ax.bar_label(bars, fmt='%.2f%%', fontsize=9, padding=3)
ax.set_xlim(0, grupo['taxa_mortalidade'].max() * 1.2)

plt.tight_layout()
plt.savefig('outputs/correlacao_meteo_taxa_mortalidade.png')
plt.show()

# -------------------------------------------------------------
# GRÁFICO 8 — Classificação dos Acidentes por Condição Meteorológica (%)
# -------------------------------------------------------------
cross = pd.crosstab(
    df_filtrado['condicao_metereologica'],
    df_filtrado['classificacao_acidente'],
    normalize='index'
) * 100

cross = cross.sort_values('Com Vítimas Fatais', ascending=True)

fig, ax = plt.subplots(figsize=(10, 6))
cross[['Com Vítimas Fatais', 'Com Vítimas Feridas', 'Sem Vítimas']].plot(
    kind='barh',
    stacked=True,
    ax=ax,
    color=['firebrick', 'sandybrown', 'steelblue'],
    edgecolor='white',
    width=0.7
)

ax.set_title('Classificação dos Acidentes por Condição Meteorológica (%)',
             fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Proporção (%)', fontsize=11)
ax.set_ylabel('Condição Meteorológica', fontsize=11)
ax.legend(title='Classificação', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=9)
ax.set_xlim(0, 100)

plt.tight_layout()
plt.savefig('outputs/correlacao_meteo_classificacao_stacked.png')
plt.show()

# -------------------------------------------------------------
# GRÁFICO 9 — Heatmap: Condição Meteorológica x Fase do Dia
# -------------------------------------------------------------
ordem_fase = ['Amanhecer', 'Pleno dia', 'Anoitecer', 'Plena Noite']

pivot_meteo = df_filtrado.pivot_table(
    values='mortos',
    index='condicao_metereologica',
    columns='fase_dia',
    aggfunc='sum',
    fill_value=0
)[ordem_fase]

pivot_meteo = pivot_meteo.sort_values('Plena Noite', ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(
    pivot_meteo,
    annot=True,
    fmt='d',
    cmap='Reds',
    linewidths=0.5,
    ax=ax,
    cbar_kws={'label': 'Total de Mortos'}
)

ax.set_title('Total de Mortos por Condição Meteorológica e Fase do Dia',
             fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Fase do Dia', fontsize=11)
ax.set_ylabel('Condição Meteorológica', fontsize=11)
ax.tick_params(axis='x', rotation=0)
ax.tick_params(axis='y', rotation=0)

plt.tight_layout()
plt.savefig('outputs/correlacao_meteo_heatmap_mortos.png')
plt.show()

# -------------------------------------------------------------
# GRÁFICO 10 — Heatmap: Volume Absoluto de Acidentes (UF x Dia)
# -------------------------------------------------------------
pivot_uf = df.pivot_table(
    values='id',
    index='uf',
    columns='dia_semana',
    aggfunc='count',
    fill_value=0
)[ordem_dias]

pivot_uf = pivot_uf.sort_values('sábado', ascending=False)
pivot_uf.columns = dias_label

fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(
    pivot_uf,
    annot=True,
    fmt='d',
    cmap='YlOrRd',
    linewidths=0.4,
    ax=ax,
    cbar_kws={'label': 'Nº de Acidentes'}
)

ax.set_title('Volume de Acidentes por Estado e Dia da Semana',
             fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Dia da Semana', fontsize=11)
ax.set_ylabel('Estado (UF)', fontsize=11)
ax.tick_params(axis='x', rotation=0)
ax.tick_params(axis='y', rotation=0)

plt.tight_layout()
plt.savefig('outputs/heatmap_uf_dia_absoluto.png')
plt.show()

# -------------------------------------------------------------
# GRÁFICO 11 — Heatmap: Distribuição % de Acidentes por Estado
# -------------------------------------------------------------

# Normalizar: cada linha (UF) soma 100%
# Permite comparar o padrão semanal independente do volume do estado
pivot_norm = pivot_uf.div(pivot_uf.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(
    pivot_norm,
    annot=True,
    fmt='.1f',
    cmap='Blues',
    linewidths=0.4,
    ax=ax,
    cbar_kws={'label': '% dos Acidentes do Estado'}
)

ax.set_title('Distribuição (%) de Acidentes por Dia da Semana — por Estado',
             fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Dia da Semana', fontsize=11)
ax.set_ylabel('Estado (UF)', fontsize=11)
ax.tick_params(axis='x', rotation=0)
ax.tick_params(axis='y', rotation=0)

plt.tight_layout()
plt.savefig('outputs/heatmap_uf_dia_normalizado.png')
plt.show()

print("\nGráficos avançados gerados e salvos em outputs/")
