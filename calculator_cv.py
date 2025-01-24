import pandas as pd
import numpy as np
'''

Reference => # https://datatab.net/tutorial/fleiss-kappa 

'''
# Define the file paths for annotator data
data_directory = "annotations/"
file_names = ["cv_aryan.csv", "cv_parthiv.csv", "cv_praneet.csv"]

# Read the data for each annotator
df_aryan = pd.read_csv(data_directory + file_names[0])
df_parthiv = pd.read_csv(data_directory + file_names[1])
df_praneet = pd.read_csv(data_directory + file_names[2])

# Function to convert the "choice" column ('Not trucks' to 0, 'Trucks' to 1)
def convert_choices(df):
    return np.where(df["choice"] == 'Not trucks', 0, 1)

# Apply the conversion function for each annotator
choices_aryan = convert_choices(df_aryan)
choices_parthiv = convert_choices(df_parthiv)
choices_praneet = convert_choices(df_praneet)

# Create a DataFrame with choices for each annotator and the image names
annotations = pd.DataFrame({
    'image': df_aryan["image"],
    'aryan': choices_aryan,
    'parthiv': choices_parthiv,
    'praneet': choices_praneet
})

# Calculate the count of "Trucks" and "Not trucks" for each image (row)
annotations["Trucks"] = annotations["aryan"] + annotations["parthiv"] + annotations["praneet"]
annotations["Not trucks"] = (1 - annotations["aryan"]) + (1 - annotations["parthiv"]) + (1 - annotations["praneet"])

# Number of annotators and total number of items
num_annotators = 3
num_samples = len(annotations)

# Calculate expected proportion (P_e)
P_e = ((annotations["Trucks"].sum() / (num_annotators * num_samples)))**2 + \
      ((annotations["Not trucks"].sum() / (num_annotators * num_samples)))**2

print(f"\nThe P_e: {P_e:.2f}\n")
# Calculate the observed proportion (P_o)
component_p_o = 0
for i in range(num_samples):
    component_p_o += annotations["Trucks"][i]**2 + annotations["Not trucks"][i]**2

P_o = (1 / (num_samples * (num_annotators - 1) * num_annotators)) * (component_p_o - num_annotators * num_samples)

# Print the observed proportion (P_o)
print(f"The observed proportion (P_o) is {P_o}\n")

# Calculate Fleiss' Kappa
fleiss_kappa_score = (P_o - P_e) / (1 - P_e)
print(f"\tFleiss' Kappa: {fleiss_kappa_score:.3f}")

'''
ANSWER/OUTPUT => 

The P_e: 0.50

The observed proportion (P_o) is 0.9

        Fleiss' Kappa: 0.800

'''