import numpy as np
import pandas as pd
import re
import random

# load pneumonia patient data
import json

with open('treatments.json') as f:
    data = json.load(f)

# print(len(data))
key_list = list(data.keys())


with open('patient_admitID_list.json', 'w') as fp:
  json.dump(key_list, fp)
# print(len(list(data.keys())))

# print(key_list[0], data[key_list[0]], type(key_list[0]))
# load in set of treatments

# discretize set of available treatments

# for each patient-admitId pair, append the treatment label as column "action"
