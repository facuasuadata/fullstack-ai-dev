# Repaso clase 1

* Seguir al profe en IG: https://www.instagram.com/mct.esteban.calabria/

* Seguir a Abel https://www.instagram.com/orion.technologies/
Experto en AWS

# Python en clase 
* Primer saludo
* Matplotlib
https://colab.research.google.com/drive/1IJTDVL-wuzRMZ91z-y7SbhopquLARnk7#scrollTo=cHAzDurN57ca

# Distintas librerias de python que usaremos
* Las Liberias
https://www.instagram.com/p/DPmewyVjs88/?img_index=1
* Lo mas importante ahora que esta la IA
* DE IA y análisis de datos
Aprendizaje automático (Sckit-learn)
Pandas
MatPlotLib
https://matplotlib.org/
Gradio
* Web
Framework Django
Matraz
FastAPI (El nodejs/express de Python)
solicitudes
Automatizaciones 
* De oficina
* Tkinter
* Juegos
Pygame
* Optimización
numpy
* Móvil 
Kivy
* Pruebas
Pytest

# Pyton y los LLM
Los llm tipo Claude, ChatGPT, Qwen tienen un intérprete de python y le podes pedir a la IA que para resolverte un rápido ejecutar código en python y te muestre el resultado
Tienen como un google colab incorporado
Interpretar código en ChatGPT

# ChatGPT
Utiliza matplotlib para mostrarme un grafico de torta que muestre la poblacion de las 10 provincias mas pobladas de argentina, usando edeitor de codigo
Hizo ese grafico

<img width="869" height="735" alt="image" src="https://github.com/user-attachments/assets/3a9f636d-07b1-4364-8cc9-2a2bd06d8815" />

y este codigo

import matplotlib.pyplot as plt

# Población aproximada de las 10 provincias más pobladas de Argentina
provincias = [
    "Buenos Aires", "Córdoba", "Santa Fe", "Mendoza", "Tucumán",
    "Entre Ríos", "Salta", "Misiones", "Chaco", "Corrientes"
]

poblacion = [
    17569000, 3970000, 3556000, 2020000, 1730000,
    1426000, 1421000, 1278000, 1216000, 1197000
]

plt.figure(figsize=(9, 9))
plt.pie(
    poblacion,
    labels=provincias,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Población de las 10 provincias más pobladas de Argentina")
plt.axis("equal")
plt.show()

# Claude
Quiero que uses el interprete de codigo para generarme un grafico de lineas en matplotlib
donde se muestre el valor de la accion de nvidia y msft en un mismo grafico, me devuelvas el codigo y el grafico

Grafico 
<img width="1650" height="900" alt="nvda_vs_msft" src="https://github.com/user-attachments/assets/f1a9d8b3-9107-4055-a718-c6f8374bdfdc" />

* Codigo

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Precios de cierre diarios reales (fuente: MarketBeat, últimos ~22 días hábiles hasta el 07/08/2026)
fechas_str = [
    "07/09/2026", "07/10/2026", "07/13/2026", "07/14/2026", "07/15/2026",
    "07/16/2026", "07/17/2026", "07/20/2026", "07/21/2026", "07/22/2026",
    "07/23/2026", "07/24/2026", "07/27/2026", "07/28/2026", "07/29/2026",
    "07/30/2026", "07/31/2026", "08/03/2026", "08/04/2026", "08/05/2026",
    "08/06/2026", "08/07/2026",
]
fechas = [datetime.strptime(f, "%m/%d/%Y") for f in fechas_str]

nvda = [202.78, 210.96, 203.69, 211.80, 212.50, 207.40, 202.81, 203.28, 207.29,
        212.06, 208.76, 206.84, 196.51, 197.01, 190.01, 195.04, 200.75, 206.64,
        211.94, 219.22, 218.78, 223.96]

msft = [384.36, 385.10, 390.99, 384.93, 395.63, 401.10, 393.82, 402.29, 397.75,
        390.34, 381.58, 381.70, 389.10, 393.35, 390.54, 451.10, 464.72, 487.65,
        492.81, 487.46, 499.86, 499.99]

fig, ax = plt.subplots(figsize=(11, 6))

ax.plot(fechas, nvda, marker="o", linewidth=2, color="#76B900", label="NVIDIA (NVDA)")
ax.plot(fechas, msft, marker="o", linewidth=2, color="#00A4EF", label="Microsoft (MSFT)")

ax.set_title("Precio de cierre: NVIDIA (NVDA) vs Microsoft (MSFT)\nÚltimo mes (09 jul – 07 ago 2026)",
              fontsize=13, fontweight="bold")
ax.set_xlabel("Fecha")
ax.set_ylabel("Precio de cierre (USD)")
ax.legend(loc="upper left", fontsize=10)
ax.grid(True, alpha=0.3)

ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%b"))
fig.autofmt_xdate(rotation=45)

plt.tight_layout()
plt.savefig("nvda_vs_msft.png", dpi=150)
print("listo")


# Qwen

Quiero que uses el interprete de codigo para generarme un grafico de lineas en 
matplotlib donde se muestre el valor de la accion de nvidia y msft en un mismo grafico, me devuelvas el codigo y el grafico

Grafico
<img width="1189" height="590" alt="1786534657" src="https://github.com/user-attachments/assets/1b81022b-9bf6-42d9-93cb-925a7ff1d4ca" />

Codigo(me hizo importar galeria finance, claude no)
import yfinance as yf
import matplotlib.pyplot as plt

# Descargar datos de los últimos 6 meses
nvda = yf.Ticker("NVDA")
msft = yf.Ticker("MSFT")

nvda_hist = nvda.history(period="6mo")
msft_hist = msft.history(period="6mo")

# Crear el gráfico
plt.figure(figsize=(12, 6))
plt.plot(nvda_hist.index, nvda_hist['Close'], label='NVIDIA (NVDA)', color='#76b900', linewidth=2)
plt.plot(msft_hist.index, msft_hist['Close'], label='Microsoft (MSFT)', color='#00a4ef', linewidth=2)

# Personalización
plt.title('Evolución del precio de NVIDIA vs Microsoft (Últimos 6 meses)', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Precio de Cierre (USD)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Mostrar gráfico
plt.show()


# GITHUB

* Creeamos repo
* Verificar si teniamos el comando git instalado
* Crear una carpeta localmente para bajar una copia del repositorio
* Bajar el repositorio de moto localmente
* Crear subcarpeta clase02
* bajamos el notebook de python del colab y lo copiamos a esa carpeta
* Agregar los archivos a un repositorio local (no lo subimos a internet todavia)
* Parados en la carpeta raíz del repositorio
  >git add *
  >git commit -m "Mi primer commit"

* ver la lista
  git log

* Subir todo a internet (Al repositorio remoto, a github)
  > git push

* Vemos si se realizaron los cambios

# Aportes
* Prompt de Guido
Ver prompt
  




