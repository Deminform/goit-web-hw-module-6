import sqlite3
from datetime import datetime, timedelta
from random import randint, random

import faker

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 8
SUBJECTS = ['Mathematics', 'Physics', 'History', 'Geography', 'Computer Science']
NUMBER_SCORES = 20 * NUMBER_STUDENTS


def generate_fake_data(number_students, number_groups, number_teachers, subjects, number_score):
    fake_students = []
    fake_groups = []
    fake_teachers = []
    fake_subjects = []
    fake_scores = []
    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_groups):
        fake_groups.append('G' + str(randint(300, 399)))

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for subject in subjects:
        fake_subjects.append(subject)

    for _ in range(number_score):
        fake_scores.append(fake_data.random_number(2))

    return fake_students, fake_groups, fake_teachers, fake_subjects, fake_scores


def prepare_data(students, groups, teachers, subjects, scores):
    for_students = []
    for i, student in enumerate(students):
        group = groups[i % len(groups) + 1]
        for_students.append((student, group,))

    for_groups = []
    for group in groups:
        for_groups.append((group,))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_subjects = []
    for i, subject in enumerate(subjects):
        teacher = teachers[i % len(teachers) + 1]
        for_subjects.append((subject, teacher,))

    for_score = []
    # start_date = datetime(2023, 1, 1)
    for i, score in enumerate(scores):
        student = students[i % len(students) + 1]
        subject = subjects[i % len(subjects) + 1]
        # for_score.append((score, student, subject, start_date + timedelta(days=randint(0, 364))))
        for_score.append((score, student, subject, faker.Faker().date_between('2023-01-01', '2023-12-31'),))

    return for_students, for_groups, for_teachers, for_subjects, for_score


def insert_data_to_db(students, groups, teachers, subjects, scores):
    with sqlite3.connect('database/school.db') as con:
        cur = con.cursor()

        sql_to_students = 'INSERT INTO students(student_name) VALUES (?)'
        cur.executemany(sql_to_students, students)

        sql_to_groups = 'INSERT INTO groups(group_name, student_id) VALUES (?, ?)'
        cur.executemany(sql_to_groups, groups)

        sql_to_teachers = 'INSERT INTO teachers(teacher_name, group_id) VALUES (?, ?)'
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = 'INSERT INTO subjects(teacher_id) VALUES (?)'
        cur.executemany(sql_to_subjects, subjects)

        sql_to_scores = 'INSERT INTO scores(score, date, student_id, subject_id) VALUES (?, ?, ?, ?)'
        cur.executemany(sql_to_scores, scores)


if __name__ == '__main__':
    students_data, groups_data, teachers_data, subjects_data, scores_data = prepare_data(*generate_fake_data(
        NUMBER_STUDENTS,
        NUMBER_GROUPS,
        NUMBER_TEACHERS,
        SUBJECTS,
        NUMBER_SCORES
    ))
    insert_data_to_db(students_data, groups_data, teachers_data, subjects_data, scores_data)
