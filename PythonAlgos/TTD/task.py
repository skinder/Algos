import aws as aws
import boto3
import botocore
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import hadoop-aws

BUCKET_NAME='sa-data-engineering-exercise'
AWS_KEY='AKIAWJ4POKDXO3PJGMOV'
AWS_SECRET_KEY='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'

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id=AWS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

#spark = SparkSession.builder.appName("TTD").getOrCreate()

sc=SparkContext()
hadoopConf = sc.hadoopConfiguration()

spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "mykey")
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "mysecret")


dataframe = spark.createDataFrame(data, columns)
dataframe.show()

'''

for obj in s3.Bucket(BUCKET_NAME).objects.all():
    print(obj)


try:
    s3.Bucket(BUCKET_NAME).download_file('wwo3pza/reds/date=2021-07-23/hour=5/2021-07-235impressions0.gz', '2021-07-235impressions0.gz')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
'''
