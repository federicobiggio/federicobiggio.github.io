from colorthief import ColorThief
import os
import pandas as pd
from sklearn.cluster import KMeans
import colorsys

# Funzione per calcolare la hue_median di un'immagine usando K-Means
def calculate_hue_median(image_path, num_clusters=5):
    color_thief = ColorThief(image_path)
    # Estrai tutti i pixel dell'immagine
    pixels = color_thief.image.getdata()
    
    # Esegui il clustering K-Means sui pixel
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(pixels)
    
    # Ottieni il colore dominante del cluster più grande
    dominant_color = max(set(kmeans.labels_), key=list(kmeans.labels_).count)
    
    # Converti il colore dominante nel formato (r, g, b)
    centroid_rgb = kmeans.cluster_centers_[dominant_color]
    
    # Calcola la componente Hue del colore dominante utilizzando colorsys
    hue_median = colorsys.rgb_to_hsv(centroid_rgb[0]/255, centroid_rgb[1]/255, centroid_rgb[2]/255)[0] * 360
    
    return hue_median

# Cartella contenente le immagini
image_folder = "wired_cover_crop"

# File CSV esistente
csv_file = 'wired_data.csv'

# Carica il DataFrame esistente
df = pd.read_csv(csv_file, sep=';')

# Calcola la hue_median usando K-Means per tutte le immagini
df['hue_median'] = [calculate_hue_median(os.path.join(image_folder, filename)) for filename in df['filename']]

# Salva il DataFrame aggiornato nel file CSV esistente
df.to_csv(csv_file, sep=';', index=False)

print("Calcolo della hue_median con K-Means completato e i risultati sono stati aggiunti al file CSV.")
