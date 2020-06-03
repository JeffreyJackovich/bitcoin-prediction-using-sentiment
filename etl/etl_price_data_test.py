
from pyspark.sql import SparkSession
from pytest import fixture

CORRECT_HEADERS = [
"Unnamed: 0",
"date",
"Open",
"High",
"Low",
"Close",
"Volume_(BTC)",
"Volume_(Currency)",
"Weighted_Price"]

@fixture(scope='session')
def spark_session():
	spark = SparkSession.builder \
		.master("local[*]") \
		.appName("Simple etl job") \
		.getOrCreate()

	return spark

def test_spark_session(spark_session):
	assert spark_session, "SparkSession does not exist"
# def test_column_headers(spark_session):
# 	df = spark_session.read.format("csv").option("header", "true").load("test_data/test_btc_price.csv")
# 	column_headers = df.schema.names
# 	assert  column_headers == CORRECT_HEADERS, "Column headers error"