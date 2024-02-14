/*
 * Task: Display the top 3 cities' temperatures during July and August ordered by temperature (descending).
 */

/* Query to calculate average temperature for July and August by city and select the top 3 */
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

