#!/usr/bin/env python3
import csv
import sys
from unicodedata import name
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
import os

### setup ###
rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = ["Meiryo"]
out_dir = "img/"
os.makedirs(out_dir, exist_ok=True)

### argument ###
import_file = sys.argv[0]   # csv file
ch_num = sys.argv[1]        # channel number
plt_pitch = sys.argv[2]     # plot pitch


# import csv file
col_name = range(1,12,1)
df = pd.read_csv(import_file, names = col_name, 
                 encoding="shift-jis", 
                 delimiter=",", 
                 dtype="object")


# filter DataFrame
plt_num = int(df.iloc[10,1])
header_num = int(df.iloc[0,1]) - 7
_df = df[header_num:]

if ch_num >= 4:
    _df = _df.drop([1,2], axis=1)
    _df = _df.dropna(how='all', axis=1)
    _df = _df.dropna(how='any')
    # _df = _df[1:]
    _df = _df[1:].astype(float)
else:
    _df = _df.drop([1,2,6], axis=1)
    _df = _df.dropna(how='all', axis=1)
    _df = _df.dropna(how='any')
    _df = _df[1:-1]
    _df = _df[1:].astype(float)


# plot
channels = []
ch_names = []
for i in range(ch_num):
    ch_name = "ch{}".format(i+1)
    channels.append(i)
    ch_names.append(ch_name)

# ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9 = [], [], [], [], [], [], [], [], []


for ch, j in zip(channels, range(ch_num)):
    for i in range(0, plt_num, plt_pitch):
        a = _df.iloc[i,j]
        if j != 8 and float(a) > 0 and ch[-1] <= 0:
            print("ch{0} : {1} 時間".format(j+1, len(ch)))
        ch.append(float(a))

fig = plt.figure(figsize=(9, 7), dpi=300)
ax = fig.add_subplot(111)
ax.set_title('解凍テスト（段ボールあり）')
ax.set_xlabel('時間 [h]')
ax.set_ylabel('温度 [℃]')
ax.axhline(y=0, xmin=0, xmax=plt_num/plt_pitch, color='red', lw=1, ls='--')


for ch, names in zip(channels, ch_names):
    ax.plot(ch, label = names)

ax.legend()
fig.show()
fig.savefig(out_dir + "ダンボール有.jpg")


# for test_2: 40℃ 温水解凍
ch1 = []
ch2 = []
ch3 = []
ch4 = []
ch5 = []

channels = [ch1, ch2, ch3, ch4, ch5]
ch_names = ["水温", 
            "一斗缶(表面)", 
            "ゆず果汁(表面)", 
            "一斗缶(中心)",  
            "ゆず果汁(中心)"
           ]

for ch, j in zip(channels, range(5)):
    for i in range(1000, 82123, 3600):
        a = _df2.iloc[i,j]
        if j != 0 and float(a) > 0 and ch[-1] <= 0:
            print("ch{0} : {1} 時間".format(j+1, len(ch)))
        ch.append(float(a))

fig = plt.figure(figsize=(9, 7), dpi=300)
ax = fig.add_subplot(111)
ax.set_title('温水解凍(40℃)')
ax.set_xlabel('time [h]')
ax.set_ylabel('Temparature [℃]')
ax.axhline(y=0, xmin=0, xmax=750, color='red', lw=1, ls='--')


for ch, names in zip(channels, ch_names):
    ax.plot(ch, label = names)

ax.legend()
fig.show()
fig.savefig(out_dir + "温水_40.jpg")