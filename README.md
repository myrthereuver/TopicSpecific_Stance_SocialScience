# Topic-specific social science theory in stance detection: a proposal and interdisciplinary pilot study on sustainability initiatives

#### This repository contains the code and documents for the paper 
#### "Topic-specific social science theory in stance detection: a proposal and interdisciplinary pilot study on sustainability initiatives", authors: Myrthe Reuver, Alessandra Polimeno, Antske Fokkens, Ana Isabel Lopes. Published at the 4th Workshop on Computational Linguistics for the Political and Social Sciences (CPSS) at KONVENS, 13 September 2024.
#### contact: Myrthe Reuver, myrthe[fullstop]reuver[at]gmail.com

The datasets in this paper are the "Reddit European Sustainability Initiatives corpus" and the annotated subset of this corpus, released (under CC-BY-NC licence) through the following huggingface repository: [Myrthe/RedditEuropeanSustainabilityInitiatives](https://huggingface.co/datasets/Myrthe/RedditEuropeanSustainabilityInitiatives).

This repository contains code, data, and documentations to complete:
- Scraping: the code that was used to scrape posts and comments about sustainable initiatives on Reddit.
- Annotating: codebook versions, and annotation task designs (in Qualtrics import files and visually in pdf);
- (Pre)processing: code to obtain a clean dataset from the annotions, calculate Inter-Annotator Agreement, and majority labels;
- Data analysis: code to train topic models and clustering models 

Code subsections:

### (1) `Scraping`
#### `scrape_reddit`
Retrieves the posts and comments that contain the selected keywords, and performs a number of preprocessing steps such as filtering comments made by bots.

#### `word2vec.py`
Can be used to obtain semantically similar words to a query with the Google News word2vec embeddings and the Glove GigaWord corpus.

### (2) `Annotating`
#### 'AnnotationGuidelines_SustainabilityArguments.pdf'
Contains the final codebook with instructions for the crowd annotating the 91 sample data points.

#### Qualtrics Templates
The qualtrics templates, which toegether with the data in the HuggingFace repository can be used to re-create the annotation experiments, are provided in the folder "data" under "Qualtrics templates"

### (3) `Data (Pre)Processing`
The 'annotator_agreement' folder contains notebooks that analyze the output of the crowd task and the expert coder task for inter annotator agreement, as well as preprocess it into an annotated dataset.

### (4) `Modelling and Data Analysis`
The 'exploratory_notebooks' folder contains code for our exploration of the Reddit corpus, which was mostly done through clustering and BERTopic models and described in the appendix of our paper.

The 'models' folder contains the version of the BERTopic model used to analyze the dataset as described in the appendix of our paper.
