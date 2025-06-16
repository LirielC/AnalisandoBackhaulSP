# 📊 Análise de Prestadoras de Backhaul – São Paulo (SP)

Este documento foca exclusivamente na análise dos dados de prestadoras de serviços de **backhaul** no município de **São Paulo/SP**, usando o mesmo dataset nacional 2023-2024.

---

## 🎯 Objetivo

• Identificar e categorizar as prestadoras por meio de transporte utilizado para o backhaul:

- **Fibra óptica**
- **Rádio**
- **Ambos os meios**

• Gerar estatísticas e relatórios fáceis de reproduzir.

---

## 📁 Estrutura do Projeto

```
AnalisandoBackhaul-main/
├── analise.py                     # Script principal
├── backhaul_municipios_2023-2024.csv
├── relatorio_sao_paulo_backhaul.txt  # Relatório gerado (este repositório)
└── README_Sao_Paulo.md            # Este arquivo
```

---

## 🚀 Como Executar a Análise para São Paulo

1. Garanta que possui **Python 3.7+** instalado.
2. No terminal/power-shell, navegue até a pasta do projeto:
   ```bash
   cd AnalisandoBackhaul-main
   ```
3. Execute o script com o parâmetro de município:
   ```bash
   python analise.py -m "São Paulo"
   ```
4. O relatório será mostrado na tela e salvo como `relatorio_sao_paulo_backhaul.txt`.

> Obs.: se desejar analisar outro município basta trocar o nome após `-m`.

---

## 📈 Resultados (dataset 2023-2024)

| Métrica | Valor |
|---------|-------|
| Registros analisados | **134** |
| Prestadoras únicas    | **90** |
| Apenas Fibra          | **69** (76,7 %) |
| Apenas Rádio          | **12** (13,3 %) |
| Ambos os meios        | **8**  (8,9 %) |

### Prestadoras que Utilizam Ambos os Meios

🔵 **Prestadoras que Utilizam Apenas Fibra (69)**

```
ACESSE COMUNICACAO LTDA
ACESSO NET SERVICOS LTDA - EPP
ACESSOLINE TELECOMUNICACOES LTDA
ALGAR TELECOM S/A
ALTA REDE CORPORATE LTDA
AMERICAN TOWER DO BRASIL - COMUNICACAO MULTIMIDIA LTDA
ASCENTY DATA CENTERS E TELECOMUNICAÇÕES S/A
America Net S.a.
B R A SERVICOS DE COMUNICACAO EIRELI
BRASILNET TELECOMUNICAÇÕES DO PARANÁ - EIRELI
CENTURY TELECOM LTDA
CLAUDEMON SILVEIRA - ME
CTI COMUNICACAO DE DADOS E TECNOLOGIA LTDA
DINAMICA TELECOMUNICACOES LTDA
DZ7 TELECOMUNICACOES LTDA
Desktop - Sigmanet
Desktop Internet Ltda
ESTRELAS TECNOLOGIA DA INFORMAÇÃO LTDA - ME
Ejm Net Tecnologia Ltda
FONATA TELECOMUNICACOES LTDA.
Fiber Kings Internet Ltda
Flay Telecomunicacoes Ltda
G8 NETWORKS LTDA
GOOGLE INFRAESTRUTURA BRASIL LTDA
IDC TELECOM LTDA
INTERFOX TELECOMUNICACOES EIRELI
INTERNEXA BRASIL OPERADORA DE TELECOMUNICACOES S.A.
IPNET TELECOM LTDA.
IRANTEC TECNOLOGIA EM COMUNICACAO MULTIMIDIA LTDA - ME
JAS GAB PROVEDORES DE ACESSOS A INTERNET SCM E COMERCIO DE EQUIPAMENTOS DE INFORMATICA E SERVICOS LTDA-ME
JR & JS - TELECOM LTDA
L & J REDES DE TELECOMUNICACAO E INFORMATICA LTDA
LCS WIFI LTDA
LUXFIBRA TELECOMUNICACOES LTDA
MASTER TELECOM LTDA.
MICRON INTERNET LTDA
MM Telecomunicacoes Ltda
MULTICAST TELECOM LTDA
MUNDIVOX TELECOMUNICACOES LTDA
Megatelecom Telecomunicacoes S.a.
Mogi Fibra Telecomunicacoes Slu Ltda
NETFI SERVIÇOS DE COMUNICAÇÕES LTDA
NEW H.B. SERVICOS DE TELECOMUNICACOES LTDA
OPÇÃOTELECOM TELECOMUNICAÇÕES S/A
Op Telecom Ltda
PONGAR TELECOMUNICAÇÕES EIRELI
R. RODRIGUES DOS SANTOS PROVEDORES DE INTERNET
REDE LANDAN INTERNET EIRELI - ME
SAMM - SOCIEDADE DE ATIVIDADES EM MULTIMÍDIA LTDA.
SEABRAS 1 BRASIL LTDA.
SETE MEIA TELECOMUNICACOES LTDA
SILVERNET TECNOLOGIA LTDA
SINAL BR TELECOM LTDA
SUMICITY TELECOMUNICACOES S.A.
TECHCOM COMUNICACAO, COMERCIO E SERVICOS LTDA
TELCABLES BRASIL LTDA
TELEFONICA BRASIL S.A.
TELXIUS CABLE BRASIL LTDA.
TERA SOLUÇÕES TECNOLÓGICAS SLU LTDA
THREE TELECOM EM FIBRA OPTICA LTDA
Telecomunicacoes Brasileiras S.A. Telebras
Tera Corporation Telecomunicacoes Slu Ltda
UFINET BRASIL S.A
UNIVERSAL NET-SERVICOS DE COMUNICACAO MULTIMIDIA LTDA
V.TAL - REDE NEUTRA DE TELECOMUNICACOES S.A.
VNT FIBRA TELECOMUNICAÇÕES LTDA.
VSX NETWORKS LTDA
Vip Br Telecom S.a.
Wip Telecom Multimidia Ltda
```

