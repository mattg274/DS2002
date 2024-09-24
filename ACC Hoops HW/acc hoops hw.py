#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:04:57 2024

@author: matt
"""
#%%
import pandas as pd
#%%
accdf = pd.read_csv(r"/Users/matt/Desktop/Academics/UVA/4th Year/Fall 24/DS 2002/acc_players-2324F.csv")
accdf.head(5)
accdf.describe()

#%% 
# 2a: Find the total points scored by all players combined
accdf['Unnamed: 13'] = pd.to_numeric(accdf['Unnamed: 13'], errors='coerce')
print(accdf['Unnamed: 13'].dtype)
total_points = accdf['Unnamed: 13'].sum()
print(total_points)
#%%
# 2b: Find the player who has played the most minutes (MP)
accdf['Unnamed: 6'] = pd.to_numeric(accdf['Unnamed: 6'], errors='coerce')
most_minutes = accdf['Unnamed: 6'].max()
print(most_minutes)
#%%
# 2c: Identify the top 5 players in terms of total rebounds (TRB)
accdf['Unnamed: 7'] = pd.to_numeric(accdf['Unnamed: 7'], errors = 'coerce')
top_rebounders = accdf.sort_values(by='Unnamed: 7', ascending=False).head(5)
print(top_rebounders[['Unnamed: 1','Unnamed: 7']])
#%%
# 3a: create a new dataframe only with players who played more than 500 minutes
minutes_df = accdf[accdf['Unnamed: 13'] > 500]
print(minutes_df)
#%%
# From this filtered DataFrame, determine the player with the highest total assists (AST)
minutes_df.loc[:, 'Unnamed: 8'] = pd.to_numeric(minutes_df['Unnamed: 8'], errors='coerce')
top_assist = minutes_df.loc[minutes_df['Unnamed: 8'].idxmax()]
print(top_assist[['Unnamed: 1','Unnamed: 8']])
#%%
# who are the top 3 assist leaders?
top_3_assists = accdf.sort_values(by='Unnamed: 8', ascending=False).head(3)
#%%
# Who are top 3 shot blocker
accdf.loc[:, 'Unnamed: 10'] = pd.to_numeric(minutes_df['Unnamed: 10'], errors='coerce')
top_3_blockers = minutes_df.sort_values(by='Unnamed: 10', ascending=False).head(3)
#%%
# 4a
school_points = accdf.groupby('Unnamed: 4')['Unnamed: 13'].sum()
print(school_points)
#%%
# 4b
accdf['Unnamed: 8'] = pd.to_numeric(accdf['Unnamed: 8'], errors = 'coerce')
school_assists = accdf.groupby('Unnamed: 4')['Unnamed: 8'].sum()
print(school_assists)
#%%
Total_school_points = accdf.groupby('Unnamed: 4')['Unnamed: 13'].sum()
top3 = Total_school_points.sort_values(ascending = False).head(3)
print(top3)
