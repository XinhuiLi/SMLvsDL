import csv
import mat73
import numpy as np
import pandas as pd

# read IC index
file_name = '/Users/xinhui.li/Documents/neuromark/ICA/ICNlabel_For_Sharing_onlyICNs.xlsx'
# '/data/users1/xinhui/neuromark/script/ICNlabel_For_Sharing_onlyICNs.xlsx'
df = pd.read_excel(file_name, sheet_name='Sheet1', header=0)
ic = df["'GSP_IC_ID'"]
ic_label = ic.to_numpy() - 1

# read label
fbirn_sub_path = '/Users/xinhui.li/Documents/neuromark/Subject_selection/FBIRN/sub_info_FBIRN.mat'
# '/data/users2/zfu/Matlab/GSU/Neuromark/Results/Subject_selection/FBIRN/sub_info_FBIRN.mat'
data_dict = mat73.loadmat(fbirn_sub_path)

keys=['diagnosis(1:sz; 2:hc)','PANSS(positive)','PANSS(negative)']
ind = [data_dict['FILE_ID'].index(i) for i in keys]

label = data_dict['analysis_SCORE'][:,ind]

train_sample = 53*250
out_csv = f'/Users/xinhui.li/Documents/SMLvsDL/reprex/SampleSplitsAll/te_{train_sample}_rep_0.csv' #tr_1250_rep_0, va_1250_rep_0, te_1250_rep_0
# '/data/users1/xinhui/neuromark/script/XL_FBIRN.csv' # XL_FBIRN_all
fields = ['smriPath', 'ic', 'label', 'PANSS_positive', 'PANSS_negative'] # regression
rows = []

# Selected IC
# 3 SMN; 21 AUD; 45 SCN; 7 CER; - SZ
# 94 DMN - Autism

for i in range(283, 312): # total 312; 1, 253; 253, 283; 283, 312
    ica_path = '/data/users2/zfu/Matlab/GSU/Neuromark/Results/ICA/FBIRN/FBIRN_sub'+str(i).zfill(3)+'_component_ica_s1_.nii'
    
    if np.isnan( label[i-1, 1] )==True:
        continue
    
    for j in range(53): #[2, 20, 44, 6, 93]: 
        if label[i-1, 1] > 0 and label[i-1, 2] > 0:
            # rows.append( [ica_path, j, label[i-1,0], label[i-1,1], label[i-1,2]] )
            rows.append( [ica_path, ic_label[j], label[i-1,0], label[i-1,1], label[i-1,2]] )
        else:
            # rows.append( [ica_path, j, label[i-1,0], 0, 0] )
            rows.append( [ica_path, ic_label[j], label[i-1,0], 0, 0] )

with open(out_csv, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)