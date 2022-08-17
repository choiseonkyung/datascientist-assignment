-- ANSWER 4
SELECT author_id, hindex
FROM (SELECT author_id , (JUlianDay(published_at)-JulianDay('2010-01-01'))/365.25 AS hindex
      FROM paper_author)
WHERE hindex < 1