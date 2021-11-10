'''
Create excel for sMRI dataset
'''
import os
import csv
import mat73
import numpy as np
import pandas as pd

# read label
fbirn_smri_path = '/data/qneuromark/Data/FBIRN/ZN_Neuromark/ZN_Prep_sMRI'
fbirn_sub_path = '/data/users2/zfu/Matlab/GSU/Neuromark/Results/Data_info/FBIRN/subject_information_FBIRN.mat'
# '/Users/xinhui.li/Documents/neuromark/sMRI_data_info/subject_information_FBIRN.mat'
data_dict = mat73.loadmat(fbirn_sub_path)

keys = ['diagnosis(1:sz; 2:hc)', 'PANSS(positive)', 'PANSS(negative)']
ind = [data_dict['FILE_ID'].index(i) for i in keys]
label = data_dict['Num_scores'][:,ind]
subid_list = data_dict['SubjectID']

smri_list = os.listdir('/data/qneuromark/Data/FBIRN/ZN_Neuromark/ZN_Prep_sMRI')

train_sample = 285
out_csv = f'/data/users1/xinhui/neuromark/SMLvsDL/reprex/SampleSplitsSMRI/tr_{train_sample}_rep_0.csv'
# f'/Users/xinhui.li/Documents/SMLvsDL/reprex/SampleSplitsSMRI/tr_{train_sample}_rep_0.csv' #tr_1250_rep_0, va_1250_rep_0, te_1250_rep_0
# XL_FBIRN_all
fields = ['smriPath', 'label', 'PANSS_positive', 'PANSS_negative'] # regression
rows = []

# Selected IC
# 3 SMN; 21 AUD; 45 SCN; 7 CER; - SZ
# 94 DMN - Autism

for i in range(1, 325): # total 405; 1, 325; 326, 365; 366, 406
    
    subid = subid_list[i-1][0]
    smri_path = os.path.join( fbirn_smri_path, subid_list[i-1][0], 'VBM_modulated_SPM12_SM6.nii' )

    if np.isnan( label[i-1, 1] )==True:
        continue
    
    if subid not in smri_list:
        continue

    if label[i-1, 1] > 0 and label[i-1, 2] > 0:
        # rows.append( [ica_path, j, label[i-1,0], label[i-1,1], label[i-1,2]] )
        rows.append( [smri_path, label[i-1,0], label[i-1,1], label[i-1,2]] )
    else:
        # rows.append( [ica_path, j, label[i-1,0], 0, 0] )
        rows.append( [smri_path, label[i-1,0], 0, 0] )

with open(out_csv, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)