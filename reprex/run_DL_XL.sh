# SZ classification
python run_DL.py --tr_smp_sizes 1250 --nReps 20 --nc 2 --bs 32 --lr 0.00001 --es 1000 --pp 0 --es_va 1 --es_pat 20 --ml 'clx_results/' --mt 'neuromarkNet' --ssd 'SampleSplits/'  --scorename 'label' --nw 8 --cr 'clx' --tss 1250

# SZ regression
python run_DL.py --tr_smp_sizes 1250 --nReps 20 --nc 1 --bs 32 --lr 0.00001 --es 1000 --pp 0 --es_va 1 --es_pat 20 --ml 'reg_results/' --mt 'neuromarkNetRegression' --ssd 'SampleSplits/'  --scorename 'PANSS_positive' --nw 8 --cr 'reg'