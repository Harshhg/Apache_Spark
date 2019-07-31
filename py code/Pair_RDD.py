#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Importing findspark and initializing 
import findspark
findspark.init('/home/ec2-user/spark')


# In[6]:


# Importing pyspark
import pyspark
from pyspark import SparkContext


# In[5]:


# Calling SparkContext 
sc = SparkContext()


# In[7]:


# Pair RDD --- RDD in key:value pair.
# Creating pair RDD from key-value tuple

my_tuple = [('Harsh',20), ('Ankit',21), ('Harshit',22)]
pair_rdd_tuple = sc.parallelize(my_tuple)


# In[10]:


# Printing
pair_rdd_tuple.collect()


# In[39]:


# Creating pair RDD from Regular RDD
my_list = ['Harsh 20', 'Ankit 21', 'Harshit 22']
regular_rdd = sc.parallelize(my_list)
pair_rdd_list = regular_rdd.map(lambda s : (s.split(' ')[0],  s.split(' ')[1]) )  


# In[40]:


# Printing
pair_rdd_list.collect()

