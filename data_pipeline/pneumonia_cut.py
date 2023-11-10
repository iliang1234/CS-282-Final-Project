import numpy as np
import pandas as pd
import re
import random
import json 
import pdb
# load corresponding treatments
with open('treatments.json') as f:
    data = json.load(f)

# load pneumonia patient data
pneumonia = pd.read_csv('../data/physionet.org/files/mimiciv/2.0/hosp/all_info_pneumonia.csv.gz', compression='gzip', header=0)
print(pneumonia.columns)
print("data shape: ", pneumonia.shape)

# action space (determined by evaluating most frequent and relevant treatments)
combinations = set([])

meds = {
  'Metoprolol Tartrate': '1',
  'Azithromycin': '2', 
  'Hydrocortisone Na Succ.': '3',
  'Ipratropium Bromide Neb': '3',
  'Ipratropium-Albuterol Neb': '3',
  'Albuterol 0.083% Neb Soln': '4',
  'Gabapentin': '5'
}
# Metoprolol Tartrate: 16826910 patients
# Azithromycin: 2628275 patients
# Hydrocortisone Sodium Succinate: 456760 patients
# Ipratropium Bromide Neb', 13233926 patients / 'Ipratropium-Albuterol Neb': 9752899 patients' / Albuterol 0.083% Neb Soln': 13145969 patients;'
# Gabapentin: 11164402 patients

def getCombo(med_list):
  this_set = set([])
  for m in med_list:
    if m[0] in meds:
      this_set.add(meds[m[0]])
  this_list = list(this_set)
  return ''.join(this_list)

# how many different combinations of these treatments exist in the dataset?
count = 0
for index, row in pneumonia.iterrows():
  # convert to float to index into treatments dictionary
  if pd.isna(row['hadm_id_x']):
      admit_id = float(0000.0)
  else:
      admit_id = float(row['hadm_id_x'])
  key = (row['subject_id'], admit_id)
  string_key = str(key)
  
  if string_key not in data:
    count+=1
  else:
    # check the combinations
    combinations.add(getCombo(data[string_key]))

print("saved, len of combinations: ", len(combinations))
print("# of patient-admitID pairs NOT included:", count)

# record the set of unique combinations
with open('combinations.txt','w') as f:
   f.write(str(combinations))

# NEXT STEPS: 
# discretize set of available treatments

# for each patient-admitId pair, append the treatment label as column "action"
