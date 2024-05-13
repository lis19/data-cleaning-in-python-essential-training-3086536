# %%
import pandas as pd

# %%
df = pd.read_csv('/workspaces/data-cleaning-in-python-essential-training-3086536/Ch01/01_03/metrics.csv', parse_dates=['time'])
df.sample(10)

# %%
df.groupby('name').describe()

# %%
df['name'].value_counts()

# %%
pd.pivot(df, index='time', columns='name').plot(subplots=True)

# %%
df.query('name == "cpu" & (value < 0 | value > 100)')

# %% 
mem = df[df['name'] == 'mem']['value'] # filter by mem only in 'name' column, and save 'value' entries 
z_score = (mem - mem.mean())/mem.std() # z-score (distance from mean)
bad_mem = mem[z_score.abs() > 2] # find those that are >2s.d. away
df.loc[bad_mem.index] # use index column of bad_mem to find bad rows in df
