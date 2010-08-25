CREATE VIEW foos_wins (id, team_id, wins)
AS SELECT 1, s1.team_id, COUNT(s1.team_id)
FROM foos_score AS s1
JOIN foos_score AS s2
USING (game_id)
WHERE s1.team_id <> s2.team_id AND s1.score > s2.score
GROUP BY s1.team_id;
