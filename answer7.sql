-- ANSWER 7
SELECT author_id, year, hindex
FROM (SELECT author_id, strftime('%Y', published_at) AS year , (JUlianDay(published_at)-JulianDay('2010-01-01'))/365.25 AS h5index
      FROM paper_author)
WHERE hindex < 5
GROUP BY author_id, year