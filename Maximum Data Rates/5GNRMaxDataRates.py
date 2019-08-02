#Created by github.com/zulfadlizainal

import pandas as pd

# Print Information
print('\n###########################################################################\n')
print('5G NR Maximum Data Rates Calculator - 3GPP TS 38.306 Section 4.1.2 Rel 15')
print('\n###########################################################################\n')

print('\nFormulae:\n')

print('Data Rates (in Mbps) = 10^(-6) x (J x (v x Q x f(i) x Rmax x (PRB x 12 / Ts) x (1 - OH))\n')

print('J    = Number of Carrier Aggregation Carriers\n'
      'v    = MIMO Layers - Spatial Multiplexing\n'
      'Q    = Modulation Order (bits/symbol)\n'
      'f(i) = Scaling Factor (1)\n'
      'Rmax = Contant (948/1024)\n'
      'μ    = Numerology\n'
      'PRB  = Number of PRB respective of Bandwidth and Subcarrier Spcacing\n'
      'Ts   = Symbol Duration/Subframe (10^(-3)/(14 x 2^(μ))\n'
      'OH   = Overhead Constant\n'
      )

#Get Information
print('\nInput Values:\n')

J = int(input('Number of Carrier Aggregation Carriers (J) = '))
print('\n')
v = int(input('MIMO Layers - Spatial Multiplexing (v) = '))

df_Q = pd.read_excel('Modulation.xlsx', encoding='utf-8-sig')
print('\n')
print('*****Modulation Order*****')
print('\n')
print(df_Q.to_string(index = False))
print('\n')
Q = int(input('Modulation Order in bits/symbol (Q) = '))

df_numerology = pd.read_excel('Numerology.xlsx', encoding='utf-8-sig')
print('\n')
print('*****Numerology*****')
print('\n')
print(df_numerology.to_string(index = False))
print('\n')
numerology = int(input('Numerology (μ) = '))

df_prbfr1 = pd.read_excel('PRB_FR1.xlsx', encoding='utf-8-sig')
df_prbfr2 = pd.read_excel('PRB_FR2.xlsx', encoding='utf-8-sig')
print('\n')
print('*****FR1 PRB based on SCS (kHz) and Bandwith (MHz)*****')
print('\n')
print(df_prbfr1.to_string(index = False))
print('\n')
print('*****FR2 PRB based on SCS (kHz) and Bandwith (MHz)*****')
print('\n')
print(df_prbfr2.to_string(index = False))
print('\n')
PRB = int(input('Number of PRB respective of Bandwidth and Subcarrier Spcacing (PRB) = '))

df_OH = pd.read_excel('Overhead.xlsx', encoding='utf-8-sig')
print('\n')
print('*****Overhead Constant*****')
print('\n')
print(df_OH.to_string(index = False))
print('\n')
OH = float(input('Overhead Constant = '))

#Calculate

Ts = 10**(-3) / (14*2**(numerology))

MaxTput = (10**(-6)) * J * (v * Q * 1 * (948 / 1024) * ((270 * 12) / Ts) * (1 - OH))

print(f'\nMaximum Data Rates = {MaxTput} Mbps\n')

print(' ')
print('ありがとうございました！！')
print('Download this program: https://github.com/zulfadlizainal')
print('Author: https://www.linkedin.com/in/zulfadlizainal')
print(' ')
