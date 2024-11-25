"""
Este script executa todos os processos necessários do projeto, incluindo:
1. Execução do script principal (run_script).
2. Execução da análise do CSV (run_analysis).
"""

from src.script import run_script
from src.leitorCSV import run_analysis

def main():
    print("Iniciando o processo completo...")
    
    print("\nExecutando o script principal...")
    run_script()

    print("\nExecutando a análise do CSV...")
    run_analysis()
    
    print("\nProcesso completo finalizado com sucesso!")


main()
