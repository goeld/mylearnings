from pyspark import SparkConf, SparkContext
import re


def normalised_word(text):
    return re.compile(r"\W+", re.UNICODE).split(text.lower())


conf = SparkConf().setMaster("local").setAppName("Word Count by Regular expression")
sc = SparkContext(conf= conf)

all_words = sc.textFile("data/Book.txt")
valid_words = all_words.flatMap(normalised_word)
word_counts = valid_words.countByValue()
for word, count in word_counts.items():
    print(f"{word} {count}")


