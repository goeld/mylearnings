from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, LongType
from pyspark.sql import  functions as func

schema = StructType([
    StructField("userId", IntegerType(), False),
    StructField("movieId", IntegerType(), False),
    StructField("rating", IntegerType(), False ),
    StructField("timestamp", LongType(), False )
])

spark = SparkSession.builder.appName("My Movie Rating").master("local").getOrCreate()

movie_df = spark.read.schema(schema=schema).option("sep", "\t").csv("../../ml-100k/u.data")
movie_df.show()

df_sorted = movie_df.groupBy("movieId").count().orderBy(func.desc("count"))
df_sorted.show(10)

spark.stop()