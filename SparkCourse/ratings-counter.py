from pyspark import SparkConf, SparkContext
import collections

class RatingHistogram:

    def __init__(self):
        conf = SparkConf().setMaster("local").setAppName("my-rating-historgram")
        self.sc = SparkContext(conf=conf)


    def load_rating(self, file_path):
        lines = self.sc.textFile(file_path)
        ratings = lines.map(lambda x: x.split()[2])
        results = ratings.countByValue()
        sortedResults = collections.OrderedDict(sorted(results.items()))
        for key, value in sortedResults.items():
            print(f"{key} - {value}")


ratingHistogram = RatingHistogram()
ratingHistogram.load_rating("ml-100k/u.data")
