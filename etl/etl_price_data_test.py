from etl_price_data import load_df_without_schema

from pyspark.sql import SparkSession
from pytest import fixture

@fixture
def spark_session():
	spark = SparkSession.builder \
		.master("local[*]") \
		.appName("pytest-pyspark-local-testing") \
		.getOrCreate()

	return spark

def test_column_headers(spark_session):
	df = spark.read.format("csv").option("header", "true").load("data/processed_btc_prices_ohlcvvw_2014-12-01_to_2018-11-11.csv")

    assert df.schema.names == CORRECT_HEADERS, "Column headers error"