from dataclasses import dataclass

from pyspark import SparkConf, SparkContext


@dataclass(init=True)
class ParseFakeFriendUtil:

    def parse_line(self, line: str) -> (int, int):
        fields = line.split(",")
        age = int(fields[2])
        no_of_friends = int(fields[3])
        return age, no_of_friends


class AverageFriendsByAge:

    def __init__(self):
        spark_config = SparkConf().setMaster("local").setAppName("AverageFriendsByAgeExample")
        self.spark_context = SparkContext(conf=spark_config)

    def calculate_average_by_friends_age(self):
        lines = self.spark_context.textFile("data/fakefriends.csv")
        ff = ParseFakeFriendUtil()
        rdd_ff = lines.map(ff.parse_line)
        totalsByAge = rdd_ff.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
        averageByNumbers = totalsByAge.mapValues(lambda x: x[0] / x[1])
        results = averageByNumbers.collect()
        for age, average_friends in results:
            print(f"Age={age}, Average Age= {average_friends}")
        print("Successfully executed")


avg_friends_age = AverageFriendsByAge();
avg_friends_age.calculate_average_by_friends_age()
