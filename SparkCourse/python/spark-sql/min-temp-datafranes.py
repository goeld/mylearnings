from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col, round

spark_session = SparkSession.builder.appName("Minimum Temperature by Spark Session").getOrCreate()

schema = StructType([
    StructField("stationId", StringType(), True),
    StructField("date", IntegerType(), True),
    StructField("type", StringType(), True),
    StructField("temperature", IntegerType(), True),
])

df = spark_session.read.schema(schema).csv("../../data/1800.csv")
df = df.filter(df.type == "TMIN").groupBy("stationId").min("temperature")
results = df.withColumn("temperatureS",
                        round(col("min(temperature)") * 0.1 * ((9.0 / 5.0) + 32.0), 2)) \
    .select("stationId", "temperatureS") \
    .sort("temperatureS").collect()

for result in results:
    print(f"{result.stationId} : {result.temperatureS}")

spark_session.stop()
