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


# In[10]:


# Creating a DataFrame from csv,txt,json file.

df = spark.read.csv("/home/ec2-user/wc.csv" , header=True, inferSchema=True)
#dftxt = spark.read.text("/home/ec2-user/wc.txt")  # For TEXT file
#dfjson = spark.read.json("/home/ec2-user/wc.csv") # For JSON file

# header=True -- means it will take the first line of csv file as header or column name
# inferSchema=True -- fetches the schema of the table. 


# In[11]:


# Displaying the dataframe values
df.show()
dftxt.show()


# In[ ]:


# Next we're going to perform some operations on DATAFRAMES.. stay tuned :)

