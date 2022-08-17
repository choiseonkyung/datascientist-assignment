-- ANSWER 2
SELECT author_id, year, COUNT(paper_id) AS publication_count, COUNT(reference_paper_id) AS citation_count
FROM (SELECT a.*, r.reference_paper_id, strftime('%Y', published_at) AS year
      FROM paper_author AS a
      LEFT JOIN paper_reference AS r
      ON a.paper_id = r.reference_paper_id)
GROUP BY author_id, year