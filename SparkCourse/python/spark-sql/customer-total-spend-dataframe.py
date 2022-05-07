from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType
from pyspark.sql.functions import col, round, sum
from datetime import datetime


schema = StructType([
    StructField("customerId", IntegerType(), True),
    StructField("orderId", IntegerType(), True),
    StructField("spend", FloatType(), True)
])
conf = SparkConf()

conf.set("spark.executor.memory", '8g')
conf.set('spark.executor.cores', '5')
conf.set('spark.cores.max', '3')
conf.set("spark.driver.memory", '8g')
conf.set("spark.driver.memory", '8g')


spark_session = SparkSession.builder.appName("Customer spend total using dataframe").config(conf=conf).getOrCreate()

start = datetime.now()

orders = spark_session.read.schema(schema).option("mergeSchema", True).csv("../../data/customer-orders.csv")

schema = orders.schema;
schema_time = (datetime.now() - start).total_seconds()
print(f"Schema_time : {schema_time}")


ordersByCustomer = orders.groupBy(orders.customerId)\
    .agg(round(sum(col("spend")), 2)).alias("total_spend")\
    .sort(orders.customerId)

date1 = datetime.now()

ordersByCustomer.show(ordersByCustomer.count())

date2 = datetime.now()

first_diff = (date1 - start).total_seconds()
second_diff = (date2 - date1).total_seconds()

print(f"Date1 : {first_diff}, second diff: {second_diff}")


spark_session.stop()