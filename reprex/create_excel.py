import csv
import mat73
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
ind = data_dict['FILE_ID'].index('diagnosis(1:sz; 2:hc)')
diagnosis_label = data_dict['analysis_SCORE'][:,ind]
diagnosis_label[diagnosis_label==2] = 0 # HC: 0; SZ: 1

out_csv = '/Users/xinhui.li/Documents/neuromark/XL_FBIRN.csv'
# '/data/users1/xinhui/neuromark/script/XL_FBIRN.csv'
fields = ['smriPath', 'ic', 'label']
rows = []

for i in range(1, 312):
    ica_path = '/data/users2/zfu/Matlab/GSU/Neuromark/Results/ICA/FBIRN/FBIRN_sub'+str(i).zfill(3)+'_component_ica_s1_.nii'
    for j in range(53):
        rows.append( [ica_path, ic_label[j], diagnosis_label[i-1]] )

with open(out_csv, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)