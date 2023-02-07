#!/usr/bin/env python3
import imp
import sys
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
import os
import os.path

### Init ###
rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = ["Meiryo"]
out_dir = "out/"
os.makedirs(out_dir, exist_ok=True)

#######
# Argument
import_file = sys.argv[1]       # csv file
ch_num = int(sys.argv[2])       # channel number
plt_pitch = int(sys.argv[3])    # plot pitch
if plt_pitch==3600:
    plt_name = "1h"
elif plt_pitch==1800:
    plt_name = "30m"
elif plt_pitch == 1:
    plt_name = "1m"

ch_inner = int(sys.argv[4])     # 庫内 channel


# Debug
print("Input file: {0} ({1})".format(os.path.basename(import_file), type(import_file)))
print("Channel number: {0} ({1})".format(ch_num, type(ch_num)))
print("Plot Picth: {0} ({1})".format(plt_pitch, type(plt_pitch)))
print("Inner channel: {0} ({1})".format(ch_inner, type(ch_inner)))
out_name = os.path.basename(import_file).rstrip('.CSV')
print("Output Name: {0} ({1})".format(out_name, type(out_name)))

######

# convert csv to DataFrame
col_name = range(1,12,1)
df = pd.read_csv(import_file, names = col_name, 
                 encoding="shift-jis", 
                 delimiter=",", 
                 dtype="object")


# filter DF
plt_num = int(df.loc[df[1] == 'データ数'].iloc[0,1])
header_num = int(df.iloc[0,1]) - 7
_df = df[header_num:]

if ch_num >= 4:
    _df = _df.drop([1,2], axis=1)
    _df = _df.dropna(how='all', axis=1)
    _df = _df.dropna(how='any')
else:
    _df = _df.drop([1,2,6], axis=1)
    _df = _df.dropna(how='all', axis=1)
    _df = _df.dropna(how='any')
    _df = _df[1:-1]

_df = _df[1:].astype(float)


# list plot points
channels = []
ch_names = []
for i in range(ch_num):
    ch = str(i)
    ch = []
    channels.append(ch)
    
    ch_name = "ch{}".format(i+1)
    ch_names.append(ch_name)


for ch, j in zip(channels, range(ch_num)):
    for i in range(0, plt_num, plt_pitch):
        a = float(_df.iloc[i,j])
        if plt_pitch==3600 and j!=ch_inner-1 and a>0 and  len(ch)!=0 and ch[-1]<=0:
            print("ch{0} : {1} h".format(j+1, len(ch)))
        if plt_pitch==1800 and j!=ch_inner-1 and a>0 and  len(ch)!=0 and ch[-1]<=0:
            print("ch{0} : {1:.1f} h".format(j+1, len(ch)/2))
        ch.append(a)

# Plot init
fig = plt.figure(figsize=(9, 7), dpi=300)
ax = fig.add_subplot(111)
ax.set_title('Defrost Test: {}'.format(out_name), fontsize=18)
ax.set_xlabel('Time [h]', fontsize=16)
ax.set_ylabel('Temparature [℃]', fontsize=16)
ax.axhline(y=0, color='red', lw=1, ls='--')

# Plot
for ch, names in zip(channels, ch_names):
    ax.plot(ch, label = names)

ax.legend()
fig.show()
fig.savefig(out_dir + "{0}_{1}".format(out_name, plt_name)+".jpg")