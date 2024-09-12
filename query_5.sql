-- Teachers name: Jonathan Frank / Sara Ewing / Jason Herrera / Michelle Hale DDS / Crystal Peck
SELECT subject_name
FROM subjects
         JOIN teachers ON teachers.id = subjects.teacher_id
WHERE teachers.teacher_name = 'Jonathan Frank'