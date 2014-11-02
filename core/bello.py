__author__ = 'aligajani'
# MIT License: www.aligajani.com

# bello.py
# Bello: Text Miner

import re
import nltk
from nltk.corpus import stopwords


class Bello:

    # Deal globally
    global stopset

    # Load relevant components
    # param: language

    def __init__(self, language, file_path, corpus_name):

        # Load corpus data
        self.file_read = self.__load(language, file_path)

        # Print a generic headline
        print("Statistical Analysis of ", corpus_name)
        print("Bello version 0.1")
        print("Corpus language:", language, "\n")

        # Filtering Controls
        basic_filtering = self.__filter(self.file_read)
        advanced_filtering = self.__remove_stopwords(basic_filtering)

        # Filter level list
        self.level = [basic_filtering, advanced_filtering]

        print("{0} {1}: {2}".format("Total words in ", corpus_name, len(basic_filtering)))
        print("{0} {1}: {2}".format("Total distinct words in ", corpus_name, len(set(basic_filtering))))

        print("{0} {1} {2} {3}".format("Total words in ", corpus_name, "[stopwords removed]: ", len(advanced_filtering)))
        print("{0} {1} {2} {3}".format("Total distinct words in ", corpus_name, "[stopwords removed]: ", len(set(advanced_filtering))))
        print("\n")

    # Load stopset and corpora
    # param: language

    def __load(self, language, file_path):

        # Global Stopset
        global stopset

        # Load relevant corpus
        file_name = file_path
        file_open = open(file_name, 'r')
        file_read = file_open.read()

        # Load corpora stopset
        if language is "arabic":
            stopset = set(line.strip() for line in open('data/arabic-stopwords.txt'))
        elif language is "english":
            stopset = set(stopwords.words('english'))

            # For english corpus only
            stopset.add('p')
            stopset.add('section')

        # Return the corpus
        return file_read

    # Basic filtering
    # param: fr, corpus itself

    def __filter(self, fr):

        # Apply regex filter
        filter_lowercase = fr.lower()
        regex = re.compile('[%s]' % re.escape("!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"))

        # Apply extra filter
        filter_lowercase_punctuation = regex.sub('', filter_lowercase)
        filter_lowercase_punctuation_digits = ''.join(i for i in filter_lowercase_punctuation if not i.isdigit())

        # Convert corpus to a list
        filter_lowercase_punctuation_digits_list = filter_lowercase_punctuation_digits.split()

        # Return filtered list: level basic
        return filter_lowercase_punctuation_digits_list

    # Advanced filtering
    # param: filtered, basic filtered list

    def __remove_stopwords(self, filtered):

        # Remove stopwords
        corpus_minus_filters_stopwords = [i for i in filtered if i not in stopset]

        # Return filtered list: level advanced
        return corpus_minus_filters_stopwords

    # Count word frequency of corpus
    # param: level of filtering, plot yes or no, text print count, plot word count

    def word_frequency(self, filter_level, plot_boolean=False, print_count=100, word_count=50):

        # Word Frequency
        word_frequency_fdist = nltk.FreqDist(self.level[filter_level])
        word_frequency = word_frequency_fdist.most_common(print_count)
        print("Most commonly occurring words: ")

        for i in word_frequency:
            print([i])

        if plot_boolean is True:
            word_frequency_fdist.plot(word_count)

        print("\n")

    # Count longest words in corpus
    # param: level of filtering, length of word

    def long_words(self, filter_level, length=15):

        # Long Words
        long_words = [w for w in self.level[filter_level] if len(w) > length]
        print("The longest words: ")

        for i in sorted(long_words):
            print([i])

        print("\n")

    # Bigram frequency counter
    # param: level of filtering, plot yes or no, text print count, plot word count

    def bigram_analysis(self, filter_level, plot_boolean=False, print_count=100, word_count=50):

        # Bi-gram analysis
        b_gram = list(nltk.bigrams(self.level[filter_level]))
        b_gram_freq_fd = nltk.FreqDist(b_gram)
        b_gram_freq = b_gram_freq_fd.most_common(print_count)

        print("Most frequent bi-grams: ")

        for i in b_gram_freq:
            print([i])

        if plot_boolean is True:
            b_gram_freq_fd.plot(word_count)

        print("\n")

    # Trigram frequency counter
    # param: level of filtering, plot yes or no, text print count, plot word count

    def trigram_analysis(self, filter_level, plot_boolean=False, print_count=100, word_count=50):

        # Tri-gram analysis
        t_gram = list(nltk.trigrams(self.level[filter_level]))
        t_gram_freq_fd = nltk.FreqDist(t_gram)
        t_gram_freq = t_gram_freq_fd.most_common(print_count)

        print("Most frequent tri-grams: ")

        for i in t_gram_freq:
            print([i])

        if plot_boolean is True:
            t_gram_freq_fd.plot(word_count)

        print("\n")

    # Word length frequency distrbution
    # param: level of filtering, plot yes or no

    def word_length(self, filter_level, plot_boolean=False):

        # Word Length Frequency Distribution
        fdist = nltk.FreqDist(len(qq) for qq in self.level[filter_level])
        fdist_c = fdist.most_common()
        print("Most common word lengths: ")

        for i in fdist_c:
            print([i])

        if plot_boolean is True:
            fdist.plot()

        print("\n")

    # Dispersion plot
    # param: level of filtering, keywords for dispersion, search string

    def dispersion_plot(self, filter_level, keywords):

        # Dispersion Plot
        text1 = nltk.Text(self.level[filter_level])
        text1.dispersion_plot(keywords)

    # Search for a keyword
    # param: level of filtering, search query

    def search_word(self, filter_level, string):

        # Search with concordance
        text1 = nltk.Text(self.level[filter_level])
        print(string, "appears ", text1.count(string), " times")
        print(text1.concordance(string))


