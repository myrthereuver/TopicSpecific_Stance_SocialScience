# Topic-specific social science theory in stance detection: a proposal and interdisciplinary pilot study on sustainability initiatives

#### This repository contains the code and documents for the paper 
#### "Topic-specific social science theory in stance detection: a proposal and interdisciplinary pilot study on sustainability initiatives", authors: Myrthe Reuver, Alessandra Polimeno, Antske Fokkens, Ana Isabel Lopes. Published at the 4th Workshop on Computational Linguistics for the Political and Social Sciences (CPSS) at KONVENS, 13 September 2024.
#### contact: Myrthe Reuver, myrthe[fullstop]reuver[at]vu.nl

The datasets in this paper are the "Reddit European Sustainability Initiatives corpus" and the annotated subset of this corpus, released (under CC-BY-NC licence) through the following huggingface repository: [Myrthe/RedditEuropeanSustainabilityInitiatives](https://huggingface.co/datasets/Myrthe/RedditEuropeanSustainabilityInitiatives).

This repository contains code, data, and documentations to complete:
- Scraping: the code that was used to scrape posts and comments about sustainable initiatives on Reddit.
- Annotating: codebook versions, and annotation task designs (in Qualtrics import files and visually in pdf);
- (Pre)processing: code to obtain a clean dataset from the annotions, calculate Inter-Annotator Agreement, and majority labels;
- Data analysis: code to train topic models and clustering models 

Code subsections:

### `scraping`
#### `scrape_reddit`
Retrieves the posts and comments that contain the selected keywords, and performs a number of preprocessing steps such as filtering comments made by bots.

#### `word2vec.py`
Can be used to obtain semantically similar words to a query with the Google News word2vec embeddings and the Glove GigaWord corpus.

### `annotating`
#### 'Codebook_data.pdf'
Contains the first codebook with instructions written for the expert coding session for the annotated variables.

#### 'AnnotationGuidelines_SustainabilityArguments.pdf'
Contains the final codebook with instructions for the crowd annotating the 91 sample data points.

#### `coding.xlsx`
Contains the first data annotations performed by two coders

### `(Pre)Processing`
The IAA folder contains notebooks that analyze the output of the crowd task for inter annotator agreement, as well as preprocess it into an annotated dataset.
