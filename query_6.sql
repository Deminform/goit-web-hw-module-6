-- Available groups: G390 / G302 / G388
SELECT students.student_name
FROM students
JOIN groups on students.group_id = groups.id
WHERE groups.group_name = 'G390'