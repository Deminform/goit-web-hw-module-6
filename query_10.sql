-- Teachers name: Jonathan Frank / Sara Ewing / Jason Herrera / Michelle Hale DDS / Crystal Peck
SELECT subjects.subject_name
FROM subjects
JOIN scores ON scores.subject_id = subjects.id
JOIN students ON scores.student_id = students.id
JOIN teachers ON teachers.id = subjects.teacher_id
WHERE students.student_name = 'Reginald Marshall' AND teachers.teacher_name = 'Jason Herrera'
GROUP BY subjects.subject_name