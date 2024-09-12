-- Groups: G390 / G302 / G388
-- Subjects: Mathematics / Physics / History / Geography / Computer Science / Biology / Chemistry / Literature / Art
SELECT scores.score, students.student_name
FROM scores
         JOIN students ON scores.student_id = students.id
         JOIN groups ON students.group_id = groups.id
         JOIN subjects ON scores.subject_id = subjects.id
WHERE scores.date = (SELECT MAX(date)
                     FROM scores
                     WHERE scores.student_id = students.id
                       AND scores.subject_id = subjects.id)
  AND groups.group_name = 'G390'
  AND subjects.subject_name = 'Mathematics';
