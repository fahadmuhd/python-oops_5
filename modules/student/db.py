import sqlite3
 
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()
 
# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(20),
        date_of_birth VARCHAR(20),
        age INTEGER,
        gender VARCHAR(10),
        mobile_number INT,
        email_address VARCHAR(20) UNIQUE,
        password VARCHAR(25),
        preferred_language VARCHAR(20),
        school_college_name VARCHAR(50),
        class_grade VARCHAR(10),
        board_curriculum VARCHAR(20),
        academic_year VARCHAR(10),
        tuition_subjects TEXT NOT NULL DEFAULT '[]',
        subject_levels TEXT NOT NULL DEFAULT '[]',
        topics_needing_help TEXT NOT NULL DEFAULT '[]',
        parent_guardian_name VARCHAR(20),
        parent_guardian_relationship VARCHAR(20),
        parent_guardian_mobile_number INT
    );
""")
cursor.execute("""
    INSERT INTO students (
        full_name,
        date_of_birth,
        age,
        gender,
        mobile_number,
        email_address,
        password,
        preferred_language,
        school_college_name,
        class_grade,
        board_curriculum,
        academic_year
    )
    VALUES (
        'MUHAMMED Fahad',
        '2006-09-20',
        20,
        'male',
        9562688002,
        'fahadm265627@gmail.com',
        'fahada2145',
        'malayalam',
        'ilahia',
        'A',
        'nill',
        '2025'
    )
""")

# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")