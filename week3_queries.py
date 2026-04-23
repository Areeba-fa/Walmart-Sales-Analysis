import sqlite3
import pandas as pd

conn = sqlite3.connect('walmart_data.db')

# Hint 1: Understand the table
print("--- SQL: First 5 Rows ---")
query1 = "SELECT * FROM sales LIMIT 5;"
print(pd.read_sql(query1, conn))

# Hint 2: Aggregations (Top stores by total revenue)
print("\n--- SQL: Top Stores by Total Revenue ---")
query2 = """
SELECT Store, SUM(Weekly_Sales) as Total_Revenue 
FROM sales 
GROUP BY Store 
ORDER BY Total_Revenue DESC 
LIMIT 5;
"""
print(pd.read_sql(query2, conn))

conn.close()