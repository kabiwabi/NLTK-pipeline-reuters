from pipeline import *

CONFIG = {
    'file_path': "reuters21578.tar.gz",
    'extract_path': "extracted_gzip",
    'stopwords_file': "Stopwords-used-for-output.txt",
    'output_folder': 'processed_output'
}


def main():
    download_nltk_resources()
    stop_words_list = read_stopwords_from_file(CONFIG['stopwords_file'])

    # Read & extract all the news articles from the TAR file
    read_tar_file(CONFIG['file_path'], CONFIG['extract_path'])
    filtered_files = filter_files_in_directory(CONFIG['extract_path'], r'reut2-\d+.sgm')

    # Store only the <Text> elements from the HTML
    articles = []
    for file_name in filtered_files:
        file_path = os.path.join(CONFIG['extract_path'], file_name)
        html_content = read_html_from_file(file_path)
        articles.extend(extract_text_from_html(html_content))

    # Step 1: Save original articles before processing
    for i, article in enumerate(articles[:5]):
        # Create the directory for outputs if it doesn't already exist
        full_path = os.path.join('processed_output', f"Original-Article-{i + 1}.txt")
        with open(full_path, "w", encoding='utf-8') as f:
            f.write(article)

    # Step 2: Tokenize all articles
    tokenized_articles = tokenize(articles[:5])

    for i, tokenized_articles in enumerate(tokenized_articles):
        write_pipeline_stage_to_file(tokenized_articles, 'Tokenized', i + 1)

        # Step 3: Lowercase all articles
        lowercase_articles = to_lowercase(tokenized_articles)
        write_pipeline_stage_to_file(lowercase_articles, 'Lowercased', i + 1)

        # Step 4: Stem all articles
        stemmed_articles = stem_tokens(lowercase_articles)
        write_pipeline_stage_to_file(stemmed_articles, 'Stemmed', i + 1)

        # Step 5: Remove stopwords for all articles
        stopwords_removed_articles = remove_stopwords(stemmed_articles, stop_words_list)
        write_pipeline_stage_to_file(stopwords_removed_articles, 'Stopwords Removed', i + 1)


if __name__ == "__main__":
    main()
