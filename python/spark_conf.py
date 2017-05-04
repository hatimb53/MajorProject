import os
import sys

os.chdir("/home/hatim/Documents/workspace/MajorProject/python")
os.curdir

if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME']='/usr/local/spark'
    
SPARK_HOME = os.environ['SPARK_HOME']

sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib"))   
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","pyspark.zip"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","py4j-0.10.1-src.zip"))

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext
from pyspark.streaming import StreamingContext
from pyspark.ml.linalg import Vectors


from pyspark.ml.feature import StringIndexer

class Spark:
	def __init__(self):
			
		self.conf=SparkConf()
		self.conf.set("spark.executer.memeory","1g")
		self.conf.set("spark.cores.max","2")

		self.conf.setAppName("My first")

		self.sc=SparkContext('local',conf=self.conf)
		self.ssc = StreamingContext(self.sc,2)
		self.sqlContext=SQLContext(self.sc)

		


 