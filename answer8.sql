-- ANSWER 8
SELECT author_id, yearmonth, hindex
FROM (SELECT author_id, strftime('%Y%m', published_at) AS yearmonth , (JUlianDay(published_at)-JulianDay('2010-01-01'))/365.25 AS h5index
      FROM paper_author)
WHERE hindex < 5
GROUP BY author_id, yearmonth