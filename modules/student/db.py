import sqlite3
from pathlib import Path




database_path = Path(__file__).with_name('student.db')
# Path(__file__) → gets the path of the current Python file.

# .with_name('student.db') → replaces the current filename with student.db.

connection = sqlite3.connect(database_path)

connection.execute(
    '''
    CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        date_of_birth_or_age TEXT,
        gender TEXT,
        mobile_number TEXT,
        email_address TEXT
    )
    '''
)
connection.commit()

connection.close()