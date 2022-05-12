package com.learning.spark.schemas;

import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

import java.util.ArrayList;
import java.util.List;

public class Schemas {


    public static StructType Popular_Movies() {
        List<StructField> fields = new ArrayList<>();
        fields.add(DataTypes.createStructField("customerId", DataTypes.IntegerType, true));
        fields.add(DataTypes.createStructField("movieId", DataTypes.IntegerType, true));
        fields.add(DataTypes.createStructField("rating", DataTypes.IntegerType, true));
        fields.add(DataTypes.createStructField("timestamp", DataTypes.LongType, true));

        return DataTypes.createStructType(fields);
    }

}
