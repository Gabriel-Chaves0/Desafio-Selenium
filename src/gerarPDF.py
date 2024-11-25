import matplotlib.pyplot as plt
from fpdf import FPDF

def generate_pie_charts(authors_data, tags_data):
    
    authors, author_counts = zip(*authors_data.items())
    plt.figure(figsize=(5, 5))  
    plt.pie(author_counts, labels=authors, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.title("Distribuição de Citações por Autor")
    author_chart_path = "author_chart.png"
    plt.savefig(author_chart_path)
    plt.close()

    tags, tag_counts = zip(*tags_data.items())
    plt.figure(figsize=(5, 5))  
    plt.pie(tag_counts, labels=tags, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
    plt.title("Distribuição de Tags Utilizadas")
    tag_chart_path = "tag_chart.png"
    plt.savefig(tag_chart_path)
    plt.close()

    return author_chart_path, tag_chart_path

def generate_pdf(results_text, author_chart_path, tag_chart_path, output_pdf):
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=18, style="B")  # Fonte maior e em negrito
    pdf.cell(0, 20, "Análise de Citações e Tags", ln=True, align="C")  # Texto centralizado
    pdf.ln(10) 

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, results_text)

    pdf.image(author_chart_path, x=10, y=70, w=90)  
    pdf.image(tag_chart_path, x=110, y=70, w=90) 
    

    pdf.output(output_pdf)
    print(f"PDF gerado com sucesso: {output_pdf}")

