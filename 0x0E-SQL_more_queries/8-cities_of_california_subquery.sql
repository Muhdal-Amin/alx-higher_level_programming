-- A script that lists out all the cities of california in the database hbtn_0d_usa
-- Results are sorted in ascending order by cities.id
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
