# For two Dataframes that have the same number of rows, merge all columns, row by row.

# Get the function monotonically_increasing_id so we can assign ids to each row, when the
# Dataframes have the same number of rows.
from pyspark.sql.functions import monotonically_increasing_id

#Create some test data with 3 and 4 columns.
df1 = sqlContext.createDataFrame([("foo", "bar","too","aaa"), ("bar", "bar","aaa","foo"), ("aaa", "bbb","ccc","ddd")], ("k", "K" ,"v" ,"V"))
df2 = sqlContext.createDataFrame([("aaa", "bbb","ddd"), ("www", "eee","rrr"), ("jjj", "rrr","www")], ("m", "M" ,"n"))

# Add increasing Ids, and they should be the same.
df1 = df1.withColumn("id", monotonically_increasing_id())
df2 = df2.withColumn("id", monotonically_increasing_id())

# Perform a join on the ids.
df3 = df2.join(df1, "id", "outer").drop("id")
df3.show()
