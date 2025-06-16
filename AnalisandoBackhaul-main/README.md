# 📊 Análise de Prestadoras de Backhaul - São José dos Campos

Este projeto realiza uma análise detalhada dos dados de prestadoras de serviços de backhaul em São José dos Campos, categorizando-as por meio de transporte utilizado (Fibra, Rádio ou Ambos).

## 🎯 Objetivo

Analisar e categorizar as prestadoras de serviços de backhaul em São José dos Campos com base nos dados dos anos 2023-2024, identificando:
- Prestadoras que utilizam apenas **Fibra**
- Prestadoras que utilizam apenas **Rádio**  
- Prestadoras que utilizam **ambos os meios**
- Estatísticas e percentuais por categoria

## 📁 Estrutura do Projeto

```
DataSetBackhaul/
├── analise.py                          # Script principal de análise
├── backhaul_municipios_2023-2024.csv   # Dataset original
├── relatorio_sjc_backhaul.txt          # Relatório gerado automaticamente
└── README.md                           # Este arquivo
```

## 🚀 Como Usar

### Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas padrão do Python (csv, collections, typing, dataclasses, pathlib)

### Execução

1. **Clone ou baixe o projeto**
2. **Navegue até o diretório do projeto**
3. **Execute o script:**

```bash
python analise.py
```

### Saída Esperada

O script irá:
1. Carregar automaticamente os dados do arquivo CSV
2. Filtrar apenas os registros de São José dos Campos
3. Exibir a análise no terminal
4. Salvar um relatório detalhado em `relatorio_sjc_backhaul.txt`

## 📊 Exemplo de Saída

```
🔄 Carregando dados de São José dos Campos do arquivo original...
📋 Cabeçalhos encontrados: ['Ano', 'Município', 'UF', 'Código IBGE', 'Prestadora', 'CNPJ', 'Meio Transporte']
✅ Arquivo carregado com encoding: utf-8
📊 Total de registros carregados: 39

================================================================================
📊 ANÁLISE DE PRESTADORAS DE BACKHAUL - SÃO JOSÉ DOS CAMPOS
================================================================================

📈 ESTATÍSTICAS GERAIS:
   • Total de registros analisados: 39
   • Total de prestadoras únicas: 20
   • Período analisado: 2023 - 2024

🔵 PRESTADORAS QUE UTILIZAM APENAS FIBRA (14):
   • TELEFONICA BRASIL S.A.
   • CLARO S.A.
   • TIM S A
   [...]

📡 PRESTADORAS QUE UTILIZAM APENAS RÁDIO (3):
   • DIRECTNET PRESTACAO DE SERVICOS LTDA
   • VOGEL SOLUCOES EM TELECOMUNICACOES E INFORMATICA S.A.
   • WIRELESS COMM SERVICES LTDA

🔄 PRESTADORAS QUE UTILIZAM AMBOS OS MEIOS (3):
   • CLARO S.A.
   • TELEFONICA BRASIL S.A.
   • TIM S A

📊 RESUMO ESTATÍSTICO:
   • Apenas Fibra: 14 (70.0%)
   • Apenas Rádio: 3 (15.0%)
   • Ambos os meios: 3 (15.0%)
```

## 🏗️ Arquitetura do Código

### Classes Principais

#### `RegistroBackhaul`
Dataclass que representa um registro individual do dataset:
- `ano`: Ano do registro
- `municipio`: Nome do município
- `uf`: Unidade federativa
- `codigo_ibge`: Código IBGE do município
- `prestadora`: Nome da prestadora
- `cnpj`: CNPJ da prestadora
- `meio_transporte`: Tipo de meio (Fibra/Rádio)

#### `AnalisadorBackhaul`
Classe principal responsável pela análise:
- **`carregar_dados_csv()`**: Carrega dados do arquivo CSV com tratamento de encoding
- **`categorizar_prestadoras()`**: Categoriza prestadoras por meio de transporte
- **`gerar_relatorio()`**: Gera relatório formatado
- **`salvar_relatorio()`**: Salva relatório em arquivo

### Funcionalidades

✅ **Carregamento Robusto**: Testa múltiplos encodings automaticamente  
✅ **Tratamento de BOM**: Remove Byte Order Mark automaticamente  
✅ **Filtros**: Filtra dados por município específico  
✅ **Validação**: Verifica se os dados foram carregados corretamente  
✅ **Relatórios**: Gera relatórios formatados com estatísticas  
✅ **Exportação**: Salva resultados em arquivo texto  

## 📈 Insights da Análise

Com base nos dados de São José dos Campos (2023-2024):

- **70%** das prestadoras utilizam apenas **Fibra**
- **15%** das prestadoras utilizam apenas **Rádio**
- **15%** das prestadoras utilizam **ambos os meios**

### Prestadoras Híbridas (Fibra + Rádio)
As seguintes prestadoras oferecem flexibilidade tecnológica:
- CLARO S.A.
- TELEFONICA BRASIL S.A.
- TIM S A

## 🔧 Personalização

### Para Analisar Outro Município

Modifique a linha no arquivo `analise.py`:

```python
analisador.carregar_dados_csv("backhaul_municipios_2023-2024.csv", "Nome do Município")
```

### Para Analisar Todos os Municípios

Remova o filtro:

```python
analisador.carregar_dados_csv("backhaul_municipios_2023-2024.csv")
```

## 📋 Formato dos Dados

O arquivo CSV deve conter as seguintes colunas:
- `Ano`: Ano do registro
- `Município`: Nome do município
- `UF`: Unidade federativa
- `Código IBGE`: Código IBGE do município
- `Prestadora`: Nome da prestadora
- `CNPJ`: CNPJ da prestadora
- `Meio Transporte`: Fibra ou Rádio

## 🐛 Solução de Problemas

### Erro de Encoding
O script testa automaticamente múltiplos encodings. Se ainda houver problemas, verifique o formato do arquivo CSV.

### Nenhum Dado Carregado
- Verifique se o arquivo `backhaul_municipios_2023-2024.csv` existe
- Confirme se o nome do município está correto (case-sensitive)
- Verifique se o arquivo contém dados para o município especificado

### Erro de Permissão
Certifique-se de que tem permissão de leitura no arquivo CSV e escrita no diretório para salvar o relatório.

## 📝 Licença

Este projeto é de uso livre para fins educacionais e de análise de dados.

## 👨‍💻 Autor Liriel Castro

Desenvolvido para análise de dados de telecomunicações e backhaul.

---

**Última atualização:** 2025
**Versão:** 1.0 