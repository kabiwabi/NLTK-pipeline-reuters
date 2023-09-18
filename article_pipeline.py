import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

import tarfile
import os
import re

nltk.download('punkt')

def read_extract_text(file_path, extract_path):
    extracted_articles = []
    with tarfile.open(file_path, 'r:gz') as tar:
        tar.extractall(path=extract_path)
        for file_name in os.listdir(path=extract_path):
            if re.match(r'reut2-\d+.sgm', file_name):
                with open(os.path.join(extract_path, file_name), 'r', encoding='latin-1') as news_article:
                    raw_article_html = news_article.read()
                    soup = BeautifulSoup(raw_article_html, 'html.parser')
                    article_elements = soup.findAll('text')
                    for article_element in article_elements:
                        article_text_element = article_element.text
                        extracted_articles.append(article_text_element)
    return extracted_articles


def tokenize(extracted_articles):
    return [word_tokenize(extracted_article) for extracted_article in extracted_articles]


def to_lowercase(tokenized_articles):
    return [tokenized_article.lower() for tokenized_article in tokenized_articles]


def stem_tokens(lowercase_tokenized_articles):
    stemmer = PorterStemmer()
    return [stemmer.stem(lowercase_tokenized_article) for lowercase_tokenized_article in lowercase_tokenized_articles]


def remove_stopwords(stemmed_tokens, stopwords_list):
    return [stemmed_token for stemmed_token in stemmed_tokens if stemmed_token not in stopwords_list]


def read_stopwords_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def write_pipeline_stage_to_file(stage_output, stage_name, article_number):
    full_path = os.path.join('processed_output', f"{stage_name}-output-{article_number}.txt")
    with open(full_path, "w") as f:
        for line in stage_output:
            f.write(f"{line}\n")
