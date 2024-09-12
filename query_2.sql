-- Subjects: Mathematics / Physics / History / Geography / Computer Science / Biology / Chemistry / Literature / Art
SELECT ROUND(AVG(scores.score), 2) AS avg_score, students.student_name
FROM scores
         JOIN students ON students.id = scores.student_id
         JOIN subjects ON subjects.id = scores.subject_id
WHERE subjects.subject_name = 'Physics'
GROUP BY student_id
ORDER BY avg_score DESC
LIMIT 1