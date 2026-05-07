import pytest

@pytest.fixture(scope="session")
def actual_df(spark):           
    return spark.read.table("smil_catalog.smil_schema.orders_gold")

@pytest.fixture(scope="session")
def expected_df(spark):
    data = [
        (1001, "John Smith",       "Laptop", 2, 999.99, "Active",   1999.98,           "High"),
        (1002, "Sarah Johnson",    "Phone",  1, 599.99, "Active",   599.99,            "Medium"),
        (1003, "Michael Williams", "Tablet", 0, 449.99, "Active",   0.0,               "Low"),
        (1004, "Emily Brown",      "Laptop", 3, 999.99, "Inactive", 2999.9700000000003,"High"),
        (1005, "David Jones",      "Phone",  2, 0.0,    "Active",   0.0,               "Low"),
        (1006, "Jessica Garcia",   "Tablet", 1, 449.99, "Active",   449.99,            "Low"),
        (1007, "Daniel Martinez",  "Laptop", 0, 999.99, "Active",   0.0,               "Low"),
        (1008, "Ashley Davis",     "Phone",  3, 599.99, "Inactive", 1799.97,           "High"),
        (1009, "James Rodriguez",  "Tablet", 2, 449.99, "Active",   899.98,            "Medium"),
        (1010, "Amanda Wilson",    "Laptop", 1, 999.99, "Active",   999.99,            "Medium"),
    ]
    schema = ["order_id", "customer_name", "product", "quantity",
              "price", "status", "total_amount", "order_grade"]
    return spark.createDataFrame(data, schema)