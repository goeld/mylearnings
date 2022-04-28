from pyspark.sql import SparkSession, Row

spark_session = SparkSession.builder.appName("Teenage-App").getOrCreate()
lines = spark_session.sparkContext.textFile("../../data/fakefriends.csv")

# for line in lines.collect():
#     print(line)


def line_mapper(line: str):
    fields = line.split(",")
    row: Row = Row(ID=int(fields[0]), name=fields[1], age=int(fields[2]), num_friends=int(fields[3]) )
    return row


people = lines.map(line_mapper)

df_people = spark_session.createDataFrame(people).cache()
df_people.createOrReplaceTempView("people")

teenagers = spark_session.sql("select * from people where age>=13 and age <= 19")

for t in teenagers.collect():
    print(f"Teenager : {t}")

df_people.groupby("age").count().orderBy("age").show()
spark_session.stop()