# 🚦 Análise Exploratória de Dados — Acidentes de Trânsito em Rodovias Federais (2025)

Projeto de Análise Exploratória de Dados (AED) sobre acidentes registrados em rodovias federais brasileiras no ano de 2025, com base nos dados abertos da **Polícia Rodoviária Federal (PRF)**.

---

## 📋 Sobre o Dataset

| Atributo | Detalhe |
|---|---|
| **Fonte** | [Polícia Rodoviária Federal — Dados Abertos](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos) |
| **Arquivo** | `datatran2025.csv` |
| **Registros** | 72.529 acidentes |
| **Colunas** | 30 variáveis |
| **Período** | Janeiro a Dezembro de 2025 |
| **Separador** | `;` (ponto e vírgula) |
| **Encoding** | `latin1` |

### Principais variáveis analisadas

| Variável | Descrição |
|---|---|
| `uf` | Estado onde ocorreu o acidente |
| `causa_acidente` | Causa registrada do acidente |
| `condicao_metereologica` | Condição do tempo no momento do acidente |
| `fase_dia` | Período do dia (Amanhecer, Pleno dia, Anoitecer, Plena Noite) |
| `dia_semana` | Dia da semana |
| `mortos` | Número de mortos no acidente |
| `feridos_leves` | Número de feridos leves |
| `feridos_graves` | Número de feridos graves |
| `pessoas` | Total de pessoas envolvidas |
| `classificacao_acidente` | Com Vítimas Fatais / Com Vítimas Feridas / Sem Vítimas |

---

## 📁 Estrutura do Projeto

```
datatran2025/
│
├── 01_limpeza.py                 # Carregamento, limpeza e conversão de tipos
├── 02_eda.py                     # Análise Exploratória inicial (6 gráficos)
├── 03_analises_avancadas.py      # Correlações e heatmaps (5 gráficos)
│
├── outputs/                      # Gráficos gerados (criada automaticamente)
│   ├── grafico_acidentes_por_uf.png
│   ├── grafico_top_causas.png
│   ├── grafico_distribuicao_mortos.png
│   ├── grafico_acidentes_dia_semana.png
│   ├── grafico_fase_dia.png
│   ├── grafico_evolucao_mensal.png
│   ├── correlacao_meteo_taxa_mortalidade.png
│   ├── correlacao_meteo_classificacao_stacked.png
│   ├── correlacao_meteo_heatmap_mortos.png
│   ├── heatmap_uf_dia_absoluto.png
│   └── heatmap_uf_dia_normalizado.png
│
├── requirements.txt              # Dependências do projeto
├── .gitignore                    # Arquivos ignorados pelo Git
└── README.md                     # Este arquivo
```

> ⚠️ O arquivo `datatran2025.csv` **não está versionado** (ver `.gitignore`). Faça o download diretamente no site da PRF e coloque na raiz do projeto antes de rodar os scripts.

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/datatran2025.git
cd datatran2025
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Baixe o dataset

Acesse [dados.gov.br](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos), baixe o arquivo `datatran2025.csv` e coloque na raiz do projeto.

### 4. Crie a pasta de outputs

```bash
mkdir outputs
```

### 5. Execute os scripts em ordem

```bash
python 01_limpeza.py
python 02_eda.py
python 03_analises_avancadas.py
```

> Os scripts também podem ser executados diretamente no **Spyder** — basta abrir cada arquivo e rodar com F5.

---

## 📊 Análises Realizadas

### EDA Inicial (`02_eda.py`)

| # | Gráfico | Tipo |
|---|---|---|
| 1 | Acidentes por Unidade Federativa | Barras verticais |
| 2 | Top 10 Causas de Acidente | Barras horizontais |
| 3 | Distribuição de Mortos por Acidente | Histograma |
| 4 | Acidentes por Dia da Semana | Barras verticais |
| 5 | Acidentes por Fase do Dia | Barras verticais |
| 6 | Evolução Mensal de Acidentes | Linha com marcadores |

### Análises Avançadas (`03_analises_avancadas.py`)

| # | Gráfico | Tipo |
|---|---|---|
| 7 | Taxa de Mortalidade por Condição Meteorológica | Barras horizontais com gradiente |
| 8 | Classificação dos Acidentes por Condição Meteorológica | Barras empilhadas (%) |
| 9 | Mortos por Condição Meteorológica e Fase do Dia | Heatmap |
| 10 | Volume de Acidentes por Estado e Dia da Semana | Heatmap (absoluto) |
| 11 | Distribuição % de Acidentes por Estado e Dia | Heatmap (normalizado) |

---

## 🔍 Principais Achados

- **Minas Gerais, Santa Catarina e Paraná** concentram mais de 34% dos acidentes do país
- **Falta de atenção ao volante** é responsável por quase 30% de todos os acidentes (ausência de reação + reação tardia)
- **92,8%** dos acidentes não resultam em mortes — mas os 7,2% fatais somam mais de 6.000 vítimas
- **Sexta, sábado e domingo** registram os maiores volumes de acidentes
- **Plena noite** é desproporcionalmente perigosa: alto número de acidentes para um período de baixo tráfego
- **Nevoeiro/Neblina** apresenta a maior taxa de mortalidade (~5%), superando até a chuva (~2,8%)
- A condição de **céu claro** tem mais mortes em volume absoluto, mas isso se deve ao volume total de acidentes

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **pandas** — manipulação e análise dos dados
- **matplotlib** — construção dos gráficos
- **seaborn** — estilização e gráficos estatísticos

---

## 👤 Autor

Desenvolvido como projeto de portfólio de Análise de Dados.  
Sinta-se à vontade para abrir issues ou contribuir com melhorias.
