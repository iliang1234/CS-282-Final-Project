from hosp_preprocess_util import read_d_labitems_table
import pandas as pd

# this is the mapping
mapping_path = '../data/physionet.org/files/mimiciv/2.0/hosp/d_icd_diagnoses.csv.gz'
labitems_path = '../data/physionet.org/files/mimiciv/2.0/hosp/d_labitems.csv.gz'
# diagnosis
diagnosis_path = '../data/physionet.org/files/mimiciv/2.0/hosp/diagnoses_icd.csv.gz'


module = pd.read_csv(diagnosis_path, compression='gzip', header=0)
mapping = pd.read_csv(mapping_path, compression='gzip', header=0)

print(module.columns)
print(module.shape)

# filter for icd version 9
module = module[module['icd_version']==9]
code_mapping = {}
for index, row in mapping.iterrows():
    if row['icd_version'] == 9:
        if row['icd_code'] in code_mapping:
            print("warning: overwriting")

    code_mapping[row['icd_code']] = row['long_title']

print(len(code_mapping))

## emar
emar_path = '../data/physionet.org/files/mimiciv/2.0/hosp/emar.csv.gz'
emars = pd.read_csv(emar_path, compression='gzip', header=0)
print(emars)

###
def custom_key(row):
    if pd.isna(row['hadm_id']):
        admit_id = float(0000.0)
    else:
        admit_id = row['hadm_id']
    return (row['subject_id'], admit_id)

# Create a new key column
emars['Patient-AdmitVisit'] = emars.apply(custom_key, axis=1)
# Groupby
grouped = emars.groupby('Patient-AdmitVisit')

# custom aggregator
def custom_aggregator(group):
    return list(zip(group['medication']))

# aggregate
result = grouped.apply(custom_aggregator)
result = result.to_frame(name='medications_list')
print("finished result")

final_result = result.reset_index().rename(columns={"index":"Patient-AdmissionId"})
print(final_result.columns)

# get mapping from subjectId-AdmitId to list of medications
treatments = {}
for index, row in final_result.iterrows():
  string_key = str(row['Patient-AdmitVisit'])
  treatments[string_key] = row['medications_list']

print("finished getting json")

### export all treatments per  subjectId-AdmitId to json file
import json
with open('treatments.json', 'w') as fp:
  json.dump(treatments, fp)