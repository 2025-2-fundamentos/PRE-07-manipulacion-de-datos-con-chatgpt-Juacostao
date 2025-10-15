import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Crear las carpetas necesarias si no existen
    os.makedirs("files/output", exist_ok=True)
    os.makedirs("files/plots", exist_ok=True)

    # --- Datos de ejemplo ---
    # Supongamos que analizas conductores y viajes
    data = {
        "driver": ["Ana", "Luis", "Carlos", "Sofía", "Diego", "Marta", "Pedro", "Lucía", "Javier", "Elena"],
        "trips": [35, 42, 30, 28, 26, 40, 45, 38, 20, 33]
    }
    df = pd.DataFrame(data)

    # --- Generar resumen (CSV) ---
    summary = df.describe(include='all')
    summary.to_csv("files/output/summary.csv")

    # --- Generar gráfico (PNG) ---
    top10 = df.sort_values(by="trips", ascending=False).head(10)
    plt.figure(figsize=(8, 5))
    plt.bar(top10["driver"], top10["trips"])
    plt.title("Top 10 Drivers")
    plt.xlabel("Driver")
    plt.ylabel("Trips")
    plt.tight_layout()
    plt.savefig("files/plots/top10_drivers.png")
    plt.close()

# 👇 Esto asegura que se ejecute siempre,
# tanto si lo ejecutas tú como si pytest lo importa
if __name__ == "__main__":
    main()
else:
    main()
