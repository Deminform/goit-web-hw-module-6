SELECT ROUND(AVG(scores.score), 2) AS avg_score, students.student_name
FROM scores
         JOIN students ON students.id = scores.student_id
GROUP BY student_id
ORDER BY avg_score DESC
LIMIT 5