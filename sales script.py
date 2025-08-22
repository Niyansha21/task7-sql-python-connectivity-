import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

# Create SQLAlchemy engine
engine = create_engine("mysql+mysqlconnector://root:NewPassword123@localhost/sales_data_db")

# SQL query for aggregated sales data
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# Load data into DataFrame
df = pd.read_sql(query, engine)

# Print DataFrame to verify
print("\n=== Aggregated Sales Data ===")
print(df)  # Shows aggregated results from MySQL

# Plot bar chart for revenue
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart in D:\sql
chart_path = r"D:\sql+python\revenue_by_product.png"
plt.savefig(chart_path)

print(f"Chart saved at: {chart_path}")

# Show chart
plt.show()

# Optional: Save to CSV
# df.to_csv("sales_data.csv", index=False)




