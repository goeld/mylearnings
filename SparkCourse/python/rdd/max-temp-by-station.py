from pyspark import SparkConf, SparkContext


class ParseUtility:

    def parseLine(self, line: str) -> (str, str, float):
        fields = line.split(",")
        station_id = fields[0]
        temperature_type = fields[2]
        temperature = float(fields[3])
        return station_id, temperature_type, temperature


class MaxTemperatureByStation:

    def __init__(self):
        spark_conf = SparkConf().setMaster("local").setAppName("Max-Temperature-By-Station")
        self.spark_context = SparkContext(conf=spark_conf)

    def calculate_max_temperature(self, file_path: str):
        lines = self.spark_context.textFile(file_path)
        filtered_results = lines.map(ParseUtility().parseLine)
        rdd = filtered_results.filter(lambda x: 'TMAX' in x[1]).map(lambda x: (x[0], x[2]))
        max_temp_station = rdd.reduceByKey(lambda x, y: max(x, y))
        results = max_temp_station.collect()
        for result in results:
            station = result[0]
            temperature = result[1] * 0.1 * (9.0 / 5.0) + 32
            print(f"{station} - {temperature}")
            print(station + "\t{:.2f}".format(temperature))


MaxTemperatureByStation().calculate_max_temperature("data/1800.csv")