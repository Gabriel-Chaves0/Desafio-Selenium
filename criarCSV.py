import csv

def CriarCSV(quotes_data):
    with open('citacoes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Define os nomes das colunas
        colunas = ['Citação', 'Autor', 'Tags']
        writer = csv.DictWriter(csvfile, fieldnames=colunas, delimiter=';') 

        # Escreve o cabeçalho no CSV
        writer.writeheader()

        # Escreve cada linha de dados no CSV
        for quote in quotes_data:
            writer.writerow(quote)
