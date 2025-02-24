import pymssql
import xml.etree.ElementTree as ET

# Database connection details
SERVER = "LAPTOP-7GM89BAS"
DATABASE = "CompanyDB"
USERNAME = "sa"
PASSWORD = "NewPassword123"  # Use your correct password

# Connect to SQL Server
try:
    conn = pymssql.connect(
        server=SERVER,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE,
        port=1433,  # Ensure connection via port 1433
        autocommit=True  # Enable auto-commit
    )
    cursor = conn.cursor()
    print("✅ Connected to SQL Server successfully!")
except Exception as e:
    print("❌ Failed to connect:", e)
    exit()

# Close connection
conn.close()
