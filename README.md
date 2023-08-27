# Mainframe DB2 Database Population Script

This repository contains a Python script designed to populate a Mainframe DB2 database. This Python script generates `CREATE TABLE` statements and `INSERT` statements using information from TXT files. Additionally, it creates a new TXT file with these generated statements, which can be uploaded from the console to the Mainframe environment for execution.

## Background

Populating a Mainframe DB2 database with data often involves creating the required table structures and inserting data into those tables. This process can be time-consuming and error-prone when done manually. To automate and streamline this process, the Python script in this repository generates the necessary SQL statements based on the data provided in a TXT file.

## Prerequisites

Before using the script, ensure you have the following:

- Python 3.x installed on your system.
- Access to a Mainframe environment with DB2 database capabilities.
- A TXT file containing the data you want to populate the database with.

### Script Overview

The script performs the following steps:

1. **Reading Data from TXT Files:** The script reads data from TXT files containing information about tables, columns, data types, and values.

2. **Data Processing and Statement Generation:** It processes the data and generates `CREATE TABLE` statements and `INSERT` statements based on the extracted information.

3. **Writing Statements to a TXT File:** The generated statements are written to a new TXT file, which can be later uploaded to the Mainframe for populating the DB2 database.

### Getting Started

1. Clone this repository to your local machine.

2. Ensure you have Python installed (version 3.x).

3. Prepare your TXT files with the required table information and data.

4. Run the `main.py` script using the command:
   ```
   python main.py
   ```

5. The script will generate `INSERT` statements and write them to the `insert_result.txt` file.

6. Upload the `insert_result.txt` file from your local machine to the Mainframe system.

## Example

For example data in `data.txt`:

```
Name, Age, Occupation
John Doe, 30, Engineer
Jane Smith, 25, Analyst
```

Running the script will generate SQL statements like:

```sql
CREATE TABLE PEOPLE (
    ID INT NOT NULL PRIMARY KEY,
    NAME VARCHAR(255),
    AGE INT,
    OCCUPATION VARCHAR(255)
);

INSERT INTO PEOPLE (ID, NAME, AGE, OCCUPATION)
VALUES (1, 'John Doe', 30, 'Engineer');

INSERT INTO PEOPLE (ID, NAME, AGE, OCCUPATION)
VALUES (2, 'Jane Smith', 25, 'Analyst');
```

### Disclaimer

This script is provided as-is and may require modification to suit your specific environment and requirements. Make sure to review and test the generated statements before executing them on your Mainframe DB2 database.

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request.
