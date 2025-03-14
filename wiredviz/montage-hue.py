import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carica i dati dal file CSV
file_path = 'wired_data.csv'
data = pd.read_csv(file_path, delimiter=';')

# Crea una mappa di colori
cmap = sns.color_palette("husl", as_cmap=True)

# Crea un istogramma con colori basati sulla tonalità
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(data['hue_median'], bins=40)

# Assegna colori specifici a ciascun bin
for i in range(len(patches)):
    color = cmap(bins[i] / 360)  # Normalizza la tonalità tra 0 e 1
    patches[i].set_facecolor(color)

# Personalizza il grafico
plt.title('Distribuzione delle Tonalità Dominanti')
plt.xlabel('')
plt.ylabel('')


# Aggiungi una barra di colore
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=360))
sm.set_array([])  # necessario per evitare un'eccezione
cbar = plt.colorbar(sm, label='Tonalità (gradi)')

# Mostra il grafico
plt.show()
