# CS-282-Final-Project
goal: interpretable visual framework for IRL models

## Directory Break-down
### /AIRL 
Attempt at implement AIRL (in progress)
### /data_pipeline
1. (playground.ipynb) First, we are only looking at ICD 9 codes in the non-ICU (hospital) setting, since they are more broad (more data to work with). Within that scope, we are only looking at patients with pneunomia (ICD9: 486) and hyperxemia (ICD9: 79902), two of the more frequently diagnosed diseases that would require immediate treatment.

2. After extracting the patients with only the diseases of interest, we merged the subject id, ICD code, and ICD English description with the lab events corresponding to each patient. In addition, we added an additional column that reflects the age of each patient to create a masterlist of all the information we need to know.

3. Case 1: Pneumonia --> Finding the "action" for each pneumonia patient

(preproc_mapping.py) Downloads emars table to map (subject_id, admission_id) —> list of drugs/treatments given to patient
- The mapping is stored in treatments.json (todo: rename the file to a more descriptive title)

(pneumonia_treatments.py) Reads in the mapping above and identifies the unique set of treatments given to pneumonia patients in the past

(pneumonia_cut.py) Supposed to append an action to each patient’s row in data frame and export final data frame

### /max-entropy
Compilation of extracted reward / gradient values and code for optimizer, trajectory construction etc.

### /output visualizations
Code for generating more interpretable visualizations for IRL model output and feature comparison

### /reward landscape
(BC_loss_landscape.ipynb) Adjusted code to create multi-dimensional plots that explain how reward values grow during the training process
* Paper citation: Hao Li, Zheng Xu, Gavin Taylor, Christoph Studer and Tom Goldstein. Visualizing the Loss Landscape of Neural Nets. NIPS, 2018.

### /reward extraction
()
()
(CS282_Final_Project_Pneumonia_Viz.ipynb) IRL-WIT for pneumonia cohort
(CS282_Final_Project_MIMIC_IV_viz.ipynb) IRL-WIT for hypotension cohort

