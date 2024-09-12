-- Groups: G390 / G302 / G388
-- Subjects: Mathematics / Physics / History / Geography / Computer Science / Biology / Chemistry / Literature / Art
SELECT scores.score
FROM scores
         JOIN students ON students.id = scores.student_id
         JOIN subjects ON subjects.id = scores.subject_id
         JOIN groups ON groups.id = students.group_id
WHERE groups.group_name = 'G302'
  AND subjects.subject_name = 'Physics'