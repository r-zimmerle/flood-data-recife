# Análise de Chamados de Alagamentos em Recife

## Descrição

Este projeto tem como objetivo coletar, analisar e espacializar dados de chamados relacionados a alagamentos na cidade do Recife, utilizando ferramentas como Python e ArcGIS. Baseado em dados abertos fornecidos pela Prefeitura do Recife, o projeto visa facilitar a visualização e identificação das áreas mais suscetíveis a alagamentos na cidade.

No repositório, você encontrará códigos que coletam os dados do portal de dados abertos, aplicam filtros (como ano e tipo de chamado), realizam a geocodificação dos endereços para obter coordenadas geográficas e, por fim, permitem a espacialização em softwares GIS.

## Etapas do Projeto

### 1. Coleta de Dados

Os dados foram extraídos do portal de dados abertos da Prefeitura do Recife no dia **07 de outubro de 2024**, especificamente das seguintes planilhas:

- **Solicitações**: [Baixar CSV](http://dados.recife.pe.gov.br/dataset/45dbabee-0352-411a-b289-66fccde8942a/resource/fa35d810-b291-4e74-9282-3c4db1aca312/download/sedec_solicitacoes.csv)
- **Tipos de Ocorrências dos Chamados**: [Baixar CSV](http://dados.recife.pe.gov.br/dataset/45dbabee-0352-411a-b289-66fccde8942a/resource/7a22d871-250e-419a-9b5a-1cab19db7be5/download/sedec_tipo_ocorrencias.csv)

Os dados estão disponíveis no portal de dados abertos da Prefeitura do Recife: [http://dados.recife.pe.gov.br/](http://dados.recife.pe.gov.br/)

Os arquivos devem ser baixados e colocados na pasta `/data`.

### 2. Processamento e Filtragem dos Dados

O script `processar_dados.py` realiza o filtro dos chamados relacionados a alagamentos a partir do ano de 2019 e faz a validação com base nos tipos de ocorrências confirmadas.

**Como funciona:**

- Filtra as linhas que contêm palavras-chave relacionadas a alagamentos na coluna `solicitacao_descricao`.
- Filtra os dados a partir de um ano específico (padrão: 2019).
- Faz o merge com a planilha de tipos de ocorrências para validar os alagamentos confirmados.
- Remove duplicatas com base na coluna `processo_numero` para garantir que cada chamado seja único.
- Gera o arquivo `alagamentos_confirmados.csv` na pasta `/output`.

### 3. Geocodificação

O script `geocodificacao.py` utiliza a API do Google Maps para obter as coordenadas geográficas (latitude e longitude) dos endereços confirmados.

**Como funciona:**

- Lê o arquivo `alagamentos_confirmados.csv` da pasta `/output`.
- Para cada endereço, faz a geocodificação adicionando "Recife, Pernambuco, Brasil" ao final.
- Gera o arquivo `alagamentos_com_coordenadas.csv` com as coordenadas na pasta `/output`.

### 4. Espacialização dos Dados

Com o arquivo `alagamentos_com_coordenadas.csv`, os dados podem ser importados para o ArcGIS ou QGIS para gerar um mapa de pontos representando os chamados de alagamento.

**Como proceder:**

- **Usando ArcGIS ou QGIS:**
  - Utilize a ferramenta **"XY Table to Point"** (ou equivalente) para converter a tabela CSV em pontos geográficos.
  - Configure as colunas de latitude e longitude correspondentes.
  - Projete os pontos no sistema de coordenadas adequado para a região.
- **Resultado:**
  - Um mapa com os pontos dos alagamentos confirmados, permitindo análises espaciais e visualização das áreas mais afetadas.

### 5. Resultados

Os resultados incluem um mapa geoespacial com os pontos dos chamados, facilitando a visualização das áreas mais propensas a alagamentos em Recife.

## Como Usar

### Pré-requisitos

- Python 3.x
- Chave da API do Google Maps (colocar em `/config/geocoding-api.txt`)
- Instalar as dependências:

```bash
pip install -r requirements.txt
```
## Executando o projeto

1. Clone o repositório:
```bash
git clone https://github.com/r-zimmerle/flood-data-recife
cd seu-repositorio
```
2. Coloque os dados na pasta /data:
Baixe os arquivos CSV mencionados na seção de Coleta de Dados.
Coloque-os na pasta data/.
3. Configure sua chave da API do Google Maps:
Crie o arquivo config/geocoding-api.txt.
Cole sua chave da API dentro desse arquivo.
Importante: Não comite este arquivo no Git (já está listado no .gitignore).
4. Execute os scripts manualmente

Processamento dos Dados:
```bash
python src/processar_dados.py
```
Geocodificação:
```bash
python src/geocodificacao.py
```
## Dependências
As dependências do projeto estão listadas em `requirements.txt`:
```
pandas
geopy
```
Instale-as com:
```
pip install -r requirements.txt
```
## Observações
1. Limites da API: A geocodificação utiliza a API do Google Maps, que possui limites de uso e pode gerar custos.
2. Certifique-se de estar ciente dos termos de uso da API.
3. Tratamento de Erros: O script de geocodificação inclui tratamento de exceções para lidar com possíveis erros durante a obtenção das coordenadas.
4. Contribuições: Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença e Dados

- **Licença do Código:** Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.
- **Licença dos Dados:** Os dados utilizados neste projeto são provenientes do portal de dados abertos da Prefeitura do Recife. Verifique os termos de uso [aqui](http://dados.recife.pe.gov.br/pages/terms/).

