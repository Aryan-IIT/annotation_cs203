# Annotation_CS203 - Team 19  

### Annotations  

All annotations are exported in CSV format and created using **Label Studio**. These files are located in the `annotations` folder:  

- **[NLP 1 Annotation](/annotations/nlp_parthiv.csv)**: Sentence annotations by Parthiv (Team 19).  
- **[NLP 2 Annotation](annotations/nlp_aryan.csv)**: Sentence annotations by Aryan (Team 19).  
- **[CV 1 Annotation - Parthiv](annotations/cv_parthiv.csv)**: Truck/No Truck image annotations by Parthiv (Team 19).  
- **[CV 1 Annotation - Aryan](annotations/cv_aryan.csv)**: Truck/No Truck image annotations by Aryan (Team 19).  
- **[CV 1 Annotation - Praneet](annotations/cv_praneet.csv)**: Truck/No Truck image annotations by Praneet (Other).  

---

### Python Files  

- **[Extractor](extractor.py)**: Builds the NLP dataset from the provided data for Label Studio.  
- **[CV Dataset Processes - Fleiss Kappa](calculator_cv.py)**: Calculates Fleiss' Kappa for the image dataset annotations.  
- **[NLP Dataset Processes - Cohen's Kappa](calculator_nlp.ipynb)**: Calculates Cohen's Kappa for the language dataset annotations.  

---

### Requirements  

Install the required dependencies using the [requirements file](requirements.txt):  
```bash
pip install -r requirements.txt
```
---

### Note 

Please read [User History](user_history.txt) for more information on task 1. 
The pdf of images, and images of the history are put in this [file](Task_1_Enivronment_setup.pdf).
