from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def clean_orders(df: DataFrame) -> DataFrame:
    return df.fillna({"quantity": 0, "price": 0.0})

def add_total_amount(df: DataFrame) -> DataFrame:
    return df.withColumn("total_amount",
        F.col("quantity") * F.col("price"))

def add_order_grade(df: DataFrame) -> DataFrame:
    return df.withColumn("order_grade",
        F.when(F.col("total_amount") > 1500, "High")
         .when(F.col("total_amount") > 500, "Medium")
         .otherwise("Low"))

def transform_orders(df: DataFrame) -> DataFrame:
    df = clean_orders(df)
    df = add_total_amount(df)
    df = add_order_grade(df)
    return df