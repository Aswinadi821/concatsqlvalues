SELECT title, year,
CASE WHEN directors_Rating = '5' THEN "Alice Smith"
     WHEN directors_Rating = '3' THEN "Bob Jones" ELSE 'UNKNOWN' END Directors
FROM movie
JOIN movie_cast 
  ON movie_cast.mov_id=movie.mov_id 
JOIN actor 
  ON movie_cast.act_id=actor.act_id
WHERE actor.act_id IN (
SELECT act_id 
FROM movie_cast 
GROUP BY act_id HAVING COUNT(*)>=2);



