-- Task 16
-- Lists all recods of second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;