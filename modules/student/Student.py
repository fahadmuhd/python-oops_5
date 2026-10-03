class studentClass:
    def __init__(self):
        self.full_name = ''
        self.date_of_birth = ''
        self.age = ''
        self.gender = ''
        self.mobile_number = ''
        self.email_address = ''
        self.password = ''
        self.preferred_language = ''
        self.school_college_name = ''
        self.class_grade = ''
        self.board_curriculum = ''
        self.academic_year = ''
        self.subjects_for_tuition = []
        self.current_level_per_subject = {}
        self.areas_topics_needing_help = []
        self.parent_guardian_name = ''
        self.parent_guardian_relationship = ''
        self.parent_guardian_mobile_number = ''
        self.parent_guardian_email_address = ''
        self.preferred_comcommunication_method = ' '


    def setfullname_dob_gender_mobile(self, full_name, date_of_birth, gender, mobile_number):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.mobile_number = mobile_number

    def save_to_database(self):
        import sqlite3
        conn = sqlite3.connect("tution.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (full_name, date_of_birth, age, gender, mobile_number, email_address, password, preferred_language, school_college_name, class_grade, board_curriculum, academic_year)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.full_name, self.date_of_birth, self.age, self.gender, self.mobile_number, self.email_address, self.password, self.preferred_language, self.school_college_name, self.class_grade, self.board_curriculum, self.academic_year))
        conn.commit()
        conn.close()