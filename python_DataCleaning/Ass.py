import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', "MAdrid_miLAN", 'londON_StockhOlm',

                               'Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})


# FIRST  PUZZLE
df['FlightNumber'][0:2] = df['FlightNumber'][0:2].fillna(10055)

df['FlightNumber'][2:4] = df['FlightNumber'][2:4].fillna(10075)

df['FlightNumber'] = df['FlightNumber'].astype(int)

print(df['FlightNumber'].dtype)

# SECOND PUZZLE

Temp_df = pd.DataFrame({'From': df['From_To'].apply(lambda x: x.split('_')[0]),
                        'To': df['From_To'].apply(lambda x: x.split('_')[1])})


# THIRD PUZZLE

Temp_df['From'] = Temp_df['From'].apply(lambda x: x.title())

Temp_df['To'] = Temp_df['To'].apply(lambda x: x.title())


# print(Temp_df)

# FOURTH PUZZLE

df.drop('From_To', axis=1,inplace=True)

df = pd.concat([df, Temp_df], axis=1)

# print(df)

# FIFTH PUZZLE

lst = [df['RecentDelays'][i] for i in range(5)]

delay1 = []

delay2 = []

delay3 = []

[delay1.append(np.nan) if len(lst[i]) == 0 else delay1.append(lst[i][0]) for i in range(len(lst))]

[delay2.append(np.nan) if len(lst[i]) < 2 else delay2.append(lst[i][1]) for i in range(len(lst))]

[delay3.append(np.nan) if len(lst[i]) < 3 else delay3.append(lst[i][2]) for i in range(len(lst))]

delays = pd.DataFrame([delay1, delay2, delay3])

delays = delays.T

delays.columns = ['delay1', 'delay2', 'delay3']


df.drop('RecentDelays', axis=1, inplace=True)

Final_df = pd.concat([df, delays], axis=1)

print(Final_df)
