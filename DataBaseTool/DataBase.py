import MySQLdb
import sqlite3

# Database configurations

localhost = '0.0.0.0'
root = 'root'

# Notes
# School Tools


def create_server_db(school_name):
    connections = MySQLdb.connect(localhost, root, '')
    connection = connections.cursor()
    connection.execute(
        f'''
        CREATE DATABASE {school_name}
        '''
    )
    connections.commit()

# create_server_db('MySchool')

def create_school(school_name):
    lite_connection = sqlite3.connect('school.db')
    lite_connection.execute(
        '''
        CREATE TABLE IF NOT EXISTS SchoolTable (
            id INT NOT NULL,
            school_name VARCHAR NOT NULL,
            school_logo BLOB
            )
        '''
    )

    lite_connection.commit()


def insert_school(school_name, image='NULL'):
    lite_connection = sqlite3.connect('school.db')
    lite_connection.execute(
        '''
            INSERT INTO SchoolTable(id, school_name, school_logo)
                    VALUES(?, ?, ?)
        ''', (0, school_name, image)
    )

    lite_connection.commit()


def get_school():
    lite_connection = sqlite3.connect('school.db')
    fetch = lite_connection.execute(
        '''
        SELECT school_name FROM SchoolTable
        '''
    )

    school_name = []
    for i in fetch:
        school_name.append(i[0])

    return school_name[0]


def get_school_logo():
    lite_connection = sqlite3.connect('school.db')
    fetch = lite_connection.execute(
        '''
        SELECT school_logo FROM SchoolTable
        '''
    )

    school_name = []
    for i in fetch:
        school_name.append(i[0])

    return school_name[0]


# Admin Tools


def create_admin():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        CREATE TABLE IF NOT EXISTS AdminTable (
            id INT(20) PRIMARY KEY NOT NULL,
            surname VARCHAR(100) NOT NULL,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            username VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            image_dir BLOB
            )
        '''
    )
    connections.commit()


def insert_admin(id_, s_name, f_name, l_name, username, password, image_dir=''):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        INSERT AdminTable (id, surname, first_name, last_name, username, password, image_dir)
            VALUES (%s, %s, %s, %s, %s, %s, LOAD_FILE(%s))
        ''', (id_, s_name, f_name, l_name, username, password, image_dir)
    )
    connections.commit()


def get_admin_password(username):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT password FROM AdminTable WHERE username = {};
        '''.format(username)
    )
    connections.commit()

    results = connection.fetchall()
    data = []
    for res in results:
        data.append(res)
    return data


def get_admin_by(column):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT {} FROM AdminTable
        '''.format(column)
    )
    connections.commit()

    results = connection.fetchall()
    data = []
    for res in results:
        data.append(res[0])
    return data


def get_admin():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT id, surname, first_name, last_name, username, password FROM AdminTable
        '''
    )
    connections.commit()

    results = connection.fetchall()
    data = []
    for res in results:
        data.append(res)
    return data


def get_admin_image(id_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT image_dir FROM AdminTable WHERE id=%s
        ''', (str(id_))
    )
    connections.commit()

    results = connection.fetchall()
    data = []
    for res in results:
        data.append(res)
    return data


