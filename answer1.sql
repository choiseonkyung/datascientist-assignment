-- ANSWER 1

--각 저자별 publication_count 구하기
SELECT author_id, count(distinct a.paper_id) as publication_count
FROM paper_author as a
LEFT JOIN paper_reference as r
ON a.paper_id = r.paper_id
GROUP BY author_id

