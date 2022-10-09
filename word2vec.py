import gensim.downloader

# Print all gensim embedding models
print(list(gensim.downloader.info()['models'].keys()))


# Download the "word2vec-google-news-300" embeddings
word2vec_vectors = gensim.downloader.load('word2vec-google-news-300')

word2vec_vectors.most_similar('climate')
word2vec_vectors.most_similar('circular economy')
word2vec_vectors.most_similar('global warming')
word2vec_vectors.most_similar('sustainability')
word2vec_vectors.most_similar('green energy')
word2vec_vectors.most_similar('waste')



# Download glove embeddings 
glove_vectors = gensim.downloader.load('glove-wiki-gigaword-50')

glove_vectors.most_similar('climate change')
glove_vectors.most_similar('climate')
glove_vectors.most_similar('circular economy')
glove_vectors.most_similar('global warming')
glove_vectors.most_similar('sustainability')
glove_vectors.most_similar('green energy')
glove_vectors.most_similar('waste')

