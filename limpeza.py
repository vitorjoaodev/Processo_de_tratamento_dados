#Processo de ETL e análise exploratória para tratamento de dados brutos camadas Bronze (RAW) e Silver
import pandas as pd

try:
    # 1️⃣ Ler o arquivo CSV
    df = pd.read_csv("dados.csv")

    # 2️⃣ Remover duplicados
    df = df.drop_duplicates()

    # 3️⃣ Tratar dados ausentes
    # Remove linhas onde valor ou data estão ausentes
    df = df.dropna(subset=["data", "valor"])

    # 4️⃣ Converter coluna valor para float
    df["valor"] = df["valor"].astype(float)

    # 5️⃣ Converter data para datetime
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    # Remove datas inválidas (caso existam)
    df = df.dropna(subset=["data"])

    # 6️⃣ Criar coluna ano_mes no formato YYYY-MM
    df["ano_mes"] = df["data"].dt.to_period("M").astype(str)

    # 7️⃣ Criar coluna valor_com_imposto (15%)
    df["valor_com_imposto"] = df["valor"] * 1.15

    print("Transformação concluída com sucesso!")
    print(df)

except FileNotFoundError:
    print("Erro: arquivo CSV não encontrado.")

except Exception as e:
    print(f"Erro inesperado: {e}")
