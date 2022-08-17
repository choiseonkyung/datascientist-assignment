-- ANSWER 6
SELECT author_id, year, hindex
FROM (SELECT author_id, strftime('%Y', published_at) AS year , (JUlianDay(published_at)-JulianDay('2010-01-01'))/365.25 AS hindex
      FROM paper_author)
WHERE hindex < 1
GROUP BY author_id, year