📡 **Prestadoras que Utilizam Apenas Rádio (12)**

```
Atlanet Telecomunicacoes Ltda
DIRECTNET PRESTACAO DE SERVICOS LTDA
Global Web Master Ltda
HIT TELECOMUNICACOES LTDA.
I T S - COMERCIO DE PECAS E EQUIPAMENTOS LTDA. - EPP
LEOMAX TELECOM LTDA
MEC SOLUTION LTDA
NETWALK TELECOMUNICACOES EM INFORMATICA LTDA-ME
Rss Comunicacao Ltda
SPACE NET REDES DE INTERNET EIRELI
TMC - TECNOLOGIA EM TELECOMUNICACOES LTDA
URSOFT TELECOM LTDA
```

🔄 **Prestadoras que Utilizam Ambos os Meios (8)**

```
ALFA NETWORK SOLUTIONS INFORMÁTICA LTDA - ME
ATTUS TECNOLOGIA EM TELECOMUNICACOES EIRELI
CLARO S.A.
FENIX INTERNET COMUNICACOES EIRELI
Ozonio Telecomunicacoes Ltda
TIM S A
VOGEL SOLUCOES EM TELECOMUNICACOES E INFORMATICA S.A.
WIRELESS COMM SERVICES LTDA
```

---

## 🐍 Exemplo de Saída

