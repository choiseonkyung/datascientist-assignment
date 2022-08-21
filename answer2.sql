-- ANSWER 2

--각 논문에 대한 citation_count 구하기
SELECT r.reference_paper_id, count(a.paper_id) as citation_count
FROM paper_author as a
LEFT JOIN paper_reference as r
ON a.paper_id = r.paper_id
GROUP BY r.reference_paper_id