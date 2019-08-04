#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the findspark
import findspark


# In[2]:


# Initializing the spark directory with findspark
findspark.init('/home/ec2-user/spark')


# In[3]:


# Importing pyspark
import pyspark


# In[4]:


# Importing SparkContext
from pyspark import SparkContext


# In[5]:


# Creating the spark context
sc = SparkContext()


# In[6]:


# We are creating our first RDD using parallelize method
data = [1,2,3,4,5]
rdd = sc.parallelize(data)


# In[16]:


# Applying Transformation on RDD
# Map transformation
rdd_map = rdd.map(lambda x : x * x) # It applies the function to all elements in the RDD


# In[18]:


# Filter Transformation
rdd_filter = rdd.filter(lambda x : x > 3)  # Returns the RDD with only the elements that pass the condition.


# In[21]:


# flatMap Transformation
# Returns multiple values for each element in the original RDD
    
newrdd = sc.parallelize(["Hello World", "how are you"])  # This RDD contains two elements
rdd_flatmap = newrdd.flatMap(lambda x: x.split(" "))  # This will return new RDD with 5 elements


# In[29]:


# Union Transformation 
# Takes input 2 RDD and returns union of 1 RDD with 2 RDD
input_rdd = sc.parallelize(['error 1', 'warning 1', 'error 2','warning 2'])  # Creating a RDD
error_rdd = input_rdd.filter(lambda x : 'error' in x.split())  # 1st filter transformation
warning_rdd = input_rdd.filter(lambda x : 'warning' in x.split())  # 2nd filter transformation
combine_rdd = error_rdd.union(warning_rdd)  # Taking union of RDD 1 and 2


# In[31]:


# ----  RDD Actions  ---- 
# collect()  ,   take()  ,  first(),   count()


# In[34]:


# First() action
rdd_map.first()  # Prints the first element of rdd created earlier.


# In[35]:


# Count() action
rdd_flatmap.count()  # Counts the elements of rdd.


# In[36]:


# collect() action
# Prints all the elements of new RDD
rdd_map.collect()  


# In[37]:


rdd_filter.collect()


# In[38]:


rdd_flatmap.collect()


# In[39]:


combine_rdd.collect()


# In[41]:


# take() action
# Returns an array with the first n elements of the dataset
rdd_map.take(3)  # Prints 3 elements


# In[43]:


rdd_flatmap.take(4)  # Prints 4 elements

