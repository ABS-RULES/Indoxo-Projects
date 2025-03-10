import pymssql
import xml.etree.ElementTree as ET

# Database connection details
SERVER = "LAPTOP-7GM89BAS"
DATABASE = "CompanyDB"
USERNAME = "sa"  # Change if needed
PASSWORD = "NewPassword123"  # Replace with your actual password

# Connect to SQL Server
try:
    conn = pymssql.connect(SERVER, USERNAME, PASSWORD, DATABASE)
    cursor = conn.cursor()
    print("✅ Connected to SQL Server successfully!")
except Exception as e:
    print("❌ Failed to connect:", e)
    exit()

# Parse XML file
try:
    tree = ET.parse("C:\\Users\\Surya\\Desktop\\Indoxo projects\\Task - 1\\CUsersSuryaDocumentsXML_Projectsample_data.xml.txt")
    root = tree.getroot()
    print("✅ XML file loaded successfully!")
except Exception as e:
    print("❌ Failed to load XML file:", e)
    exit()

# Insert data into SQL Server
for emp in root.findall("employee"):
    aid = int(emp.find("id").text)
    name = emp.find("name").text
    department = emp.find("department").text
    position = emp.find("position").text
    salary = float(emp.find("salary").text)
    hire_date = emp.find("hire_date").text

    # SQL query with placeholders
    sql = "INSERT INTO employees (id, name, department, position, salary, hire_date) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (aid, name, department, position, salary, hire_date)

    try:
        cursor.execute(sql, values)
        print(f"✅ Inserted {name} into database.")
    except Exception as e:
        print(f"❌ Error inserting {name}: {e}")

# Commit and close connection
conn.commit()
cursor.close()
conn.close()
print("✅ Data insertion completed!")
