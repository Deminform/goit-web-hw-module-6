SELECT subjects.subject_name
FROM scores
         JOIN students ON scores.student_id = students.id
         JOIN subjects ON subjects.id = scores.subject_id
WHERE student_name = 'Neil Drake'
GROUP BY subjects.subject_name