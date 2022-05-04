from pyspark.sql import SparkSession
from pyspark.sql import functions as func

spark_session = SparkSession.builder.appName("Word count using Spark Data Frames").getOrCreate()
lines = spark_session.read.text("../../data/Book.txt")
words = lines.select(func.explode(func.split(lines.value, "\\W+")).alias("word"))
words.printSchema()
words.filter(words.word != "")
words.groupBy(words.word).count().sort("count").show(words.count())
spark_session.stop()