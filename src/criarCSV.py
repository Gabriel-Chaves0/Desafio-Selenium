import csv

def CriarCSV(quotes_data):
    with open('citacoes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        colunas = ['Citação', 'Autor', 'Tags']
        writer = csv.DictWriter(csvfile, fieldnames=colunas, delimiter=';') 

        writer.writeheader()

        for quote in quotes_data:
            writer.writerow(quote)
