-- A script that lists all records in the table second_table with scores >= 10
-- Records should be ordered by score (top first)
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER  BY `score` DESC;
