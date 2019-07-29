#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing findspark and initializing 
import findspark
findspark.init('/home/ec2-user/spark')


# In[2]:


# Importing pyspark
import pyspark
from pyspark import SparkContext


# In[3]:


# Calling SparkContext 
sc = SparkContext()


# In[4]:


# Creating a pair RDD
my_tuple = [('Harsh',20), ('Ankit',21), ('Harshit',22)]
regular_rdd = sc.parallelize(my_tuple)


# In[5]:


# Applying Transformations on Pair RDDs
# We have to pass functions that operate on key value pairs rather than on individual elements.
# Examples of pair RDD transformation -
    # reduceByKey(func)  - Combine values with the same key.
    # sortByKey()  -  Return an RDD sorted by the key.
    # groupByKey()  -  Group values with the same key.
    # join()  -  Join two pair of RDDs based on their key.


# In[6]:


# Applying reduceByKey() Transformation
# Creating Key value pair RDD with duplicate keys
my_list = [("Harsh",20), ("Ankit",21), ("Harshit",22), ("Harsh",15)]
my_rdd = sc.parallelize(my_list)

# passing function that add values of keys that are similar.
pairRDD_reducebykey = my_rdd.reduceByKey(lambda x,y : x + y) 
pairRDD_reducebykey.collect()


# In[7]:


# Applying sortByKey() Transformation
    # Sorting the "key"..
pairRDD_sortbykey = regular_rdd.sortByKey(ascending=True) # Sorts in Ascending order.
pairRDD_sortbykey.collect()


# In[8]:


# Sorting the "value"
x = regular_rdd.map(lambda x: (x[1], x[0])) # Reverse the list and creates new RDD.
y = x.sortByKey(ascending=False)  # Sorts in Descending order.
y.collect()


# In[11]:


# Applying groupByKey() Transformation
pairRDD_groupbykey = my_rdd.groupByKey().collect()
for key,value in pairRDD_groupbykey:
    print(key,list(value))


# In[10]:


# Applying join() Transformation
rdd1 = sc.parallelize([("Harsh",20), ("Ankit",21), ("Harshit",22)]) # Creating 1st RDD.
rdd2 = sc.parallelize([("Dhruv",19), ("Ankit",26), ("Harsh",28)]) # Creating 2nd RDD.

# Joining RDDs based on their key.
# Only joins the elements that are same in both RDDs.
rdd1.join(rdd2).collect()

