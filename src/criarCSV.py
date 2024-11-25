import pandas as pd

def CriarCSV(quotes_data):
    df = pd.DataFrame(quotes_data)

    filepath = "citacoes.csv"
    df.to_csv(filepath, index=False, sep=";", encoding="utf-8")

    print(f"CSV criado em: {filepath}")
