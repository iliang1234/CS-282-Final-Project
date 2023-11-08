import pandas as pd
import numpy as np
import pdb

# grads = pd.read_csv('all_grads_maxent.csv')
# rewards = pd.read_csv('all_rewards_maxent.csv')

# filename = 'all_rewards_maxent.txt'

def csv_to_txt(csv_name, txt_name):
    filename = txt_name
    csv_file = pd.read_csv(csv_name)
    # Open the file for writing
    with open(filename, 'w') as file:
        file.write("[")
        for _, row in csv_file.iterrows():
            file.write("[")
            for i, value in enumerate(row):
                # pdb.set_trace()
                if i < len(row) - 1:
                    file.write(f"{value}, ")
                else:
                    file.write(f"{value}")
            file.write("],\n")
        file.write("]")

csv_to_txt('all_grads_maxent.csv', 'all_grads_maxent.txt')