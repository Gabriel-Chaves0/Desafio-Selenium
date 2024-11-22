import pandas as pd

class CSVAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.filename, delimiter=';', encoding='utf-8')
        self.data['Tags'] = self.data['Tags'].str.split(", ")

    def analyze_data(self):
        if self.data is None:
            print("Os dados não foram carregados. Use 'load_data()' antes de realizar análises.")
            return

        total_quotes = len(self.data)
        print(f"Total de citações: {total_quotes}")

        most_common_author = self.data['Autor'].value_counts().idxmax()
        most_common_author_count = self.data['Autor'].value_counts().max()
        print(f"Autor mais recorrente: {most_common_author} ({most_common_author_count} citações)")

        all_tags = self.data['Tags'].explode() #Função explode() é usada para dividir listas em linhas
        most_common_tag = all_tags.value_counts().idxmax()
        most_common_tag_count = all_tags.value_counts().max()
        print(f"Tag mais utilizada: {most_common_tag} ({most_common_tag_count} ocorrências)")

def main():
    filename = 'citacoes.csv'
    analyzer = CSVAnalyzer(filename)

    analyzer.load_data()
    analyzer.analyze_data()

main()
