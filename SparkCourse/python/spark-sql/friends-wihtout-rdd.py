from pyspark.sql import SparkSession, DataFrame

spark_session = SparkSession.builder.appName("Spark-SQL-Without RDD").getOrCreate()
df_people = spark_session.read.option("header", True).option("inferSchema", True)\
    .csv("../../data/fakefriends-header.csv")


df_people.printSchema()
df_people.filter(df_people.age > 13).show()
df_people.groupBy(df_people.age).count().orderBy(df_people.age).show()
df_people.select(df_people.name, df_people.age).filter(df_people.age > 68).show()
df_people.select(df_people.name, df_people.age + 10).filter(df_people.age > 68).show()
spark_session.stop()