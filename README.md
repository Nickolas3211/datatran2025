🇧🇷 Português | [🇺🇸 English](README_en.md)

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
├── datatran2025.csv              # Dataset bruto — Acidentes PRF 2025
│
├── outputs/                      # Gráficos gerados
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

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/Nickolas3211/datatran2025.git
cd datatran2025
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Crie a pasta de outputs

```bash
mkdir outputs
```

### 4. Execute os scripts em ordem

```bash
python 01_limpeza.py
python 02_eda.py
python 03_analises_avancadas.py
```

> O dataset é carregado automaticamente a partir deste repositório — não é necessário baixar nenhum arquivo separado.

> Os scripts também podem ser executados diretamente no **Spyder** — basta abrir cada arquivo e rodar com F5.

---

## 📊 Análises e Resultados

### 1. Acidentes por Unidade Federativa

![Acidentes por UF](outputs/grafico_acidentes_por_uf.png)

Minas Gerais lidera com folga (9.570 acidentes), seguida de Santa Catarina (8.186) e do Paraná (7.630). Juntos, esses três estados concentram mais de **34% de todos os acidentes do país**. Vale destacar que esse volume não significa, necessariamente, que esses estados são mais perigosos, MG, por exemplo, possui uma das maiores malhas de rodovias federais do Brasil. Para uma análise mais justa, o ideal seria cruzar com os quilômetros de rodovia por estado.

---

### 2. Top 10 Causas de Acidente

![Top 10 Causas](outputs/grafico_top_causas.png)

As duas primeiras causas se destacam: "Ausência de reação do condutor" (11.469) e "Reação tardia ou ineficiente" (10.799); juntas somam mais de 22 mil acidentes, quase **30% do total**. Na prática, ambas apontam para o mesmo problema: falta de atenção ao volante, que hoje inclui o uso do celular e a fadiga. A **ingestão de álcool** aparece em 7º lugar, com 3.685 casos, um número expressivo, considerando que é 100% evitável.

---

### 3. Distribuição de Mortos por Acidente

![Distribuição de Mortos](outputs/grafico_distribuicao_mortos.png)

O gráfico apresenta uma distribuição assimétrica à direita: a grande maioria dos acidentes concentra-se na barra do zero. **92,8% dos acidentes não resultaram em mortes**, mas os 7,2% que tiveram resultaram em mais de **6.000 vítimas fatais**, chegando a casos extremos com até 16 mortos em um único acidente. Isso evidencia que, embora raro, o acidente fatal tende a ser grave.

---

### 4. Acidentes por Dia da Semana

![Acidentes por Dia da Semana](outputs/grafico_acidentes_dia_semana.png)

Sexta, sábado e domingo concentram os maiores volumes, com pico no **sábado (11.554 acidentes)**. De segunda a quinta, os números são mais baixos e estáveis, entre 9 e 10 mil. Esse padrão reflete o comportamento das pessoas: maior movimentação nos fins de semana, viagens mais longas e maior consumo de álcool.

---

### 5. Acidentes por Fase do Dia

![Acidentes por Fase do Dia](outputs/grafico_fase_dia.png)

Pleno dia domina com 40.375 acidentes (55% do total), o que é esperado devido ao maior volume de tráfego. O dado mais preocupante é o segundo lugar: **Plena Noite, com 24.781 acidentes**, uma proporção muito alta para um período em que havia muito menos veículos nas ruas. Isso sugere que a noite é desproporcionalmente perigosa, provavelmente devido à menor visibilidade, ao cansaço e à maior disponibilidade de álcool.

---

### 6. Evolução Mensal de Acidentes

![Evolução Mensal](outputs/grafico_evolucao_mensal.png)

Janeiro e fevereiro registraram os menores volumes (5.528 e 5.287, respectivamente). A partir de março, os números sobem e se estabilizam entre 6.000 e 6.300 por mês, com um **pico em dezembro (6.788)**, o mês de maior movimentação nas estradas por conta das festas de fim de ano. A tendência de crescimento ao longo do ano pode indicar tanto um aumento real de acidentes quanto uma melhora no registro e na notificação.

---

### 7. Taxa de Mortalidade por Condição Meteorológica

![Taxa de Mortalidade por Condição Meteorológica](outputs/correlacao_meteo_taxa_mortalidade.png)

**Nevoeiro/Neblina lidera com folga (~5%)**, bem acima da chuva (~2,8%), um resultado contraintuitivo, já que a chuva é normalmente mais associada a acidentes graves. A explicação está na visibilidade: o nevoeiro reduz drasticamente o campo de visão, pegando o motorista de surpresa. Condições de céu claro têm taxa mais baixa, justamente por serem a condição de maior tráfego e de melhor visibilidade.

---

### 8. Classificação dos Acidentes por Condição Meteorológica (%)

![Classificação por Condição Meteorológica](outputs/correlacao_meteo_classificacao_stacked.png)

O gráfico mostra a proporção entre acidentes fatais, feridos com e sem vítimas para cada condição meteorológica. Permite comparar visualmente o "peso" de cada categoria e confirma que condições como nevoeiro e granizo, apesar de menor volume absoluto, concentram uma proporção maior de acidentes com vítimas fatais em relação ao total.

---

### 9. Mortos por Condição Meteorológica e Fase do Dia

![Heatmap Meteorológico](outputs/correlacao_meteo_heatmap_mortos.png)

O cruzamento entre a condição meteorológica e a fase do dia revela que **céu claro durante o dia concentra o maior número absoluto de mortes**, reflexo direto do volume de tráfego. Porém, quando analisamos proporcionalmente, o nevoeiro noturno se destaca como a combinação mais letal. O heatmap deixa claro que os fatores se potencializam: a má visibilidade, somada à noite, cria as condições mais perigosas.

---

### 10. Volume de Acidentes por Estado e Dia da Semana

![Heatmap UF x Dia (Absoluto)](outputs/heatmap_uf_dia_absoluto.png)

O heatmap em volume absoluto confirma a predominância de MG, SC e PR em todos os dias da semana. O sábado é, consistentemente, o dia mais crítico na maioria dos estados. Estados menores, como RR e AP, registram volumes baixos ao longo de toda a semana, enquanto SP apresenta distribuição mais uniforme ao longo dos dias.

---

### 11. Distribuição % de Acidentes por Estado e Dia da Semana

![Heatmap UF x Dia (Normalizado)](outputs/heatmap_uf_dia_normalizado.png)

Ao normalizar por estado (cada linha soma 100%), removemos o efeito do tamanho e focamos no **padrão semanal de cada UF**. A distribuição é relativamente uniforme entre os estados, todos concentram entre 13% e 16% dos acidentes no sábado. Isso indica que o pico de fim de semana é um fenômeno nacional, não restrito a estados específicos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **pandas** — manipulação e análise dos dados
- **matplotlib** — construção dos gráficos
- **seaborn** — estilização e gráficos estatísticos

---

## 👤 Autor

**Nickolas Santana**  
[LinkedIn](https://www.linkedin.com/in/nickolas-mateus-225587260/) • [GitHub](https://github.com/Nickolas3211)