def create_teacher():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        CREATE TABLE IF NOT EXISTS TeachersTable (
            id INT(20) PRIMARY KEY NOT NULL,
            surname VARCHAR(100) NOT NULL,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            gender VARCHAR(10) NOT NULL,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            admin_username VARCHAR(100) NOT NULL,
            admin_password VARCHAR(100) NOT NULL,
            image_dir BLOB
            )
        '''
    )
    connections.commit()

create_teacher()

image = '/RegistrationPages/default.png'


def insert_teacher(id_, s_name, f_name, l_name, gender, username, password, admin_username, admin_password, image_dir=image):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    try:
        connection.execute(
            '''
        INSERT TeachersTable (
        id, 
        surname, 
        first_name, 
        last_name, 
        gender, 
        username, 
        password, 
        admin_username, 
        admin_password, 
        image_dir
        )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, LOAD_FILE(%s))
        ''', (id_, s_name, f_name, l_name, gender, username, password, admin_username, admin_password, image_dir)
        )

        connections.commit()
    except MySQLdb._exceptions.IntegrityError as db_ERR:
        connection.execute(
            '''
        UPDATE TeachersTable 
            SET surname = %s, 
                first_name = %s, 
                last_name = %s, 
                gender = %s, 
                username = %s, 
                password = %s, 
                admin_username = %s, 
                admin_password = %s, 
                image_dir = LOAD_FILE(%s)
            WHERE id = %s 
        ''', (s_name, f_name, l_name, gender, username, password, admin_username, admin_password, image_dir, id_)
        )

        connections.commit()
    except Exception as e:
        raise e


def get_teacher(column):
    try:
        connections = MySQLdb.connect(localhost, root, '', get_school())
        connection = connections.cursor()
        connection.execute(
            '''
            SELECT {} FROM TeachersTable
            '''.format(column)
        )
        connections.commit()

        results = connection.fetchall()
        data = []
        for res in results:
            data.append(res[0])
        return data
    except Exception as e:
        return 'NULL'


def get_teacher_all():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT * FROM TeachersTable
        '''
    )
    connections.commit()

    results = connection.fetchall()
    data = []
    for res in results:
        data.append(res)
        # if res:
        #     image = open(f'UsersFiles/Imgaes/{res[0]}.jpg', 'wb')
        #     image.write(res[-1])
    return data


def get_teacher_all_id():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT id FROM TeachersTable
        '''
    )
    connections.commit()

    results = connection.fetchall()
    data = []
    for res in results:
        data.append(res[0])
    return data


def get_teacher_password(username):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT * FROM TeachersTable WHERE username = %s
        ''', (username)
    )
    connections.commit()

    results = connection.fetchall()
    data = []
    for res in results:
        data.append(res)
    return data


def get_teacher_by(id_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT * FROM TeachersTable WHERE id = %s
        ''', (str(id_))
    )
    connections.commit()

    results = connection.fetchall()
    data = []

    for teacher in results:
        data.append(teacher)
    return data


def get_teacher_id(username):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        ''' SELECT * FROM TeachersTable WHERE id = %s ''', (username)
    )
    connections.commit()

    results = connection.fetchall()
    data = []

    for teacher in results:
        data.append(teacher)
    return data


def get_teacher_names():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT username FROM TeachersTable
        '''
    )
    connections.commit()

    results = connection.fetchall()
    data = []

    for teacher in results:
        data.append(teacher[0])
    return data


def get_teacher_username(username):
    all_usernames = get_teacher_names()
    all_teachers = get_teacher_all()
    if username in all_usernames:
        user_id = all_usernames.index(username)
        return all_teachers[user_id][1], all_teachers[user_id][2]
    else:
        return 'Username doesn\'t exist.'


def delete_teacher(id_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        DELETE FROM TeachersTable WHERE id = %s
        ''', (str(id_))
    )
    connections.commit()


def create_school_class():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        CREATE TABLE IF NOT EXISTS SchoolClass (
            id INT(20) PRIMARY KEY NOT NULL,
            class_name VARCHAR(100) NOT NULL,
            subjects VARCHAR(20) NOT NULL, 
            teacher VARCHAR(200) NOT NULL, 
            username VARCHAR(200) NOT NULL
            )
        '''
    )
    connections.commit()

create_school_class()


def insert_school_class(id_, class_name, subjects, teacher, username):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    try:
        connection.execute(
            '''
            INSERT SchoolClass(id, class_name, subjects, teacher, username)
                VALUES (%s, %s, %s, %s, %s)
            ''', (id_, class_name, subjects, teacher, username)
        )
        connections.commit()
    except MySQLdb._exceptions.IntegrityError as db_ERR:
        connection.execute(
            '''
            UPDATE SchoolClass
                SET class_name = %s, subjects = %s, teacher = %s, username = %s
            WHERE id = %s
            ''', (class_name, subjects, teacher, username, id_)
        )
        connections.commit()
    except Exception as e:
        raise e


