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


# In[5]:


# Calling SparkContext 
sc = SparkContext()


# In[13]:


# --- reduce() action ---
# Used for aggregating the elements of a regular RDD
x = [1,2,3,4,5]
rdd = sc.parallelize(x,3)  # Creates RDD with 3 partitions
# This function will sum all the elements of rdd
rdd.reduce(lambda x , y: x+y)


# In[15]:


# --- saveAsTextFile() action ---
# Saves RDD into a text file inside a directory with each partition as a seperate file.
rdd.saveAsTextFile("tmpfile")  # tmpfile - name of the directory that is created...

# this directory will contain the RDD stored as text files.
# If RDD is created with multiple partitions, directory will have that number of files.


# In[19]:


# To save multiple partitioned RDD into 1 text file we use coalesce method.
rdd.coalesce(1).saveAsTextFile("myrdd1")  # Will save all rdd partitions in 1 file.
rdd.coalesce(2).saveAsTextFile("myrdd2")  # Will save all rdd partitions in 2 file.


# In[41]:


# Pair RDDs Advance Actions
    # countByKey()  -  counts the number of elements for each key.(key count)
    # collectAsMap() - returns the key value pairs in the RDD as a dictionary.


# In[42]:


# Applying countByKey() action.
rdd = sc.parallelize([("a",1), ("b",2), ("a",3),("c",6),("a",5)])
new_rdd = rdd.countByKey()  # returns number of keys count.
new_rdd


# In[43]:


# Printing in better way
for key, value in new_rdd.items():
    print(key,value)


# In[50]:


# Applying collectAsMap() action.
# This will return the pair RDD in dictionary format. Default is list.
new_rdd = rdd.collectAsMap()  
print(new_rdd)
type(new_rdd)


# In[49]:


# Default collec() action.
# Return value as list
new_rdd = rdd.collect()
print(new_rdd)
type(new_rdd)

