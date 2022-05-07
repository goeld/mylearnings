from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import functions as func


fake_friends_schema = StructType([
    StructField("id", IntegerType()),
    StructField("name", StringType()),
    StructField("age", IntegerType()),
    StructField("friends", IntegerType()),
])


# spark_session = SparkSession.builder.appName("Avg-Friends-by-age-without-rdd").getOrCreate()
#
# df_friends = spark_session.read.option("inferSchema", "true").option("header", "true")\
#     .format("csv").csv("../../data/fakefriends-header.csv")
#
#
# df_friends.select(df_friends.age, df_friends.friends).groupBy("age")\
#     .avg("friends").show()
#

spark_session = SparkSession.builder.appName("Avg-Friends-by-age-without-rdd").getOrCreate()

df_friends = spark_session.read.option("inferSchema", "true").option("header", "false")\
    .schema(fake_friends_schema)\
    .format("csv").csv("../../data/fakefriends.csv")


df_friends.select(df_friends.age, df_friends.friends).groupBy("age")\
    .agg(func.round(func.avg("friends"), 2).alias("Friends Average"))\
    .sort("age").show()

# df_friends.show()