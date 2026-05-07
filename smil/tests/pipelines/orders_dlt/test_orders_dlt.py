def test_row_count(actual_df):
    assert actual_df.count() == 10, "Expected 10 rows"

def test_column_count(actual_df):
    assert len(actual_df.columns) == 8, "Expected 8 columns"

def test_data_match(actual_df, expected_df):
    actual = actual_df.orderBy("order_id").collect()
    expected = expected_df.orderBy("order_id").collect()
    assert actual == expected, "Data does not match"