from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("Word-count-book")
sc = SparkContext(conf= conf)

words = sc.textFile("data/Book.txt").flatMap(lambda x: x.split())
word_counts = words.countByValue()

for word, count in word_counts.items():
    clean_word = word.encode("ascii", "ignore")
    if clean_word:
        print(f"{word} - {count}")