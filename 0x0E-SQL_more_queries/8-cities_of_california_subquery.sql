-- 8. Cities of California
-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

SELECT DISTINCT `cities`.`id`, `cities`.`name`
FROM            `cities`, `states`
WHERE           `cities`.`state_id` =
(
    SELECT  `states`.`id`
    FROM    `states`
    WHERE   `states`.`name` = "California"
)
ORDER BY    `cities`.`id` ASC;
