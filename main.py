import os
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

from article_pipeline import read_extract_text, tokenize, to_lowercase, stem_tokens, remove_stopwords, \
    write_pipeline_stage_to_file


def main():
    file_path = "reuters21578.tar.gz"
    extract_path = "extracted_gzip"
    stop_word_list = stopwords.words('english')

    articles = read_extract_text(file_path, extract_path)

    # Create directory for original articles if it doesn't exist
    if not os.path.exists('processed_output'):
        os.makedirs('processed_output')

    # Step 1: Save original articles before processing
    for i, article in enumerate(articles[:5]):
        # Create the full path for the output file within the 'original_articles' directory
        full_path = os.path.join('processed_output', f"Original-Article-{i + 1}.txt")
        with open(full_path, "w", encoding='utf-8') as f:
            f.write(article)

    # Step 2: Tokenize all articles
    tokenized_articles = tokenize(articles[:5])

    for i, tokenized_articles in enumerate(tokenized_articles):
        write_pipeline_stage_to_file(tokenized_articles, 'Tokenized', i + 1)

        lowercase_articles = to_lowercase(tokenized_articles)
        write_pipeline_stage_to_file(lowercase_articles, 'Lowercased', i + 1)

        stemmed_articles = stem_tokens(lowercase_articles)
        write_pipeline_stage_to_file(stemmed_articles, 'Stemmed', i + 1)

        stopwords_removed_articles = remove_stopwords(stemmed_articles, stop_word_list)
        write_pipeline_stage_to_file(lowercase_articles, 'Stopwords Removed', i + 1)


if __name__ == "__main__":
    main()