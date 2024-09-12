
-- Subjects: Mathematics / Physics / History / Geography / Computer Science / Biology / Chemistry / Literature / Art
SELECT round(avg(scores.score), 2) as avg_score, groups.group_name
FROM scores
JOIN students ON students.id = scores.student_id
JOIN subjects ON subjects.id = scores.subject_id
JOIN groups ON groups.id = students.group_id
WHERE subjects.subject_name = 'History'
GROUP BY groups.id