def get_school_class_all():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT * FROM SchoolClass
        '''
    )
    connections.commit()

    results = connection.fetchall()
    data = []

    for r in results:
        data.append(r)
    return data


def get_school_class_teacher(class_name):
    print(class_name)
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT username FROM SchoolClass WHERE class_name = %s
        ''', (class_name)
    )
    connections.commit()

    results = connection.fetchall()
    data = []

    for r in results:
        data.append(r)
    return data


def get_school_class_teacher_by_id(id_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f'''
    SELECT username FROM SchoolClass WHERE id = {id_}
        '''
    )
    connections.commit()

    results = connection.fetchall()
    data = []

    for r in results:
        data.append(r[0])
    return data[0]


def get_school_class():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT class_name FROM SchoolClass
        '''
    )
    connections.commit()

    results = connection.fetchall()
    data = []

    for r in results:
        data.append(r[0])
    return data


def delete_school_class(id_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f'''
        DELETE FROM SchoolClass WHERE id = {id_}
        '''
    )
    connections.commit()


def get_class_ids():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        SELECT id FROM SchoolClass
        '''
    )
    connections.commit()

    results = connection.fetchall()
    data = []

    for r in results:
        data.append(r[0])
    return data


def create_class(class_name):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()

    connection.execute(
        f'''
        CREATE TABLE IF NOT EXISTS {class_name} (
            id INT(20) PRIMARY KEY NOT NULL,
            class_name VARCHAR(100) NOT NULL,
            teacher VARCHAR(100) NOT NULL,
            username VARCHAR(100) NOT NULL,
            subject_1 VARCHAR(100),
            subject_2 VARCHAR(100),
            subject_3 VARCHAR(100),
            subject_4 VARCHAR(100),
            subject_5 VARCHAR(100),
            subject_6 VARCHAR(100),
            subject_7 VARCHAR(100),
            subject_8 VARCHAR(100),
            subject_9 VARCHAR(100),
            subject_10 VARCHAR(100),
            subject_11 VARCHAR(100),
            subject_12 VARCHAR(100),
            subject_13 VARCHAR(100),
            subject_14 VARCHAR(100),
            subject_15 VARCHAR(100)
            )
        '''
    )

    connections.commit()


