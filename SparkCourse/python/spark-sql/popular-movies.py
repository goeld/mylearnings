from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql.types import StructType, StructField, IntegerType, LongType
from pyspark.sql.functions import col

schema = StructType([
    StructField("customerId", IntegerType(), False),
    StructField("movieId", IntegerType(), False),
    StructField("rating", IntegerType(), False),
    StructField("timeStamp", LongType(), False),
])

spark_session = SparkSession.builder.appName("App").getOrCreate()
df_input = spark_session.read.schema(schema).option("sep", "\t").csv("../../ml-100k/u.data")
popular_movies = df_input.groupBy("movieId").count().orderBy(col("count"))

popular_movies.show(popular_movies.count())


spark_session.stop()
