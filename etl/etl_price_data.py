#import psycopg2

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, LongType, TimestampType, ShortType, DateType
from pyspark.sql.functions import isnan, when, count, col


CORRECT_HEADERS = [
    "date",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume_(BTC)",
    "Volume_(Currency)",
    "Weighted_Price"]


def initialize_spark():

    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("Simple etl job") \
        .getOrCreate()

    print("Spark Initialized", "\n")

    return spark


def load_df_without_schema(spark):

    df = spark.read.format("csv").option("header", "true").load("data/test_btc_price.csv")
    return df


spark = initialize_spark()
df = load_df_without_schema(spark)