def insert_class(id_, class_name, teacher, username, subject_1='', subject_2='', subject_3='', subject_4='', subject_5='', subject_6='', subject_7='', subject_8='', subject_9='', subject_10='', subject_11='', subject_12='', subject_13='', subject_14='', subject_15=''):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    try:
        connection.execute(
            f'''
            INSERT {class_name}(
            id, 
            class_name, 
            teacher, 
            username, 
            subject_1, 
            subject_2, 
            subject_3, 
            subject_4, 
            subject_5, 
            subject_6, 
            subject_7, 
            subject_8, 
            subject_9, 
            subject_10, 
            subject_11, 
            subject_12, 
            subject_13, 
            subject_14, 
            subject_15)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                id_, 
                class_name, 
                teacher, 
                username, 
                subject_1, 
                subject_2, 
                subject_3, 
                subject_4, 
                subject_5, 
                subject_6, 
                subject_7, 
                subject_8, 
                subject_9, 
                subject_10, 
                subject_11, 
                subject_12, 
                subject_13, 
                subject_14, 
                subject_15)
        )
        connections.commit()
    except MySQLdb._exceptions.IntegrityError as db_ERR:
        connection.execute(
        f'''
        UPDATE {class_name}
            SET class_name = %s,
                teacher = %s,
                username = %s,
                subject_1 = %s,
                subject_2 = %s,
                subject_3 = %s,
                subject_4 = %s,
                subject_5 = %s,
                subject_6 = %s,
                subject_7 = %s,
                subject_8 = %s,
                subject_9 = %s,
                subject_10 = %s,
                subject_11 = %s,
                subject_12 = %s,
                subject_13 = %s,
                subject_14 = %s,
                subject_15 = %s
            WHERE id = %s
        ''', (
            class_name, 
            teacher, 
            username, 
            subject_1, 
            subject_2, 
            subject_3, 
            subject_4, 
            subject_5, 
            subject_6, 
            subject_7, 
            subject_8, 
            subject_9, 
            subject_10, 
            subject_11, 
            subject_12, 
            subject_13, 
            subject_14, 
            subject_15, 
            id_
            )
        )
        connections.commit()
    except Exception as e:
        print(str(e))


def get_class(name):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(f''' SELECT * FROM {name} ''')
    connections.commit()

    res = connection.fetchall()

    data = []
    for d in res:
        for i in d:
            data.append(i)

    return data


def get_class_id(name):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(f''' SELECT id FROM {name} ''')
    connections.commit()

    res = connection.fetchall()

    data = []
    for d in res:
        for i in d:
            data.append(i)

    return data[0]


def get_class_subject(name):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(f''' SELECT subject_1, subject_2, subject_3, subject_4, subject_5, subject_6, subject_7, subject_8, subject_9, subject_10, subject_11, subject_12, subject_13, subject_14, subject_15 FROM {name} ''')
    connections.commit()

    res = connection.fetchall()

    data = []
    for d in res:
        for i in d:
            data.append(i)

    return data


def delete_class(class_name):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(f''' DROP TABLE {class_name} ''')
    connections.commit()


def get_class_teacher(name):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(f''' SELECT teacher FROM {name} ''')
    connections.commit()

    res = connection.fetchall()

    data = []
    for d in res:
        for i in d:
            data.append(i)

    return data[0]


def get_class_sub(name):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(f''' SELECT subject_1, subject_2, subject_3, subject_4, subject_5, subject_6, subject_7, subject_8, subject_9, subject_10, subject_11, subject_12, subject_13, subject_14, subject_15 FROM {name} ''')
    connections.commit()

    res = connection.fetchall()

    data = []
    for d in res[0]:
        data.append(d)

    return data


def create_school_students():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()

    connection.execute(
        '''
        CREATE TABLE IF NOT EXISTS SchoolStudents (
            id INT(20) PRIMARY KEY AUTO_INCREMENT,
            surname VARCHAR(100) NOT NULL,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100),
            class VARCHAR(100) NOT NULL,
            reg_num VARCHAR(100) NOT NULL,
            gender VARCHAR(100) NOT NULL,
            pin VARCHAR(100) NOT NULL,
            UNIQUE Reg_num (reg_num)
            )
        '''
    )

    connections.commit()

create_school_students()


def insert_school_students(id_, surname, first_name, last_name, class_, reg_num, gender, pin):
    try:
        connections = MySQLdb.connect(localhost, root, '', get_school())
        connection = connections.cursor()
        connection.execute(
            f'''
            INSERT SchoolStudents (surname, first_name, last_name, class, reg_num, gender, pin)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (surname, first_name, last_name, class_, reg_num, gender, pin)
        )

        connections.commit()
    except MySQLdb._exceptions.IntegrityError as e:
        connection.execute(
            '''
            UPDATE SchoolStudents 
                SET surname = %s, 
                    first_name = %s, 
                    last_name = %s, 
                    class = %s,
                    reg_num = %s,
                    gender = %s, 
                    pin = %s 
                    WHERE reg_num = %s
            ''', (surname, first_name, last_name, class_, reg_num, gender, pin, reg_num)
            )

        connections.commit()


def get_school_students():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        ''' SELECT * FROM SchoolStudents '''
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d)

    return data

def get_school_students_by_id(id_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f''' SELECT * FROM SchoolStudents WHERE id = {str(id_)}'''
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d)
    if data:
        return data[0]

def get_students_by_column(column):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f''' SELECT {column} FROM SchoolStudents '''
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d[0])

    return data
# print(get_students_by_column('reg_num'))

def delete_school_student(id_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        DELETE FROM SchoolStudents WHERE id = %s
        ''', (str(id_))
    )
    connections.commit()


def create_school_questions():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        CREATE TABLE IF NOT EXISTS SchoolQuestions (
            id INT(200) AUTO_INCREMENT PRIMARY KEY NOT NULL,
            class VARCHAR(50) NOT NULL, 
            subject VARCHAR(500) NOT NULL, 
            teacher VARCHAR(500) NOT NULL, 
            scheduled_time VARCHAR(50) NOT NULL, 
            allocated_time VARCHAR(50) NOT NULL,
            status VARCHAR(10) NOT NULL
            )
        '''
    )
    connections.commit()

