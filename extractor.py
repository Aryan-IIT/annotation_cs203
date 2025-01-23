import pandas as pd
import os
import requests
from io import BytesIO
from PIL import Image

#Read the CSV file
csv_file = pd.read_csv('NLP_POS_sentences.csv')

#Define start and end indices for team 19 (0-indexed)
team_number = 19
samples_per_team = 20

start = (team_number - 1) * samples_per_team  #start index
end = start + samples_per_team - 1           #end index (inclusive)

print(f"Start index: {start}, End index: {end}")

#relevant rows for team 19
team_19_data = csv_file.iloc[start:end + 1]

#Save the filtered data to a new CSV file
edited_csv_path = 'NLP_POS_sentences_edited.csv'
team_19_data.to_csv(edited_csv_path, index=False)
print(f"Filtered CSV saved to {edited_csv_path}")

#Create a folder for saving images
output_folder = "CV_edited"
os.makedirs(output_folder, exist_ok=True)

#Images are manually downloaded due to auth issues with drive. 