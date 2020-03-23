import psycopg2

conn = psycopg2.connect("dbname=netology_db user=netology_user host='192.168.66.73' password='dbpass'")


def create_db():
    """
    создает таблицы
    """
    pass


def get_students(course_id):
    """
    # возвращает студентов определенного курса
    :param course_id:
    :return:
    """
    pass


def add_students(course_id, students):
    """
    создает студентов и записывает их на курс
    :param course_id:
    :param students:
    :return:
    """
    pass


def add_student(student):
    """
    просто создает студента
    :param student:
    :return:
    """
    pass

def get_student(student_id):
    pass