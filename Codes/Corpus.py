# importing libraries
import sys
import requests
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os

# function for cleaning the corpus
def cleancorpus(corpus):
    # Lowercase
    corpus = corpus.lower()

    # Removing special characters and numbers from the corpus
    corpus = re.sub(r'[^a-zA-Z\s]', '', corpus)
    corpus = re.sub(r'\d+', '', corpus)

    # Tokenization
    tokens = word_tokenize(corpus)

    # Removing stopwords from it
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Removing short and long words
    tokens = [token for token in tokens if len(token) > 2 and len(token) < 20]

    # Stemming usinf porter stemmer
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    # combining the corpus
    cleaned_corpus = ' '.join(tokens)
    cleaned_corpus = re.sub(r'\s+', ' ', cleaned_corpus).strip()

    return cleaned_corpus


# making of corpus
def make_corpus(url, out_f):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    os.makedirs(os.path.dirname(out_f), exist_ok=True)

    with open(out_f, 'w') as output:
        # parsing the div tags
        relevant_elements = soup.find_all('div')

        for element in relevant_elements:
            text = element.get_text().strip()
            if text:
                cleaned_text = cleancorpus(text)
                output.write(cleaned_text + '\n')

    print('Fetch the corpus!')


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(
            'python CorpusCreation.py <website_url> <output_directory/corpus_file>')
        sys.exit(1)

    url = sys.argv[1]
    out_f = sys.argv[2]
    make_corpus(url, out_f)
