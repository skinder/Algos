from pyspark.sql import SparkSession

'''
Should be passed as parameters
'''
SQL_CONNECTION = "jdbc:mysql://localhost:3306/Test"
USER = "root"
PASS = "...."
TABLE_NAME = "medals"
MY_SQL_DRIVER="..../mysql-connector-java-8.0.23.jar"

# Define Spark session
spark = SparkSession.builder.appName("Athlete_Events")\
    .config("spark.driver.extraClassPath", MY_SQL_DRIVER) \
    .getOrCreate()

# read json to DataFrame
df = spark.read.json("athlete_events_2006_2016.json")

# Modify DataFrame
df_output = df.filter(df.medal != "null")\
    .groupBy("year","season","team")\
    .count()\
    .groupBy("year","season")\
    .count()\
    .withColumnRenamed("count", "cntry_with_medals")

# Print DataFrame
df_output.show()

'''
2006	Winter	36
2008	Summer	105
2010	Winter	37
2012	Summer	101
2014	Winter	35
2016	Summer	98

'''

# write dataframe to MySQL
df_output.write.format('jdbc').options(
          url=SQL_CONNECTION,
          driver='com.mysql.cj.jdbc.Driver',
          dbtable=TABLE_NAME,
          user=USER,
          password=PASS).mode('overwrite').save()

exit(0)
