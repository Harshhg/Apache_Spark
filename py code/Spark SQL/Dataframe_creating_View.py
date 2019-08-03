#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init('/home/ec2-user/spark')


# In[2]:


import pyspark
from pyspark import SparkContext


# In[3]:


sc = SparkContext()


# In[4]:


# Creating SparkSession bcoz this is the entry point to create DataFrame..
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("My App").config("spark.some.config.option", "some-value").getOrCreate()


# In[5]:


# Creating a DataFrame from csv file.
df = spark.read.csv("/home/ec2-user/wc.csv" , header=True, inferSchema=True)
df.show()
# header=True -- means it will take the first line of csv file as header or column name
# inferSchema=True -- fetches the schema of the table. 


# In[6]:


# Register the dataframe as SQL temporary view (creating table)
df.createOrReplaceTempView("student")

# This view is temporary(session-scoped) will disappear if session is terminated.


# In[7]:


# Now we can programmaticaly run SQL queries..
sqldf = spark.sql("select * from student")
sqldf.show()


# In[8]:


# To create temporary view that is shared across all sessions and keep alive till spark application terminates - 
# We will create GlobalTemporary view.
df.createGlobalTempView("st")


# In[9]:


# To use the global temporary view, we have to use it with name "global_temp.nameofview"
sqldf = spark.sql("select * from global_temp.st")
sqldf.show()


# In[10]:


# To check the global temporary view in cross sessions, we are creating new session
spark.newSession().sql("select * from global_temp.st").show()


# In[13]:


# Now lets perform some SQL operations using spark
query1 = " Select * from student where age > 20"
query2 = "Select * from student order by age"


# In[14]:


spark.sql(query1).show()
spark.sql(query2).show()

