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

# -- Dataframe Transformations --
    # select()
    # filter()
    # groupBy()
    # orderBy()
    # dropDuplicates()
    # withColumnRenamed()
    
# -- Dataframe Actions -- 
    # printSchema()
    # head()
    # show()
    # count()
    # columns
    # describe()
# In[7]:


# select() and show() Transformation and action
df_name = df.select("name")
df_name.show(2)


# In[8]:


# filter() Transformation
df_filter = df.filter(df['age'] >20 )  # Filters values where age is greater than 20
df_filter.show()


# In[9]:


# groupBy() and count() Transformation and Action
df_group = df.groupby('age')  # group variables with same values
df_group.count().show()       # counts number of members in group


# In[10]:


# orderBy() Transformations 
df_order = df.orderBy('city')  # Sorts results according to column name
df_order.show()


# In[11]:


# dropDuplicates() Transformations
df_drop = df.select('age','city').drop_duplicates()  # Removes Duplicates
df_drop.show()


# In[12]:


# withColumnRenamed() Transformation
df_rename = df.withColumnRenamed('age','umar')
df_rename.show()


# # Dataframe Actions

# In[15]:


# printSchema() Action -- print the schema of the dataframe
df.printSchema()


# In[18]:


# columns Action -- shows all the columns of the dataframe
df.columns


# In[21]:


# describe() Action -- computes summary statistics of numerical columns in dataframe.
df.describe().show()

# Next we're going to interact with dataframes using SQL and views.. stay tuned :)
