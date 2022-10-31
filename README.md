# Argument Mining to Analyze attitudes and beliefs on Sustainable Initiatives

This repository contains the code that was used to scrape posts and comments about sustainable initiatives on Reddit. The resulting (preliminary) dataset is presented in an extended abstract for ICA (2022).

### `code`
#### `scrape_reddit`
Retrieves the posts and comments that contain the selected keywords, and performs a number of preprocessing steps such as filtering comments made by bots.

#### `word2vec.py`
Can be used to obtain semantically similar words to a query with the Google News word2vec embeddings and the Glove GigaWord corpus.

### `data`
#### `post_data.csv`
Contains 2.073 Reddit posts

#### `comment_data.csv`
Contains 46.285 comments 

#### `coding.xlsx`
Contains the first data annotations performed by two coders