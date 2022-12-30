# Databricks notebook source
from src.pysparktools.databricks import deltaTable

# COMMAND ----------

deltbl = deltaTable()

# COMMAND ----------

assert deltbl.IAmHere() == 'I am here', 'Function IAmHere not found'
print('Class deltaTable import successfully')
