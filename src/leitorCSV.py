import pandas as pd
from src.envioEmail import send_email
from src.gerarPDF import generate_pdf, generate_pie_charts
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

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

        most_common_author = self.data['Autor'].value_counts().idxmax()
        most_common_author_count = self.data['Autor'].value_counts().max()

        all_tags = self.data['Tags'].explode()
        most_common_tag = all_tags.value_counts().idxmax()
        most_common_tag_count = all_tags.value_counts().max()

        analysis_results = (
            f"Total de citações: {total_quotes}\n"
            f"Autor mais recorrente: {most_common_author} ({most_common_author_count} citações)\n"
            f"Tag mais utilizada: {most_common_tag} ({most_common_tag_count} ocorrências)\n"
        )

        authors_data = self.data['Autor'].value_counts().to_dict()
        tags_data = all_tags.value_counts().to_dict()

        return analysis_results, authors_data, tags_data

def run_analysis():
    filename = "citacoes.csv"
    analyzer = CSVAnalyzer(filename)

    analyzer.load_data()
    results_text, authors_data, tags_data = analyzer.analyze_data()

    author_chart_path, tag_chart_path = generate_pie_charts(authors_data, tags_data)

    pdf_filename = "resultado_analise.pdf"
    generate_pdf(results_text, author_chart_path, tag_chart_path, pdf_filename)

    print(results_text)
    
    sender_email = EMAIL_USER
    sender_password = EMAIL_PASS
    recipient_email = "bielchaves2000@hotmail.com"  
    subject = "Análise de Citações"
    body = results_text
    attachment_paths = [pdf_filename , filename]

    send_email(sender_email, sender_password, recipient_email, subject, body, attachment_paths)
