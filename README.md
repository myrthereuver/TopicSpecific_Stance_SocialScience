# Topic-specific social science theory in stance detection: a pilot study and dataset on sustainability initatives

This repository contains:
- Scraping: the code that was used to scrape posts and comments about sustainable initiatives on Reddit.
- Annotating: The input data to the annotation tasks, codebook versions, and annotation task designs;
- (Pre)processing code to obtain a clean dataset from the annotions, calculate Inter-Annotator Agreement, and majority labels.

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

#### 'codebook.pdf'
Contains the first codebook with instructions for the annotated variables

#### `coding.xlsx`
Contains the first data annotations performed by two coders
