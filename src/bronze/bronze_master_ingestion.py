from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

spark = SparkSession.builder.appName("Bronze Master Ingestion").getOrCreate()

file_path="data/raw/customers.csv"
# Read the CSV file into a DataFrame
df=spark.read.option("header",true)\
    .option("inferSchema",true)\
    .csv(file_path)
df.show(5)
target_path = "dbfs:/mnt/lakehouse/bronze/customers"

df.write.format("delta").mode("overwrite").save(target_path)
print("Data ingested successfully into the Bronze layer.")

