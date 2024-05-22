import sys
import pandas as pd

filename = sys.argv[1]

df = pd.read_csv(filename)

pivot_table = pd.pivot_table(df, values="quantity", 
                             index="name", 
                             columns="product", 
                             aggfunc='count')

print (pivot_table)

with pd.ExcelWriter("salesrecords.xlsx") as writer:
    df.to_excel(writer) 

print ("finished")