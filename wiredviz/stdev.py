import cv2
import numpy as np
import os
import pandas as pd

def calculate_hue_stdev(image_path):
    # Leggi l'immagine utilizzando OpenCV
    img = cv2.imread(image_path)

    # Converti l'immagine da BGR a HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Estrai il canale di tonalità
    hue_channel = hsv_img[:, :, 0]

    # Calcola la deviazione standard della tonalità
    hue_stdev = np.std(hue_channel)

    return hue_stdev

def process_images(folder_path, output_csv):
    # Otteni la lista di file nella cartella
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

    # Creare un DataFrame vuoto
    df = pd.DataFrame(columns=['filename', 'hue_stdev'])

    # Calcola la deviazione standard per ogni immagine
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        hue_stdev = calculate_hue_stdev(image_path)
        print(f"Deviazione standard della tonalità per {image_file}: {hue_stdev}")

        # Aggiungi il risultato al DataFrame
        df = df.append({'filename': image_file, 'hue_stdev': hue_stdev}, ignore_index=True)

    # Leggi il file CSV esistente
    existing_df = pd.read_csv(output_csv, sep=';')

    # Unisci i due DataFrame in base alla colonna 'filename'
    merged_df = existing_df.merge(df, on='filename', how='left')

    # Salva il DataFrame risultante nel file CSV esistente
    merged_df.to_csv(output_csv, index=False, sep=';')

# Sostituisci 'path_to_your_folder' con il percorso effettivo della tua cartella di immagini
folder_path = 'wired_cover_crop'
output_csv = 'wired_dataT.csv'
process_images(folder_path, output_csv)