```
🔄 Carregando dados do arquivo original para o município: São Paulo ...
📋 Cabeçalhos encontrados: ['Ano', 'Município', 'UF', 'Código IBGE', 'Prestadora', 'CNPJ', 'Meio Transporte']
✅ Arquivo carregado com encoding: utf-8
📊 Total de registros carregados: 134

================================================================================
📊 ANÁLISE DE PRESTADORAS DE BACKHAUL - SÃO PAULO
================================================================================

📈 ESTATÍSTICAS GERAIS:
   • Total de registros analisados: 134
   • Total de prestadoras únicas: 90
   • Período analisado: 2023 - 2024

🔵 **Prestadoras que Utilizam Apenas Fibra (69)**

```
ACESSE COMUNICACAO LTDA
ACESSO NET SERVICOS LTDA - EPP
ACESSOLINE TELECOMUNICACOES LTDA
ALGAR TELECOM S/A
ALTA REDE CORPORATE LTDA
AMERICAN TOWER DO BRASIL - COMUNICACAO MULTIMIDIA LTDA
ASCENTY DATA CENTERS E TELECOMUNICAÇÕES S/A
America Net S.a.
B R A SERVICOS DE COMUNICACAO EIRELI
BRASILNET TELECOMUNICAÇÕES DO PARANÁ - EIRELI
CENTURY TELECOM LTDA
CLAUDEMON SILVEIRA - ME
CTI COMUNICACAO DE DADOS E TECNOLOGIA LTDA
DINAMICA TELECOMUNICACOES LTDA
DZ7 TELECOMUNICACOES LTDA
Desktop - Sigmanet
Desktop Internet Ltda
ESTRELAS TECNOLOGIA DA INFORMAÇÃO LTDA - ME
Ejm Net Tecnologia Ltda
FONATA TELECOMUNICACOES LTDA.
Fiber Kings Internet Ltda
Flay Telecomunicacoes Ltda
G8 NETWORKS LTDA
GOOGLE INFRAESTRUTURA BRASIL LTDA
IDC TELECOM LTDA
INTERFOX TELECOMUNICACOES EIRELI
INTERNEXA BRASIL OPERADORA DE TELECOMUNICACOES S.A.
IPNET TELECOM LTDA.
IRANTEC TECNOLOGIA EM COMUNICACAO MULTIMIDIA LTDA - ME
JAS GAB PROVEDORES DE ACESSOS A INTERNET SCM E COMERCIO DE EQUIPAMENTOS DE INFORMATICA E SERVICOS LTDA-ME
JR & JS - TELECOM LTDA
L & J REDES DE TELECOMUNICACAO E INFORMATICA LTDA
LCS WIFI LTDA
LUXFIBRA TELECOMUNICACOES LTDA
MASTER TELECOM LTDA.
MICRON INTERNET LTDA
MM Telecomunicacoes Ltda
MULTICAST TELECOM LTDA
MUNDIVOX TELECOMUNICACOES LTDA
Megatelecom Telecomunicacoes S.a.
Mogi Fibra Telecomunicacoes Slu Ltda
NETFI SERVIÇOS DE COMUNICAÇÕES LTDA
NEW H.B. SERVICOS DE TELECOMUNICACOES LTDA
OPÇÃOTELECOM TELECOMUNICAÇÕES S/A
Op Telecom Ltda
PONGAR TELECOMUNICAÇÕES EIRELI
R. RODRIGUES DOS SANTOS PROVEDORES DE INTERNET
REDE LANDAN INTERNET EIRELI - ME
SAMM - SOCIEDADE DE ATIVIDADES EM MULTIMÍDIA LTDA.
SEABRAS 1 BRASIL LTDA.
SETE MEIA TELECOMUNICACOES LTDA
SILVERNET TECNOLOGIA LTDA
SINAL BR TELECOM LTDA
SUMICITY TELECOMUNICACOES S.A.
TECHCOM COMUNICACAO, COMERCIO E SERVICOS LTDA
TELCABLES BRASIL LTDA
TELEFONICA BRASIL S.A.
TELXIUS CABLE BRASIL LTDA.
TERA SOLUÇÕES TECNOLÓGICAS SLU LTDA
THREE TELECOM EM FIBRA OPTICA LTDA
Telecomunicacoes Brasileiras S.A. Telebras
Tera Corporation Telecomunicacoes Slu Ltda
UFINET BRASIL S.A
UNIVERSAL NET-SERVICOS DE COMUNICACAO MULTIMIDIA LTDA
V.TAL - REDE NEUTRA DE TELECOMUNICACOES S.A.
VNT FIBRA TELECOMUNICAÇÕES LTDA.
VSX NETWORKS LTDA
Vip Br Telecom S.a.
Wip Telecom Multimidia Ltda
```

📡 **Prestadoras que Utilizam Apenas Rádio (12)**

```
Atlanet Telecomunicacoes Ltda
DIRECTNET PRESTACAO DE SERVICOS LTDA
Global Web Master Ltda
HIT TELECOMUNICACOES LTDA.
I T S - COMERCIO DE PECAS E EQUIPAMENTOS LTDA. - EPP
LEOMAX TELECOM LTDA
MEC SOLUTION LTDA
NETWALK TELECOMUNICACOES EM INFORMATICA LTDA-ME
Rss Comunicacao Ltda
SPACE NET REDES DE INTERNET EIRELI
TMC - TECNOLOGIA EM TELECOMUNICACOES LTDA
URSOFT TELECOM LTDA
```

🔄 **Prestadoras que Utilizam Ambos os Meios (8)**

```
ALFA NETWORK SOLUTIONS INFORMÁTICA LTDA - ME
ATTUS TECNOLOGIA EM TELECOMUNICACOES EIRELI
CLARO S.A.
FENIX INTERNET COMUNICACOES EIRELI
Ozonio Telecomunicacoes Ltda
TIM S A
VOGEL SOLUCOES EM TELECOMUNICACOES E INFORMATICA S.A.
WIRELESS COMM SERVICES LTDA
```

📊 RESUMO ESTATÍSTICO:
   • Apenas Fibra: 69 (76.7%)
   • Apenas Rádio: 12 (13.3%)
   • Ambos os meios: 8 (8.9%)
================================================================================
```

---

## 🔧 Personalização

1. **Outro município:** `python analise.py -m "Campinas"`
2. **Todos os municípios:** `python analise.py`
3. **Atualizar dataset:** basta substituir o arquivo CSV mantendo o mesmo formato de colunas.

---

## 📜 Licença

Uso livre para fins educativos e análises não-comerciais.

---

**Autor:** Liriel Castro – 2025

---

> Gerado automaticamente pelo script `analise.py` após a última execução. 
