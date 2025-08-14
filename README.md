# SALES DATA ANALYSIS README

## PROJECT OVERVIEW
A Python script that extracts sales data from MySQL, analyzes product performance, and generates visual reports.

## DELIVERABLES
- Script.py : main python script in which query has written with bar chart plotting.
- sales_data.sql : it is created using mysql for small database generation then loaded to pycharm.
- sales_data.csv : it is optional but created that is why i uploaded, it is also created using python.
- revenue_by_product.png : this is the image of my bar chart.

## PREREQUISITES
1. MySQL Server installed and running.
2. Database: sales_data_db (ensure this database is created).
3. Table structure (sales) within the sales_data_db:
   - product (VARCHAR)
   - quantity (INT)
   - price (DECIMAL)
   - sale_date (DATE - optional)

## REQUIREMENTS
- Python 3.x
- Required packages:
  - pandas
  - matplotlib
  - sqlalchemy
  - mysql-connector-python

## WORKFLOW

### 1. DATA EXTRACTION
- Connects to the MySQL database (sales_data_db).
- Runs aggregation query:
  * Groups by product.
  * Calculates total quantity.
  * Calculates revenue (quantity × price).

### 2. DATA PROCESSING
- Converts results to Pandas DataFrame.
- Prints formatted summary table.

### 3. VISUALIZATION
- Generates a professional bar chart:
  * Products on X-axis.
  * Revenue on Y-axis.
  * Value labels on bars.
  * Gridlines for readability.
  * Responsive layout.

### 4. OUTPUTS
1. revenue_by_product.png
   - Saved to D:/sql+python/
   - High resolution (300dpi).
   
2. sales_summary.csv (optional)
   - Contains aggregated data.
   - Saved when the user confirms.

## CUSTOMIZATION
- Modify database credentials.
- Adjust chart styles/colors.
- Change output directory.
- Update SQL query.

## TROUBLESHOOTING
1. Can't connect?
   - Verify MySQL service status.
   - Check login credentials.

2. Missing packages?
   - Run pip install for required packages.

3. File not saving?
   - Verify directory exists.
   - Check write permissions.

4. Empty results?
   - Confirm data exists in the sales table.
   - Check field names match the query.
