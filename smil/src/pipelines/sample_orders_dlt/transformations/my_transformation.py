import dlt
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

@dlt.table(
    name="orders_raw",
    comment="Raw orders data ingested from volume"
)
def orders_raw():
    schema = StructType([
        StructField("order_id", IntegerType(), True),
        StructField("customer_name", StringType(), True),
        StructField("product", StringType(), True),
        StructField("quantity", IntegerType(), True),
        StructField("price", DoubleType(), True),
        StructField("status", StringType(), True)
    ])
    return (
        spark.read.format("csv")
            .option("header", "true")
            .schema(schema)
            .load("/Volumes/smil_catalog/smil_schema/smil_volume/orders.csv")
    )


@dlt.table(
    name="orders_gold",
    comment="Cleaned and transformed orders data"
)
def orders_gold():
    return (
        dlt.read("orders_raw")
            .fillna({"quantity": 0, "price": 0.0})
            .withColumn("total_amount",
                F.col("quantity") * F.col("price"))
            .withColumn("order_grade",
                F.when(F.col("total_amount") > 1500, "High")
                 .when(F.col("total_amount") > 500, "Medium")
                 .otherwise("Low"))
    )