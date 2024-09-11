import sqlite3
from datetime import datetime, timedelta
from random import randint, random

import faker

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
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
        fake_students.append(fake_data.full_name())

    for _ in range(number_groups):
        fake_groups.append(fake_data.random_uppercase_letter() + str(fake_data.random_number(2, True)))

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.full_name())

    for subject in subjects:
        fake_subjects.append(subject)

    for _ in range(number_score):
        fake_scores.append(fake_data.random_number(2))

    return fake_students, fake_groups, fake_teachers, fake_subjects, fake_scores


def prepare_data(students, groups, teachers, subjects, scores):
    for_students = []
    for student in students:
        for_students.append((student,))

    for_groups = []
    index = 1
    students_per_group = NUMBER_STUDENTS / NUMBER_GROUPS
    for group in groups:
        for student_id in range(index, len(students) + 1):
            if len(for_groups) > students_per_group:
                index = student_id
                break
            for_groups.append((group, student_id,))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_subjects = []
    for subject in subjects:
        for teacher_id in range(1, NUMBER_TEACHERS + 1):
            for_subjects.append((subject, teacher_id,))

    for_score = []
    start_date = datetime(2023, 1, 1)
    for student_id in range(1, NUMBER_STUDENTS + 1):
        score_date = start_date + timedelta(days=randint(0, 364))
        for score in scores:
            for_score.append((score, score_date, student_id, randint(1, len(subjects)),))

    return for_students, for_groups, for_teachers, for_subjects, for_score


def insert_data_to_db(students, groups, teachers, subjects, scores):
    with sqlite3.connect('database/salary.db') as con:
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
