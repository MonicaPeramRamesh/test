import dlt
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from transformations import transform_orders

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
    return transform_orders(dlt.read("orders_raw"))  ← one line! ✅