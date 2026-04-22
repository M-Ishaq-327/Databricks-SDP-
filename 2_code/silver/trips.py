from pyspark import pipelines as dp
from pyspark.sql import functions as F


def trips_silver():
    df_bronze = spark.readStream.table("transportation.bronze.trips")
    df_silver = df_bronze.withColumn("passenger_type", F.lower("passenger_type"))

    df_silver = df_bronze.select(
        F.col("trip_id").alias("id"),
        F.col("date").cast("date").alias("business_date"),
        F.col("city_id").alias("city_id"),
        F.col("passenger_type").alias("passenger_category"),
        F.col("distance_travelled_km").alias("distance_kms"),
        F.col("fare_amount").alias("sales_amt"),
        F.col("passenger_rating").alias("passenger_rating"),
        F.col("driver_rating").alias("driver_rating"),
        F.col("ingest_datetime").alias("bronze_ingest_timestamp"),
    )
