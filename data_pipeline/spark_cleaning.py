
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataCleaning").getOrCreate()

# Load data
df = spark.read.csv("telemetry.csv", header=True, inferSchema=True)

# Data cleaning steps
df_cleaned = df.dropna()

df_cleaned.write.csv("cleaned_telemetry.csv", header=True)
            