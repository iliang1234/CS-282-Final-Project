# CS-282-Final-Project
Code repository for the IRL What-If Tool (IRL-WIT), an interactive visualization tool designed to enhance interpretability in Inverse Reinforcement Learning (IRL), particularly in the healthcare domain.

## Directory Description
### /AIRL 
Attempt at implement AIRL (in progress)

### /Experiment1_PCA
(Checkpoint 3 output viz.ipynb) Notebook code for PCA and output feature data analysis.

### /Experiment2_reward_landscapes
Adjusted code to create multi-dimensional plots that explain how reward values grow during the training process
* Paper citation: Hao Li, Zheng Xu, Gavin Taylor, Christoph Studer and Tom Goldstein. Visualizing the Loss Landscape of Neural Nets. NIPS, 2018.

### /Experiment3_gridworld
(extract_gridworld.ipynb) Notebook to extract reward data for the model running on gridworld toy domain.

### /Experiment4_data
(hypotension_extractions_clusters.ipynb) Notebook to extract rewards for the model running on hypotension patient cohort.

### /Experiment5_data
(pneumonia_extractions_clusters.ipynb) Notebook to extract rewards for the model running on pneumonia patient cohort, for one clustering algorithm.

(pneumonia_clustering.ipynb) Notebook to extract reward value information for each clustering algorithm.

#### /data_pipeline
Overall purpose here is to extract the pneumonia patient cohort.

(preproc_mapping.py) Downloads emars table to map (subject_id, admission_id) —> list of drugs/treatments given to patient
- The mapping is stored in treatments.json (todo: rename the file to a more descriptive title)

(pneumonia_treatments.py) Reads in the mapping above and identifies the unique set of treatments given to pneumonia patients in the past

(pneumonia_cut.py) Exploratory code to append an action to each patient’s row in data frame and export final data frame

### /IRLalgorithms_code
Compilation of extracted reward / gradient values and code for optimizer, trajectory construction etc.

### /reward landscape
(BC_loss_landscape.ipynb) Adjusted code to create multi-dimensional plots that explain how reward values grow during the training process
* Paper citation: Hao Li, Zheng Xu, Gavin Taylor, Christoph Studer and Tom Goldstein. Visualizing the Loss Landscape of Neural Nets. NIPS, 2018.

### /WIT_framework
(CS282_Final_Project_Pneumonia_Viz.ipynb) IRL-WIT code for pneumonia cohort
(CS282_Final_Project_MIMIC_IV_viz.ipynb) IRL-WIT code for hypotension cohort


