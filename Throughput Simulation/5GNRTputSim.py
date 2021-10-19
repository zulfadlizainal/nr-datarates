# Created by github.com/zulfadlizainal

import pandas as pd
import numpy as np

df_rsrp = pd.read_excel('Ref_LA.xlsx', 'RSRP')
df_rsrq = pd.read_excel('Ref_LA.xlsx', 'RSRQ')
df_sinr = pd.read_excel('Ref_LA.xlsx', 'SINR')

df_mcs = pd.read_excel('Ref_MCSxR.xlsx')

# Calculate Code Rate (R)

df_mcs['R'] = df_mcs['R x 1024'] / 1024

# Input 

prb_num = int(input('Max PRB: '))

# Calculate RSRP
df_rsrp['R'] = df_rsrp['MCS'].map(df_mcs['R'])  # MAP based on Index (Index = MCS in this case)
df_rsrp['QM'] = df_rsrp['MCS'].map(df_mcs['QM'])   # Map based on Index (Index = MCS in this case)
df_rsrp['nre_prime'] = (12 * df_rsrp['SYM LENGTH AVG (BASED ON SLIV)']) - df_rsrp['DMRS PER PRB'] - df_rsrp['RRC OH']
df_rsrp['nre'] = (np.minimum(156,df_rsrp['nre_prime'])) * (df_rsrp['PRB AVG (%)'] * prb_num) * df_rsrp['SLOT (%)']
df_rsrp['ninfo'] = df_rsrp['nre'] * df_rsrp['R'] * df_rsrp['QM'] * df_rsrp['LAYER']
df_rsrp['ninfo_prime'] = np.maximum(24, )

# print(' ')
# print('ありがとうございました！！')
# print('Download this program: https://github.com/zulfadlizainal')
# print('Author: https://www.linkedin.com/in/zulfadlizainal')
# print(' ')
