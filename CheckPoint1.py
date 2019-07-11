#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyspark
import time 
import os
import csv
from numpy import array
from pyspark import SparkContext, SparkConf


# In[2]:


wf1 = spark.read.csv("weather01.txt", inferSchema = True, header = True)
wf2 = spark.read.csv("weather02.txt", inferSchema = True, header = True)
wf3 = spark.read.csv("weather03.txt", inferSchema = True, header = True)
wf4 = spark.read.csv("weather04.txt", inferSchema = True, header = True)
wf5 = spark.read.csv("weather05.txt", inferSchema = True, header = True)
wf6 = spark.read.csv("weather06.txt", inferSchema = True, header = True)


# In[ ]:




