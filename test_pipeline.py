import unittest
from pipeline import tokenize, to_lowercase, stem_tokens, remove_stopwords


class PipelineUnitTests(unittest.TestCase):

    def test_tokenize(self):
        articles = ["Foo Bar Foo Bar", "Bar Foo Bar Foo"]
        tokenized = tokenize(articles)
        self.assertEqual(tokenized, [["Foo", "Bar", "Foo", "Bar"], ["Bar", "Foo", "Bar", "Foo"]])

    def test_to_lowercase(self):
        tokenized_articles = ["FOO", "BAR"]
        lowercase = to_lowercase(tokenized_articles)
        self.assertEqual(lowercase, ["foo", "bar"])

    def test_stem_tokens(self):
        lowercase_tokenized_articles = ["jumping", "flying"]
        stemmed = stem_tokens(lowercase_tokenized_articles)
        self.assertEqual(stemmed, ["jump", "fli"])

    def test_remove_stopwords(self):
        stemmed_tokens = ["the", "foo", "bar", "the", "it"]
        stopwords_list = ["the"]
        stopwords_removed = remove_stopwords(stemmed_tokens, stopwords_list)
        self.assertEqual(stopwords_removed, ["foo", "bar", "it"])