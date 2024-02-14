/*
 * Task: Display the max temperature of each state ordered by state name.
 */

/* Query to find the maximum temperature for each state */
SELECT state, MAX(temperature) AS max_temp
FROM temperature_data
GROUP BY state
ORDER BY state;

