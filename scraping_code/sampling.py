# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:08:31 2022

@author: Alessandra
"""

import pandas as pd

df = pd.read_csv("data/comment_data.csv", index_col = 0)

df_europe = df.loc[df['subreddit'] == 'europe']
df_europes = df.loc[df['subreddit'] == 'europes']
df_eu = df.loc[df['subreddit'] == 'europeanunion']


set_europe = set(df_europe['post_id'].tolist())
set_europes = set(df_europes['post_id'].tolist())
set_eu = set(df_eu['post_id'].tolist())

# Remove < 25
df_europe = df_europe.loc[df_europe['comment_body'].str.len() > 25]
df_europe = df_europe.loc[df_europe['post_title'].str.len() > 42]
df_europes = df_europes.loc[df_europes['comment_body'].str.len() > 25]
df_eu = df_eu.loc[df_eu['comment_body'].str.len() > 25]

# Remove non-t3 
df_europe = df_europe[df_europe['parent_id'].str.contains("t3") == True]
df_europe = df_europe[df_europe['post_title'].str.contains("Election") == False]
df_europes = df_europes[df_europes['parent_id'].str.contains("t3") == True]
df_eu = df_eu[df_eu['parent_id'].str.contains("t3") == True]




# randomly sample 
sample_europe = df_europe.groupby("post_title").sample(frac = 0.084)
sample_eu = df_eu.groupby("post_title").sample(frac = 0.26)
sample_europes = df_europes.groupby("post_title").sample(frac = 0.4)

sample = pd.concat([sample_europe, sample_eu, sample_europes])


sample.to_csv("data/sample.csv")