def get_school_questions_id(class_, subject):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        ''' SELECT id FROM SchoolQuestions WHERE class = %s AND subject = %s''',
        (class_, subject)
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d[0])
    if data:
        return data[0]

# print(get_school_questions_id('AdvancedLevel', 'Data Science'))

def get_class_id(class_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        ''' SELECT id FROM SchoolQuestions'''
    )
    connections.commit()

    res = connection.fetchall()
    all_ids = []
    for d in res:
        all_ids.append(d[0])

    connection.execute(
        ''' SELECT class FROM SchoolQuestions'''
    )
    connections.commit()

    res = connection.fetchall()
    all_classes = []
    for d in res:
        all_classes.append(d[0])

    index_ = all_classes.index(class_)

    return all_ids[index_]

def get_school_questions_by_id(id_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f''' SELECT * FROM SchoolQuestions WHERE id = {id_} '''
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d)

    return data

def get_school_questions_by_cs(class_, subject):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f''' SELECT * FROM SchoolQuestions WHERE class = %s AND subject = %s ''', (class_, subject)
        #(str(id_))
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d)

    return data

# print(get_school_questions_by_cs('AdvancedLevel', 'Data Science'))

def insert_school_questions(class_, subject, teacher, scheduled_time, allocated_time, status):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    try:
        connection.execute(
            f'''
            INSERT SchoolQuestions(class, subject, teacher, scheduled_time, allocated_time, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (class_, subject, teacher, scheduled_time, allocated_time, status)
        )
        connections.commit()
    except Exception as e:
        raise e

def change_exam_status(class_, subject, status):
    id_ = get_school_questions_id(class_, subject)
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        '''
        UPDATE SchoolQuestions
            SET status = %s
            WHERE id = %s
        ''', (status, id_)
        )
    connections.commit()


def get_school_questions():
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        ''' SELECT * FROM SchoolQuestions'''
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d)

    return data

def get_school_questions_avail(class_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        ''' SELECT * FROM SchoolQuestions WHERE class = %s AND status = %s''',(class_, 'True')
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d[2])

    return data

def get_all_question_ids():
    ids_ = []
    if get_school_questions:
        for id_ in get_school_questions():
            ids_.append(id_[0])
    return ids_

def create_exam_questions(class_, subject):
    if ' ' in subject:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}'
    else:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}'
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT(200) PRIMARY KEY NOT NULL,
            question VARCHAR(400) NOT NULL,
            question_image VARCHAR(100),
            opt_a VARCHAR(500) NOT NULL,
            opt_b VARCHAR(500) NOT NULL,
            opt_c VARCHAR(500) NOT NULL,
            opt_d VARCHAR(500) NOT NULL,
            answer VARCHAR(500) NOT NULL
            )
        '''
    )
    connections.commit()


