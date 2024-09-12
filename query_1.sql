SELECT round(avg(scores.score), 2) as avg_score, students.id, students.student_name
FROM scores
JOIN students ON students.id = scores.student_id
GROUP BY student_id
ORDER BY avg_score DESC
LIMIT 5