import sqlite3
from pathlib import Path

SAMPLE_EMPLOYEES = [
    (1001, 'Amit', 'Sharma', 'M', '1990-05-12', 'amit.sharma@example.com', '9998887776', 1, '2019-06-01'),
    (1002, 'Priya', 'Verma', 'F', '1992-08-21', 'priya.verma@example.com', '9998887775', 2, '2020-03-15'),
    (1003, 'Rahul', 'Kumar', 'M', '1985-11-02', 'rahul.kumar@example.com', '9998887774', 1, '2018-10-10'),
]

SAMPLE_DEPARTMENTS = [
    (1, 'Finance', 'Mumbai', 'R. Menon'),
    (2, 'Engineering', 'Bengaluru', 'S. Kapoor'),
]

SAMPLE_SALARY = [
    (1, 1001, 120000.0, 10000.0, 130000.0, '2025-10'),
    (2, 1002, 90000.0, 5000.0, 95000.0, '2025-10'),
    (3, 1003, 140000.0, 15000.0, 155000.0, '2025-10'),
]

SAMPLE_ATTENDANCE = [
    (1, 1001, '2025-10-01', 'Present'),
    (2, 1002, '2025-10-01', 'Absent'),
    (3, 1003, '2025-10-01', 'Present'),
]

SAMPLE_PROJECTS = [
    (1, 'Titan', 'Payment gateway upgrade', '2024-01-01', None),
    (2, 'Aurora', 'Mobile app rework', '2024-05-01', None),
]

SAMPLE_PROJECT_MAP = [
    (1, 1, 1001, 'Lead'),
    (2, 1, 1003, 'Developer'),
    (3, 2, 1002, 'Developer'),
]


def create_and_seed_db(db_path: str):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create tables
    c.executescript('''
    CREATE TABLE IF NOT EXISTS department (
        department_id INTEGER PRIMARY KEY,
        dept_name TEXT,
        location TEXT,
        manager_name TEXT
    );

    CREATE TABLE IF NOT EXISTS employee_details (
        emp_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        gender TEXT,
        dob TEXT,
        email TEXT,
        phone TEXT,
        department_id INTEGER,
        joining_date TEXT,
        FOREIGN KEY(department_id) REFERENCES department(department_id)
    );

    CREATE TABLE IF NOT EXISTS employee_salary (
        salary_id INTEGER PRIMARY KEY,
        emp_id INTEGER,
        base_salary REAL,
        bonus REAL,
        total_salary REAL,
        month TEXT,
        FOREIGN KEY(emp_id) REFERENCES employee_details(emp_id)
    );

    CREATE TABLE IF NOT EXISTS employee_attendance (
        att_id INTEGER PRIMARY KEY,
        emp_id INTEGER,
        date TEXT,
        status TEXT,
        FOREIGN KEY(emp_id) REFERENCES employee_details(emp_id)
    );

    CREATE TABLE IF NOT EXISTS employee_projects (
        proj_id INTEGER PRIMARY KEY,
        proj_name TEXT,
        proj_desc TEXT,
        start_date TEXT,
        end_date TEXT
    );

    CREATE TABLE IF NOT EXISTS employee_project_mapping (
        id INTEGER PRIMARY KEY,
        proj_id INTEGER,
        emp_id INTEGER,
        role TEXT,
        FOREIGN KEY(proj_id) REFERENCES employee_projects(proj_id),
        FOREIGN KEY(emp_id) REFERENCES employee_details(emp_id)
    );
    ''')

    # Insert sample data (idempotent)
    c.executemany('INSERT OR IGNORE INTO department VALUES (?, ?, ?, ?)', SAMPLE_DEPARTMENTS)
    c.executemany('INSERT OR IGNORE INTO employee_details VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', SAMPLE_EMPLOYEES)
    c.executemany('INSERT OR IGNORE INTO employee_salary VALUES (?, ?, ?, ?, ?, ?)', SAMPLE_SALARY)
    c.executemany('INSERT OR IGNORE INTO employee_attendance VALUES (?, ?, ?, ?)', SAMPLE_ATTENDANCE)
    c.executemany('INSERT OR IGNORE INTO employee_projects VALUES (?, ?, ?, ?, ?)', SAMPLE_PROJECTS)
    c.executemany('INSERT OR IGNORE INTO employee_project_mapping VALUES (?, ?, ?, ?)', SAMPLE_PROJECT_MAP)

    conn.commit()
    conn.close()
    print('Database created at:', db_path)