
-- subjects - From 1 to 9 [ 'Mathematics', 'Physics', 'History', 'Geography', 'Computer Science', 'Biology', 'Chemistry', 'Literature', 'Art' ]
SELECT round(avg(scores.score), 2) as avg_score
FROM scores