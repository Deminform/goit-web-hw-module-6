-- Teachers name: Jonathan Frank / Sara Ewing / Jason Herrera / Michelle Hale DDS / Crystal Peck
SELECT ROUND(AVG(scores.score), 2) AS avg_score
FROM scores
         JOIN subjects ON scores.subject_id = subjects.id
         JOIN teachers ON subjects.teacher_id = teachers.id
WHERE subjects.id IN (SELECT subjects.id
                      FROM subjects
                               JOIN teachers ON teachers.id = subjects.teacher_id
                      WHERE teachers.teacher_name = 'Crystal Peck')