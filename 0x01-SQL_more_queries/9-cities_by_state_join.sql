-- Task 9: Lists all cities in teh database
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id ASC, cities.name, states.name;
