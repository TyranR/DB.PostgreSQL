import psycopg2 as pg

connection = pg.connect(database='netology_db', user='netology_user', host='192.168.66.73', password='dbpass', \
                        port='5432')
cur = connection.cursor()


def prepair():
    """
    Базовые таблицы
    :return:
    """
    cur.execute("CREATE TABLE student (id serial PRIMARY KEY, name varchar(100), gpa numeric(10,2), birth timestamptz)")
    cur.execute("CREATE TABLE course (id serial PRIMARY KEY, name varchar(100))")
    cur.execute("INSERT into course (name) values ('Обучение Python')")
    cur.execute("CREATE TABLE student_course (id SERIAL PRIMARY KEY, student_id INTEGER REFERENCES student(id), \
    course_id INTEGER REFERENCES course(id))")
    connection.commit()


def create_db(tables):
    """
    создает таблицы
    """
    cur.execute("CREATE TABLE %s (id serial PRIMARY KEY, name varchar(66))" % (tables))
    connection.commit()


def get_students(course_id):
    """
    # возвращает студентов определенного курса
    :param course_id:
    :return:
    """
    cur.execute("SELECT student.name, course.name FROM student_course join course on course.id = course_id join \
    student on student.id = student_id where course_id = %s" % (course_id))
    names = cur.fetchall()
    connection.commit()
    return names


def add_students(course_id, students):
    """
    создает студентов и записывает их на курс
    :param course_id:
    :param students:
    :return:
    """
    for student in students:
        print(student)
        cur.execute("INSERT into student (name, gpa, birth) values ('%s', '%s', '%s') RETURNING id" % \
                    (student['name'], student['gpa'], student['birth']))
        student_id = cur.fetchone()
        print(student_id[0])
        cur.execute("INSERT into student_course (student_id, course_id) values (%s, %s)" % (student_id[0], course_id))
    connection.commit()


def add_student(student):
    """
    просто создает студента
    :param student:
    :return:
    """
    cur.execute("INSERT into student (name, gpa, birth) values ('%s', '%s', '%s')" % (student['name'], student['gpa'], \
                                                                                      student['birth']))
    connection.commit()


def get_student(student_id):
    """
    ИЩем студента по его id
    :param student_id:
    :return:
    """
    cur.execute("SELECT name FROM student where id = %s" % student_id)
    name = cur.fetchone()
    connection.commit()
    return name[0]


def main():
    """
    Основная функция
    :return:
    """
    prepair()
    students = ({'name': 'Андрей2', 'gpa': 99.4, 'birth': '2001-10-05'}, {'name': 'Павел2', 'gpa': 99.4, \
                                                                          'birth': '2001-10-05'})
    add_students(1,students)
    get_students(1)
    get_student(1)


main()


