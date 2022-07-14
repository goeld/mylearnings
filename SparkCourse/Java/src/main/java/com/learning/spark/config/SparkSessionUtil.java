package com.learning.spark.config;

import org.apache.spark.SparkConf;
import org.apache.spark.sql.SparkSession;

public class SparkSessionUtil {

    private SparkConf conf = new SparkConf();
    private SparkSession sparkSession;

    public SparkSessionUtil(){
        conf.setMaster("local");
    }

    public SparkConf getDefaultConfig() {
        return conf;
    }

    public SparkSession getSparkSession(){
        conf = getDefaultConfig();
        sparkSession = SparkSession.builder().config(conf).getOrCreate();
        return sparkSession;
    }
}
