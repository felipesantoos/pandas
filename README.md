# Pandas
Repositório de códigos e anotações sobre o módulo Pandas da linguagem Python.

# Artigo 01
- É uma biblioteca Python.
- É usado para analizar conjuntos de dados.

# Artigo 02
- Nos permite analizar grandes quantidades de dados e fazer conclusões com base em teorias estatísticas.
- > **Data science:** estuda como armazenar, usar e analizar dados para extrair informações.
- É usado para encontrar correlações entre duas ou mais colunas, calcular valores médios, encontrar valores mínimos e máximos.
- Apaga linhas não não são relevantes ou que possuem valores errados (vazios ou nulos). Isso se chama *limpeza*.
- https://github.com/pandas-dev/pandas

# Artigo 03
- É preciso ter o `Python` e o `pip` instalados.
- Instale o pandas com o comando `pip install pandas` ou (no meu caso) `python3 -m pip install pandas`.

# Artigo 04
- `Series Pandas` são como colunas em uma tabela.
- É um array unidimensional que armazena dados de qualquer tipo.
- Uma label é uma valor que identifica uma linha na série criada.
- Podemos nomear as labels com o argumento `index`.
- As chaves dos dicionários se tornam labels.
- DataFrames são tabelas (multidimensionais).

# Artigo 05
- Um `DataFrame` é uma estrutura de dados bidimensional.
- É como um matriz bidimensional ou uma tabela com linhas e colunas.
- É possível carregar arquivos externos dentro de um DataFrame.

# Artigo 06
- Um CSV é um arquivo cujos valores (colunas) são separados por vírgulas.
- CSV significa comma-separated-values.

# Artigo 07
- JSON é um arquivo com texto puro com formato de objeto.
- JSONs tem o mesmo formato de um dicionário em Python.

# Artigo 08
```shell
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  169 non-null    int64
 1   Pulse     169 non-null    int64
 2   Maxpulse  169 non-null    int64   
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None
```
- Informações:
    - 168 linhas.
    - 4 colunas.
    - Nome das colunas, quantidade de valores não nulos em cada coluna e tipos dos dados de cada coluna.
    - 5 valores nulos.

- Valores vazios (ou nulos) podem ser ruins ao analisar dados.
- Para resolver esse problema realizamos o processo de `limpeza dos dados`.
