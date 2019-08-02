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


# Now creating a RDD..
data = [("Apple",2019,90000) , ("Xiaomi", 2018, 30000), ("Samsung",2017, 40000)]
rdd = sc.parallelize(data)


# In[5]:


# Creating schema for the table as a list
names = ['Model', 'Year', 'Price']


# In[6]:


# Creating SparkSession, because it is the entry point to create Dataframes.
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Myapp").config("spark.some.config.option","some-value").getOrCreate()


# In[7]:


# Now creating dataframe from RDD
df = spark.createDataFrame(rdd,names)  # We are passing rdd and schema 
df.show() # Displaying the dataframe


# In[8]:


# Next we're going to create dataframes using CSV/TXT/JSON format.. stay tuned :)

