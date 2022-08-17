-- ANSWER 3
SELECT author_id, yearmonth, COUNT(paper_id) AS publication_count, COUNT(reference_paper_id) AS citation_count
FROM (SELECT a.*, r.reference_paper_id, strftime('%Y%m', published_at) AS yearmonth
      FROM paper_author AS a
      LEFT JOIN paper_reference AS r
      ON a.paper_id = r.reference_paper_id)
GROUP BY author_id, yearmonth