#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Prestadoras de Backhaul - São José dos Campos
======================================================

Este script analisa os dados de prestadoras de serviços de backhaul
em São José dos Campos, categorizando-as por meio de transporte utilizado.

Autor: Análise de Dados
Data: 2024
"""

import csv
import argparse  
from collections import defaultdict
from typing import Dict, Set, List, Tuple
from dataclasses import dataclass
from pathlib import Path


@dataclass
class RegistroBackhaul:
    """Representa um registro de backhaul do dataset."""
    ano: int
    municipio: str
    uf: str
    codigo_ibge: str
    prestadora: str
    cnpj: str
    meio_transporte: str


class AnalisadorBackhaul:
    """Classe responsável pela análise dos dados de backhaul."""
    
    def __init__(self, municipio: str | None = None):
       
        self.municipio: str | None = municipio

        self.dados: List[RegistroBackhaul] = []
        self.prestadoras_meios: Dict[str, Set[str]] = defaultdict(set)
    
    def carregar_dados_string(self, dados_raw: str) -> None:
        """Carrega dados a partir de uma string formatada."""
        linhas = dados_raw.strip().split('\n')
        
        for linha in linhas:
            if not linha.strip():
                continue
                
            partes = linha.split(';')
            if len(partes) == 7:
                registro = RegistroBackhaul(
                    ano=int(partes[0]),
                    municipio=partes[1].strip(),
                    uf=partes[2].strip(),
                    codigo_ibge=partes[3].strip(),
                    prestadora=partes[4].strip(),
                    cnpj=partes[5].strip(),
                    meio_transporte=partes[6].strip()
                )
                self.dados.append(registro)
                self.prestadoras_meios[registro.prestadora].add(registro.meio_transporte)
    
    def carregar_dados_csv(self, caminho_arquivo: str, municipio_filtro: str | None = None) -> None:
        """Carrega dados a partir de um arquivo CSV."""
        try:
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            
            for encoding in encodings:
                try:
                    with open(caminho_arquivo, 'r', encoding=encoding) as arquivo:
                        leitor = csv.DictReader(arquivo, delimiter=';')
                        
                        fieldnames = leitor.fieldnames
                        print(f"📋 Cabeçalhos encontrados: {fieldnames}")
                        
                        if fieldnames and fieldnames[0].startswith('\ufeff'):
                            fieldnames[0] = fieldnames[0].replace('\ufeff', '')
                            leitor.fieldnames = fieldnames
                        
                        for linha in leitor:
                            linha_limpa = {}
                            for chave, valor in linha.items():
                                chave_limpa = chave.replace('\ufeff', '') if chave else chave
                                linha_limpa[chave_limpa] = valor
                            
                            if municipio_filtro and linha_limpa.get('Município', '').strip() != municipio_filtro:
                                continue
                            
                            registro = RegistroBackhaul(
                                ano=int(linha_limpa['Ano']),
                                municipio=linha_limpa['Município'].strip(),
                                uf=linha_limpa['UF'].strip(),
                                codigo_ibge=linha_limpa['Código IBGE'].strip(),
                                prestadora=linha_limpa['Prestadora'].strip(),
                                cnpj=linha_limpa['CNPJ'].strip(),
                                meio_transporte=linha_limpa['Meio Transporte'].strip()
                            )
                            self.dados.append(registro)
                            self.prestadoras_meios[registro.prestadora].add(registro.meio_transporte)
                        
                        print(f"✅ Arquivo carregado com encoding: {encoding}")
                        print(f"📊 Total de registros carregados: {len(self.dados)}")
                        break
                        
                except UnicodeDecodeError:
                    continue
                except Exception as e:
                    print(f"❌ Erro com encoding {encoding}: {e}")
                    continue
            else:
                print("❌ Não foi possível carregar o arquivo com nenhum encoding testado")
        
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
        except Exception as e:
            print(f"❌ Erro ao carregar arquivo: {e}")
    
    def categorizar_prestadoras(self) -> Tuple[List[str], List[str], List[str]]:
        """Categoriza prestadoras por meio de transporte utilizado."""
        apenas_fibra = []
        apenas_radio = []
        ambos = []
        
        for prestadora, meios in self.prestadoras_meios.items():
            usa_fibra = "Fibra" in meios
            usa_radio = "Rádio" in meios
            
            if usa_fibra and usa_radio:
                ambos.append(prestadora)
            elif usa_fibra:
                apenas_fibra.append(prestadora)
            elif usa_radio:
                apenas_radio.append(prestadora)
        
        return (sorted(apenas_fibra), sorted(apenas_radio), sorted(ambos))
    
    def gerar_relatorio(self) -> str:
        """Gera um relatório formatado da análise."""
        apenas_fibra, apenas_radio, ambos = self.categorizar_prestadoras()
        
        relatorio = []
        relatorio.append("=" * 80)

        titulo_municipio = self.municipio if self.municipio else "TODOS OS MUNICÍPIOS"
        relatorio.append(f"📊 ANÁLISE DE PRESTADORAS DE BACKHAUL - {titulo_municipio.upper()}")
        relatorio.append("=" * 80)
        
        relatorio.append(f"\n📈 ESTATÍSTICAS GERAIS:")
        relatorio.append(f"   • Total de registros analisados: {len(self.dados)}")
        relatorio.append(f"   • Total de prestadoras únicas: {len(self.prestadoras_meios)}")
        relatorio.append(f"   • Período analisado: {min(r.ano for r in self.dados)} - {max(r.ano for r in self.dados)}")
        
        relatorio.append(f"\n🔵 PRESTADORAS QUE UTILIZAM APENAS FIBRA ({len(apenas_fibra)}):")
        if apenas_fibra:
            for prestadora in apenas_fibra:
                relatorio.append(f"   • {prestadora}")
        else:
            relatorio.append("   Nenhuma prestadora encontrada.")
        
        relatorio.append(f"\n📡 PRESTADORAS QUE UTILIZAM APENAS RÁDIO ({len(apenas_radio)}):")
        if apenas_radio:
            for prestadora in apenas_radio:
                relatorio.append(f"   • {prestadora}")
        else:
            relatorio.append("   Nenhuma prestadora encontrada.")
        
        relatorio.append(f"\n🔄 PRESTADORAS QUE UTILIZAM AMBOS OS MEIOS ({len(ambos)}):")
        if ambos:
            for prestadora in ambos:
                relatorio.append(f"   • {prestadora}")
        else:
            relatorio.append("   Nenhuma prestadora encontrada.")
        
        
        relatorio.append(f"\n📊 RESUMO ESTATÍSTICO:")
        relatorio.append(f"   • Apenas Fibra: {len(apenas_fibra)} ({len(apenas_fibra)/len(self.prestadoras_meios)*100:.1f}%)")
        relatorio.append(f"   • Apenas Rádio: {len(apenas_radio)} ({len(apenas_radio)/len(self.prestadoras_meios)*100:.1f}%)")
        relatorio.append(f"   • Ambos os meios: {len(ambos)} ({len(ambos)/len(self.prestadoras_meios)*100:.1f}%)")
        
        relatorio.append("\n" + "=" * 80)
        
        return "\n".join(relatorio)
    
    def salvar_relatorio(self, caminho_arquivo: str) -> None:
        """Salva o relatório em um arquivo."""
        relatorio = self.gerar_relatorio()
        
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(relatorio)
            print(f"✅ Relatório salvo em: {caminho_arquivo}")
        except Exception as e:
            print(f"❌ Erro ao salvar relatório: {e}")


def main():
    """Função principal do script."""
    parser = argparse.ArgumentParser(description="Análisa dados de prestadoras de backhaul por município")
    parser.add_argument("--municipio", "-m", help="Nome do município para filtrar (ex.: 'São Paulo'). Se omitido, analisa todos.", default="São José dos Campos")
    args = parser.parse_args()

    analisador = AnalisadorBackhaul(args.municipio)

    print(f"🔄 Carregando dados do arquivo original para o município: {args.municipio or 'TODOS'} ...")

    dataset_path = Path(__file__).parent / "backhaul_municipios_2023-2024.csv"
    analisador.carregar_dados_csv(str(dataset_path), args.municipio)
    
    if not analisador.dados:
        print("❌ Nenhum dado foi carregado. Verifique se o arquivo existe e contém dados para São José dos Campos.")
        return
    
    print("📊 Gerando relatório de análise...")
    relatorio = analisador.gerar_relatorio()
    print(relatorio)
    
    # Nome de arquivo de relatório dinâmico
    safe_name = (args.municipio or "todos").lower()
    for char in "ãáàâêéèôóòçíìúùü" :
        safe_name = safe_name.replace(char, {
            'ã':'a','á':'a','à':'a','â':'a',
            'ê':'e','é':'e','è':'e',
            'ô':'o','ó':'o','ò':'o',
            'ç':'c',
            'í':'i','ì':'i',
            'ú':'u','ù':'u','ü':'u',
        }[char])
    safe_name = safe_name.replace(' ', '_')

    caminho_relatorio = Path(__file__).parent / f"relatorio_{safe_name}_backhaul.txt"
    analisador.salvar_relatorio(str(caminho_relatorio))


if __name__ == "__main__":
    main()
