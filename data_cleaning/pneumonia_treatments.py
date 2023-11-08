
import pandas as pd
from collections import defaultdict
# read json file
import json

with open('treatments.json') as f:
    data = json.load(f)

# print(len(data))
key_list = list(data.keys())
# print(len(list(data.keys())))

print(key_list[0], data[key_list[0]], type(key_list[0]))

# load in patient table
pneumonia = pd.read_csv('../data/physionet.org/files/mimiciv/2.0/hosp/all_info_pneumonia.csv.gz', compression='gzip', header=0)
print(pneumonia.columns)
options = defaultdict(int)

def updateOptions(currentList):
  for item in currentList:
    options[item[0]] +=1
print("starting loop")
for index, row in pneumonia.iterrows():
  # convert to float to index into treatments dictionary
  if pd.isna(row['hadm_id_x']):
      admit_id = float(0000.0)
  else:
      admit_id = float(row['hadm_id_x'])
  key = (row['subject_id'], admit_id)
  string_key = str(key)
  
  if string_key not in data:
      print("----warning, missed data", key)
      break
  else:
    updateOptions(data[string_key])

with open('medications.json', 'w') as fp:
  json.dump(options, fp)

print("SUCCESS")