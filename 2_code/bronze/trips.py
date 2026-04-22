from pyspark import pipelines as dp
import pyspark.sql.functions as F

SOURCE_PATH = "s3://goodcabs-mi/trips"


def orders_bronze():
    df = (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("cloudFiles.inferColumnTypes", "true")
        .option("cloudFiles.schemaEvolutionMode", "rescue")
        .option("cloudFiles.maxFilesPerTrigger", 100)
        .load(SOURCE_PATH)
    )

     # Rename the problematic column
    df = df.withColumnRenamed(
        "distance_travelled(km)",
        "distance_travelled_km"
    )

    df = df.withColumn("file_name", F.col("_metadata.file_path")).withColumn("ingest_datetime", F.current_timestamp())

    return df
