/*Ex 1*/
SELECT matchid,player
 FROM goal 
  WHERE teamid = 'GER';

/*Ex 2*/
SELECT id,stadium,team1,team2
  FROM game
 WHERE id = 1012;

/*Ex 3*/
SELECT player,teamid,stadium,mdate
  FROM game JOIN goal ON (id=matchid)
 WHERE teamid='GER';

/*Ex 4*/
SELECT team1,team2,player
  FROM game JOIN goal ON (id=matchid)
 WHERE player LIKE 'Mario%';

/*Ex 5*/
SELECT player, teamid, coach, gtime
  FROM goal JOIN eteam ON teamid=id
 WHERE gtime<=10;

/*Ex 6*/
SELECT mdate, teamname
  FROM game JOIN eteam ON (team1=eteam.id)
 WHERE coach = 'Fernando Santos';

/*Ex 7*/
SELECT player
  FROM game JOIN goal ON (id=matchid)
 WHERE stadium = 'National Stadium, Warsaw';

/*Ex 8*/
SELECT DISTINCT(player)
  FROM game JOIN goal ON matchid = id 
    WHERE (team1='GER'AND teamid!='GER') 
  OR (team2='GER' AND teamid!='GER');

/*Ex 9*/
SELECT teamname, COUNT(teamid)
  FROM eteam JOIN goal ON id=teamid
GROUP BY teamname;

/*Ex 10*/
SELECT stadium, COUNT(1)
  FROM game JOIN goal ON matchid=id
GROUP BY stadium;

/*Ex 11*/
SELECT matchid, mdate, COUNT(teamid)
  FROM game JOIN goal ON matchid = id 
 WHERE team1 = 'POL' 
OR team2 = 'POL'
GROUP BY matchid;

/*Ex 12*/
SELECT matchid, mdate, COUNT(teamid)
  FROM game JOIN goal ON matchid = id 
 WHERE teamid = 'GER'
GROUP BY matchid;

/*Ex 13*/
SELECT mdate,
  team1, 
  SUM(CASE WHEN goal.teamid = game.team1 THEN 1 ELSE 0 END) AS score1,
  team2,
  SUM(CASE WHEN goal.teamid = game.team2 THEN 1 ELSE 0 END) AS score2
  FROM game LEFT JOIN goal ON matchid = id
  GROUP BY id, matchid, team1, team2
  ORDER BY mdate, matchid, team1, team2;
