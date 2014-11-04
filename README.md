##Bello: Text Miner

Bello is a lightweight text mining library for Python 3. It allows a text mining enthusiast like you to get up and running with analysing the corpus of your choice. Text mining is fun and we want beginners to not be put away by the high learning curve.

We expose core text mining features through a dead-simple API that you will start to love. A gentle reminder though: this is a work in progress and contributors are welcome. Bello was born out of a mini-research project on Text Mining 'The Holy Quran'. The work can be seen [here](http://bit.ly/QuranStat1).

###API documentation v0.1

####Requirements

* Python 3+
* NLTK 2.0

####Installation

To install Bello, simply clone this repository and start playing around with the `main.py`. The documentation is thorough, give it a read or two. The core functionality lives in `bello.py` in the `core` directory.

####Documentation

To boot up Bello, you must do the following in your `main.py`.

`from core.bello import Bello`

Then, to initialize the facility, do as follows. Remember, we are supplying you with a corpora of the Holy Quran in English and Arabic, so you can test things if you wish. Therefore, the example code in the documentation will refer to this dataset.

`quran = Bello("english", "data/quran-english.txt", "Quran")`

The `Bello()` constructor takes in **3 arguments**, in order:

`Bello(language, file_path, corpus_name)`. All are required.

Once you have got this far, we can perform text mining with Bello. Let the games begin.

#### Filter Levels

Bello implements two levels of filtering, which can be configured with a 0 or a 1.

###### Basic Filtering

Basic filtering filters a corpus for punctuation and digits. To use basic filtering, use `0` for the `filter_level` argument.

###### Advanced Filtering

Bello also implements an advanced level of filtering, which tops up the basic filter with stopword removal. To use the advanced filter, use `1` for the `filter_level` argument.

### Word Frequency Distributions

This allows you to find out the most used words in a corpus. Of course, you must supply one corpus at a time. To text mine word frequency distributions, Bello provides a very neat API, as shown below.

`word_frequency(filter_level, plot_boolean=False, print_count=100, word_count=50):`

You **must** supply the `filter_level`. Other arguments are optional [defaulted].

`plot_boolean` can be set to `True` if you wish to create a plot for the word frequency distrbutions.

`print_count` controls how many words are printing in the console.

`word_count` controls how many words are plotted on the graph.

For example, you can do the following:

* `quran.word_frequency(1)` would give you the top 100 words in your chosen corpus. Since the `plot_boolean` is set to `False` by default, nothing will be plotted, and hence, the `word_count` doesn't get into effect.

* `quran.word_frequency(1, True)` would give you the top 100 words in your chosen corpus, and also, it will plot for you 50 of them on a plot. Remember, you can over ride any of the integers to your liking.

* `quran.word_frequency(1, True, 25, 10)` is an example of complete customisation. You override the last 3 arguments. Basically, you tell Bello, hey, plot the word frequency distributions, do a text dump of top 25 words on console and don't forget to plot top 10 words on the plot.

**Note**: Keep these arguments in mind, as they are used further in the API.



### Long Words

You can find out the longest words in your chosen corpus using `long_words()`. The default length of the word is `15`, but you can over ride that.

This is the API generally: `long_words(filter_level, length=15)`

`quran.long_words(1)` or for customization `quran.long_words(1, 5)`

The only requirement is the first argument, which is the `filter_level`. It makes sense to use `filter_level` of `1` since stopwords aren't all that long anyway.


### Bigram Analysis

Bigrams are sequence of two words. You can count the bigram frequency of your corpus to see which two words appear together in sequence the most. Bello makes this process a cinch [dead simple]. Here's how you mine your corpus for bigram frequency.

`bigram_analysis(filter_level, plot_boolean=False, print_count=100, word_count=50)`

The same API rules apply for `bigram_analysis` as we explored for `word_frequency`.


### Trigram Analysis

Trigrams are sequence of three words. You can count the trigram frequency of your corpus to see which three words appear together in sequence the most. Bello makes this process a cinch [dead simple]. Here's how you mine your corpus for trigram frequency.

`trigram_analysis(filter_level, plot_boolean=False, print_count=100, word_count=50)`

The same API rules apply for `trigram_analysis` as we explored for `bigram_analysis`.

### Word Length

You can use Bello to figure out the most common word lengths. The API is simple:

`quran.word_length(filter_level, plot_boolean=False)`

Doing `quran.word_length(1)` would give you something like this below. This is using the advanced filter of `filter_level` set to `1` which filters your corpus for stopwords.

	Most common word lengths:
	[(4, 16778)]
	[(5, 13168)]
	[(6, 10340)]
	[(3, 9375)]

Let's see what happens when you use a `filter_level` of `0`, which is a basic filter, and does not filter your corpus for stopwords.

As you can see the most common word length is `3` which is probably understandble to due to the large number of **the** in the corpus. Although `False` by default, you can wish to plot this data.

	Most common word lengths:
	[(3, 41869)]
	[(4, 37017)]
	[(2, 33338)]
	[(5, 18445)]


### Dispersion Plots

Dispersion plots are fun because they can show you a journey of words in a large cosmos of a corpus. Well, that sounded poetic.

Anyway: for example, you want to see [visually] the number of times a word has appeared in a corpus, and more importantly, at which offset from the start. If yes, then the dispersion plot is your friend.

The API for using the dispersion plot is simple: `dispersion_plot(self, filter_level, keywords)`

All the arguments are required. `keywords` must be a **list** like `["james", "joe", "john"]`

### Search Word

You can use Bello to perform a basic keyword search by supplying a search query. The API is simply: `search_word(filter_level,string)`.

When we set a `filter_level` of `0` to ensure stopwords are included [to make sense of sentences], and a string of `"muhammad"`, we get the following. It gives you a count of the times a word appeared in a corpus in addition to its context using a concordance view.

	muhammad appears  4  times
	Displaying 4 of 4 matches:
	our own eyes and ye flinch section muhammad is no more than an apostle many we
	ough is god to call men to account muhammad is not the father of any of your m
	hose who transgress p p sura xlvii muhammad the prophet in the name of god mos
	on and enough is god for a witness muhammad is the apostle of god and those wh

#### License

The MIT License (MIT)

Copyright (c) <2014> Ali Gajani [aligajani.com]('http://www.aligajani.com')

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
