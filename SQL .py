import sqlite3

# Create database
con = sqlite3.connect("data.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE students(
id INTEGER,
name TEXT,
marks INTEGER
)
""")

# Insert data
cur.execute("INSERT INTO students VALUES(1,'Rahul',80)")
cur.execute("INSERT INTO students VALUES(2,'Priya',90)")
cur.execute("INSERT INTO students VALUES(3,'Arjun',70)")
cur.execute("INSERT INTO students VALUES(4,'Sneha',85)")

con.commit()

# SELECT
print("All Students:")
for row in cur.execute("SELECT * FROM students"):
    print(row)

# WHERE
print("\nMarks above 80:")
for row in cur.execute(
    "SELECT name,marks FROM students WHERE marks > 80"
):
    print(row)

# ORDER BY
print("\nStudents by Marks:")
for row in cur.execute(
    "SELECT name,marks FROM students ORDER BY marks DESC"
):
    print(row)

# AVG
print("\nAverage Marks:")
print(cur.execute(
    "SELECT AVG(marks) FROM students"
).fetchone()[0])

# MAX
print("\nHighest Marks:")
print(cur.execute(
    "SELECT MAX(marks) FROM students"
).fetchone()[0])

con.close()

print("\nSQL TASK COMPLETED")