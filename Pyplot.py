import csv
import pandas as pd
import datetime
import numpy as np

df = pd.read_csv('trip_data_2.csv', usecols=['pickup_datetime', 'passenger_count'])
df['a'], df['b'] = df['pickup_datetime'].str.split(' ', 1).str
df['a2'], df['b2'], df['c']=df['b'].str.split(':', 2).str
d=df.groupby(['a2']).mean()
print d

import matplotlib.pyplot as plt
ax = d[['passenger_count']].plot(kind='bar', title ="Average Passenger Count", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Hour", fontsize=12)
ax.set_ylabel("Count", fontsize=12)
plt.show()