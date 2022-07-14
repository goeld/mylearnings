package com.learning.spark.dataframes;

import com.learning.spark.schemas.Schemas;
import org.apache.spark.SparkConf;
import org.apache.spark.sql.Column;
import org.apache.spark.sql.DataFrameReader;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.StructType;

public class PopularMovies {

    public static void main(String[] args) {
        SparkConf conf = new SparkConf();
        conf.setMaster("local");
        SparkSession spark = SparkSession.builder()
                .config(conf)
                .appName("Java-Popular-Movies").getOrCreate();
        StructType schema = Schemas.Popular_Movies();

        Dataset<Row> df = spark.read()
                .option("sep", "\t")
                .schema(schema)
                .csv("/Volumes/aadi/workspace/mylearnings/SparkCourse/ml-100k/u.data");

        Dataset<Row> sorted = df.groupBy("movieId").count()
                .orderBy("count")
        ;
        sorted.show((int) sorted.count());
        df.printSchema();


    }

}
