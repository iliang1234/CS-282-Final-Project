# CS-282-Final-Project
goal: interpretable visual framework for IRL models

# Data cleaning
Explanation of pipeline: 
1. Ivy: <br>
First, we are only looking at ICD 9 codes in the non-ICU (hospital) setting, since they are more broad (more data to work with). Within that scope, we are only looking at patients with pneunomia (ICD9: 486) and hyperxemia (ICD9: 79902), two of the more frequently diagnosed diseases that would require immediate treatment. <br>

After extracting the patients with only the diseases of interest, we merged the subject id, ICD code, and ICD English description with the lab events corresponding to each patient. In addition, we added an additional column that reflects the age of each patient to create a masterlist of all the information we need to know.

2. karen's


# Questions (11/8): 
- Hospital vs ICU data?
- Admission_id vs stay_id (hw3)?
- How should we consider time?
- How are "trajectories" created and how do we go about constructing them? 
- What is a good diagnoses (other than hypotension) shoudl we look at? We are guessing that pneumonia and hypoxemia have meaningful sets of treatments but we could be wrong.


