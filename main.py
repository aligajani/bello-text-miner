
# Bello: Text Miner
# By Ali Gajani (www.aligajani.com)

from core.bello import Bello

# Bello load and supply language
quran = Bello("english", "data/quran-english.txt", "Quran")

# To run your code: python main.py > result.txt
quran.search_word(0, "muhammad")