def insert_exam_questions(class_, subject, id_, question, opt_a, opt_b, opt_c, opt_d, answer, question_image=''):
    if ' ' in subject:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}'
    else:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}'
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    try:
        connection.execute(
            f'''
            INSERT {table_name}(id, question, question_image, opt_a, opt_b, opt_c, opt_d, answer)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (id_, question, question_image, opt_a, opt_b, opt_c, opt_d, answer)
        )
        connections.commit()
    except MySQLdb._exceptions.IntegrityError as db_ERR:
        connection.execute(
            f'''
            UPDATE {table_name}
                SET question = %s, 
                    question_image = %s, 
                    opt_a = %s, 
                    opt_b = %s, 
                    opt_c = %s, 
                    opt_d = %s, 
                    answer = %s
                WHERE id = %s
            ''', (question, question_image, opt_a, opt_b, opt_c, opt_d, answer, id_)
        )
        connections.commit()
    except Exception as e:
        raise e

def get_exam_questions(class_, subject):
    if ' ' in subject:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}'
    else:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}'
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f''' SELECT * FROM {table_name} '''
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d)

    return data

def delete_exam_questions(id_):
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(f''' DELETE FROM SchoolQuestions WHERE id = {id_} ''')
    connections.commit()

def drop_table(table_name):
    try:
        connections = MySQLdb.connect(localhost, root, '', get_school())
        connection = connections.cursor()
        connection.execute(
            f'''DROP TABLE IF EXISTS {table_name}'''
        )
        connections.commit()
    except Exception as e:
        return e

def delete_exam_traces(class_, subject, id_):
    try:
        if ' ' in subject:
            subject = subject.replace(' ', '_')
            table_name = f'{class_}_{subject}'
            table_name1 = f'{class_}_{subject}_Result'
        else:
            subject = subject.replace(' ', '_')
            table_name = f'{class_}_{subject}'
            table_name1 = f'{class_}_{subject}_Result'

        # id_ = get_school_questions_id(class_, subject)

        delete_exam_questions(id_)
        drop_table(table_name1)

        connections = MySQLdb.connect(localhost, root, '', get_school())
        connection = connections.cursor()
        connection.execute(
            f'''DROP TABLE IF EXISTS {table_name}'''
        )
        connections.commit()
    except Exception as e:
        raise e

def create_student_exam_status(class_, subject):
    if ' ' in subject:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    else:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id VARCHAR(200) PRIMARY KEY NOT NULL,
            reg_num VARCHAR(100) NOT NULL,
            subject VARCHAR(100) NOT NULL,
            score VARCHAR(200) NOT NULL,
            exam_status VARCHAR(10) NOT NULL
            )
        '''
    )
    connections.commit()

def insert_student_exam_status(class_, reg_num, subject, score, exam_status):
    if ' ' in subject:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    else:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    id_ = f'{reg_num[-3:]}_{subject}'
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    try:
        connection.execute(
            f''' INSERT {table_name}(id, reg_num, subject, score, exam_status)
                    VALUES(%s, %s, %s, %s, %s)
            ''', (id_, reg_num, subject, score, exam_status)
        )

        connections.commit()
    except MySQLdb._exceptions.IntegrityError as db_ERR:
        return db_ERR
    except Exception as e:
        raise e

# insert_student_exam_status('AdvancedLevel', '2020JKN', 'Data Science', '0', 'False')

def update_exam_status(class_, reg_num, subject, score, exam_status):
    if ' ' in subject:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    else:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    id_ = f'{reg_num[-3:]}_{subject}'
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f''' UPDATE {table_name}
                SET exam_status = %s,
                    score = %s
            WHERE id = %s
        ''', (exam_status, score, id_)
    )

    connections.commit()


def get_student_exam_status_all(class_, subject):
    if ' ' in subject:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    else:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f''' SELECT * FROM {table_name} '''
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d)

    return data

# print(get_student_exam_status_all('AdvancedLevel', 'Data Science'))

def get_student_exam_status_by(class_, reg_num, subject):
    if ' ' in subject:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    else:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    id_ = f'{reg_num[-3:]}_{subject}'
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f''' SELECT * FROM {table_name} WHERE reg_num = %s AND subject = %s''',
        (reg_num, subject)
    )

    connections.commit()

    res = connection.fetchall()
    data = []
    for d in res:
        data.append(d)

    return data

# print(get_student_exam_status_by('AdvancedLevel', '2020JKN', 'Data Science')[0][-1] == 'True')

def delete_student_exam_status(class_, reg_num, subject):
    if ' ' in subject:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    else:
        subject = subject.replace(' ', '_')
        table_name = f'{class_}_{subject}_Result'
    id_ = f'{reg_num[-3:]}_{subject}'
    connections = MySQLdb.connect(localhost, root, '', get_school())
    connection = connections.cursor()
    connection.execute(
        f''' DELETE FROM {table_name} WHERE id = %s''',
        (id_)
    )

    connections.commit()

# delete_student_exam_status('2020JKN', 'Data Science')
# connections = MySQLdb.connect(localhost, root, '', get_school())
# connection = connections.cursor()
# connection.execute(
#     ''' DROP TABLE StudentsExamStatus '''
# )

# connections.commit()
