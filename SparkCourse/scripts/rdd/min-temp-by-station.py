from pyspark import SparkConf, SparkContext


class ParseUtility:

    def parseLine(self, line: str) -> (str, str, float):
        fields = line.split(",")
        station_id = fields[0]
        temperature_type = fields[2]
        temperature = float(fields[3])
        return station_id, temperature_type, temperature


class MinTemperatureByStation:

    def __init__(self):
        spark_conf = SparkConf().setMaster("local").setAppName("Minimum-Temperature-by-Station")
        self.spark_context = SparkContext(conf=spark_conf)

    def calculate_minimum_temperature(self, file_path: str):
        lines = self.spark_context.textFile(file_path)
        filtered_results = lines.map(ParseUtility().parseLine).filter(lambda x: 'TMIN' in x[1]).map(lambda x: (x[0], x[2]))
        min_temp = filtered_results.reduceByKey(lambda x, y: min(x, y))
        results = min_temp.collect()
        for result in results:
            print(result)


temperature = MinTemperatureByStation()
temperature.calculate_minimum_temperature("data/1800.csv")

