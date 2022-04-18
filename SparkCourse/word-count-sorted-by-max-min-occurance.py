from pyspark import SparkConf, SparkContext
import collections
import re


def normalised_words(line: str):
    return re.compile(f"\W+", re.UNICODE).split(line.lower())


conf = SparkConf().setMaster("local").setAppName("Word Count sorted by minimum and maximum occurrence")
sc = SparkContext(conf=conf)

input = sc.textFile("data/Book.txt")
words = input.flatMap(normalised_words)

word_counts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
word_count_sorted = word_counts.map(lambda x: (x[1], x[0])).sortByKey()
results = word_count_sorted.collect()

for count, word in results:
    print(f"{word} \t\t: {count}")
