#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:21:47 2022

@author: alessandrapolimeno
"""

import pandas as pd 
from nltk.tokenize import word_tokenize, sent_tokenize 


comment_df = pd.read_csv("data/comment_data.csv", index_col = 0)
posts = pd.read_csv("data/post_data.csv", index_col = 0)






#### Create coding dataframe where some columns are removed/switched around 
coding_df = comment_df.drop(['subreddit'], axis = 1)

coding_df = coding_df[['post_title', 'post_id', 'comment_id', 'parent_id', 'comment_body']]




#### Create coding dataframe where each comment is split into sentences

comment_df = comment_df.dropna(subset=['comment_body'])

comments = comment_df['comment_body'].tolist()
comment_ids= comment_df['comment_id'].tolist()

pairs = zip(comments, comment_ids)




sentences = []
ids = []


for com in pairs: 
    comment = com[0]
    cid = com[1]
    
    # make new comment_id 
    
    
    sents = sent_tokenize(comment)
    
    for sent in sents: 
        sentences.append(sent)
        ids.append(cid)
        

coding_df = pd.DataFrame(columns = ['comment_id','post_title', 'sentence'])
coding_df['sentence'] = sentences
coding_df['comment_id'] = ids


### Match sentences to the sourse post title 

# Make lookup dictionary 
extract_this = pd.DataFrame()
extract_this["title"] = posts["title"]
extract_this["post_id"] = posts["post_id"]

# Transpose the Dataframe and turn it into a lookup dictionary
lookup = extract_this.set_index('post_id').T.to_dict()


titles = []

for i in ids: 
    i = i[:6]
    try:
        title = lookup[i]["title"]
    except:
        title = 'NA'
    titles.append(title)

coding_df['post_title'] = titles

coding_df.to_csv("data/coding.csv", index = True)
