# data-analyst-task-3
# SQL Database Operations Using Python

## Project Description

This project demonstrates basic SQL database operations using Python and SQLite.

The program creates a student database, stores student details, and performs different SQL operations such as SELECT, WHERE, ORDER BY, AVG, and MAX.

## Technologies Used

- Python
- SQLite
- sqlite3
- Pydroid 3

## Database

Database Name:

`data.db`

## Table

Table Name:

`students`

Columns:

- `id` - Student ID
- `name` - Student Name
- `marks` - Student Marks

## Operations Performed

### 1. Create Database

Python's `sqlite3` module is used to create and connect to the database.

### 2. Create Table

A `students` table is created with ID, name, and marks columns.

### 3. Insert Data

Four student records are inserted:

| ID | Name | Marks |
|---|---|---|
| 1 | Rahul | 80 |
| 2 | Priya | 90 |
| 3 | Arjun | 70 |
| 4 | Sneha | 85 |

### 4. SELECT

Displays all student records from the table.

### 5. WHERE

Finds students whose marks are greater than 80.

**Result:**
- Priya - 90
- Sneha - 85

### 6. ORDER BY

Sorts students according to marks in descending order.

**Result:**
1. Priya - 90
2. Sneha - 85
3. Rahul - 80
4. Arjun - 70

### 7. AVG

Calculates the average marks.

**Average Marks:** 81.25

### 8. MAX

Finds the highest marks.

**Highest Marks:** 90

### 9. Commit

The `commit()` function saves the changes made to the database.

### 10. Close Database

The `close()` function closes the database connection after completing all operations.
