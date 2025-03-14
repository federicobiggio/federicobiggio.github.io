import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import colorsys
from datetime import datetime
import calendar

# Carica i dati da un file CSV
df = pd.read_csv('wired_data.csv', sep=';')

# Converti le colonne 'saturation_stdev', 'year', e 'month' in numeri, gestendo eventuali errori
df['saturation_stdev'] = pd.to_numeric(df['saturation_stdev'], errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Mappa i nomi dei mesi a numeri utilizzando il modulo calendar
df['month'] = df['month'].apply(lambda x: list(calendar.month_name).index(x) if x in calendar.month_name else None)

# Crea una lista di colori RGB basati su hue_median
colors = [colorsys.hsv_to_rgb(hue_median / 360, 1, 1) for hue_median in df['hue_median']]

# Crea il diagramma a dispersione con colori basati su hue_median e immagini
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(pd.to_datetime(df[['year', 'month']].assign(day=1)), df['saturation_stdev'], c=colors, alpha=0.5)
ax.set_title('Relazione tra tempo e saturation_stdev')
ax.set_xlabel('Tempo')
ax.set_ylabel('saturation_stdev')

# Aggiungi le immagini come OffsetImage
for i, (tempo, saturation_stdev, filename) in enumerate(zip(pd.to_datetime(df[['year', 'month']].assign(day=1)), df['saturation_stdev'], df['filename'])):
    img = plt.imread(f'wired_cover_crop/{filename}')
    imagebox = OffsetImage(img, zoom=0.05)
    ab = AnnotationBbox(imagebox, (tempo, saturation_stdev), frameon=False, pad=0)
    ax.add_artist(ab)

plt.grid(False)
plt.show()
