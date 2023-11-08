# CS-282-Final-Project
goal: interpretable visual framework for IRL models

# Data cleaning
Explanation of pipeline: 
1. First, we are only looking at ICD 9 codes in the non-ICU (hospital) setting, since they are more broad (more data to work with). Within that scope, we are only looking at patients with pneunomia (ICD9: 486) and hyperxemia (ICD9: 79902), two of the more frequently diagnosed diseases that would require immediate treatment.

2. After extracting the patients with only the diseases of interest, we merged the subject id, ICD code, and ICD English description with the lab events corresponding to each patient. In addition, we added an additional column that reflects the age of each patient to create a masterlist of all the information we need to know.

2. Case 1: Pneumonia --> Finding the "action" for each pneumonia patient
Preproc_mapping.py: 
downloads emars table to map (subject_id, admission_id) —> list of drugs/treatments given to patient
* The mapping is stored in treatments.json (todo: rename the file to a more descriptive title)

pneumonia_treatments.py: 
Reads in the mapping above and identifies the unique set of treatments given to pneumonia patients in the past

pneumonia_cut.py: 
Supposed to append an action to each patient’s row in data frame and export final data frame

# Questions (11/8): 
- Hospital vs ICU data?
- Admission_id vs stay_id (hw3)?
- How should we consider time?
- How are "trajectories" created and how do we go about constructing them? 
- What is a good diagnoses (other than hypotension) shoudl we look at? We are guessing that pneumonia and hypoxemia have meaningful sets of treatments but we could be wrong.


