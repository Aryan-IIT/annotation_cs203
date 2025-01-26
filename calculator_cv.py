import pandas as pd
import numpy as np
'''

Reference => # https://datatab.net/tutorial/fleiss-kappa 

'''

data_directory = "annotations/"
file_names = ["cv_aryan.csv", "cv_parthiv.csv", "cv_praneet.csv"]

df_aryan = pd.read_csv(data_directory + file_names[0])
df_parthiv = pd.read_csv(data_directory + file_names[1])
df_praneet = pd.read_csv(data_directory + file_names[2])

#to convert the "choice" column ('Not trucks' to 0, 'Trucks' to 1)
def convert_choices(df):
    return np.where(df["choice"] == 'Not trucks', 0, 1)

# Apply the conversion function for each annotator
choices_aryan = convert_choices(df_aryan)
choices_parthiv = convert_choices(df_parthiv)
choices_praneet = convert_choices(df_praneet)

annotations = pd.DataFrame({
    'image': df_aryan["image"],
    'aryan': choices_aryan,
    'parthiv': choices_parthiv,
    'praneet': choices_praneet
})

annotations["Trucks"] = annotations["aryan"] + annotations["parthiv"] + annotations["praneet"]
annotations["Not trucks"] = (1 - annotations["aryan"]) + (1 - annotations["parthiv"]) + (1 - annotations["praneet"])

num_annotators = 3
num_samples = len(annotations)

#expected proportion (P_e)
P_e = ((annotations["Trucks"].sum() / (num_annotators * num_samples)))**2 + ((annotations["Not trucks"].sum() / (num_annotators * num_samples)))**2

print(f"\nThe P_e: {P_e:.2f}\n")

#observed proportion (P_o) using intermediate component 
component_p_o = 0
for i in range(num_samples):
    component_p_o += annotations["Trucks"][i]**2 + annotations["Not trucks"][i]**2

P_o = (1 / (num_samples * (num_annotators - 1) * num_annotators)) * (component_p_o - num_annotators * num_samples)

#observed proportion (P_o)
print(f"The observed proportion (P_o) is {P_o}\n")

#Fleiss' Kappa
fleiss_kappa_score = (P_o - P_e) / (1 - P_e)
print(f"\tFleiss' Kappa: {fleiss_kappa_score:.3f}")

'''
ANSWER/OUTPUT => 

The P_e: 0.50

The observed proportion (P_o) is 0.9

        Fleiss' Kappa: 0.800

        
Interpretation => 
Fleiss Kappa of 0.800 indicates a high level of agreement among the three annotators, as it is 
closer to 1 (perfect agreement). The observed proportion (P_o) of 0.9 suggests that, on average, 
annotators agree 90% of the time. The expected proportion (P_e) of 0.50 reflects the likelihood of agreement 
occurring by chance, and the significant difference between P_o and P_e highlights the substantial agreement 
beyond random chance.

'''