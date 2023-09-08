# Topic-specific social science theory in stance detection: a pilot study and dataset on sustainability initatives

This repository contains code, data, and documentations to complete:
- Scraping: the code that was used to scrape posts and comments about sustainable initiatives on Reddit.
- Annotating: The input data to the annotation tasks, codebook versions, and annotation task designs;
- (Pre)processing: code to obtain a clean dataset from the annotions, calculate Inter-Annotator Agreement, and majority labels.

for the paper "Topic-specific social science theory in stance detection: a pilot study and dataset on sustainability initatives"

### `scraping`
#### `scrape_reddit`
Retrieves the posts and comments that contain the selected keywords, and performs a number of preprocessing steps such as filtering comments made by bots.

#### `word2vec.py`
Can be used to obtain semantically similar words to a query with the Google News word2vec embeddings and the Glove GigaWord corpus.

### `data`
#### `post_data.csv`
Contains the scraped 2.073 Reddit posts

#### `comment_data.csv`
Contains the scraped 46.285 comments 


### `annotating`
#### 'codebook.pdf'
Contains the first codebook with instructions for the annotated variables.

#### 'crowd_coding_instructions.pdf'
Contains the final codebook with instructions for the crowd annotating the 91 sample data points.

#### `coding.xlsx`
Contains the first data annotations performed by two coders

### `(Pre)Processing`
The IAA folder contains notebooks that analyze the output of the crowd task for inter annotator agreement, as well as preprocess it into an annotated dataset.
