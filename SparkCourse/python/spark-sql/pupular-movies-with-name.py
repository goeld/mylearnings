from pyspark import SparkContext
from pyspark.sql import SparkSession, functions as f
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import codecs


schema = StructType([
    StructField("customerId", IntegerType(), True),
    StructField("movieId", IntegerType(), True),
    StructField("rating", IntegerType(), True),
    StructField("timestamp", IntegerType(), True),
])

spark = SparkSession.builder.appName("Popular movies with Title").getOrCreate()
all_movies = spark.read.schema(schema).option("sep", "\t").csv("../../ml-100k/u.data")
all_movies.show()


def loadMoviesNames():
    movies = {}
    with codecs.open("../../ml-100k/u.item", "r", encoding="ISO-8859-1", errors="ignore" ) as file:
        for line in file:
            fields = line.split("|")
            movies[int(fields[0])] =  fields[1]

    return movies


nameDict = spark.sparkContext.broadcast(loadMoviesNames())


def lookupName(movieId):
    return nameDict.value[movieId]


lookupNameUdf = f.udf(lookupName)

movie_counts = all_movies.groupBy("movieId").count().orderBy("count", ascending=False)
movies_with_title = movie_counts.withColumn("Movie_Name", lookupNameUdf(f.col("movieId")) )
movies_with_title.show(10)