/*Ex 1*/
SELECT name FROM world
  WHERE name LIKE 'B%';

/*Ex 2*/
SELECT name FROM world
  WHERE name LIKE '%y';

/*Ex 3*/
SELECT name FROM world
  WHERE name LIKE '%x%';

/*Ex 4*/
SELECT name FROM world
  WHERE name LIKE '%land';

/*Ex 5*/
SELECT name FROM world
  WHERE name LIKE 'C%ia';

/*Ex 6*/
SELECT name FROM world
  WHERE name LIKE '%oo%';

/*Ex 7*/
SELECT name FROM world
  WHERE name LIKE '%a%a%a%';

/*Ex 8*/
SELECT name FROM world
 WHERE name LIKE '_t%'
ORDER BY name;

/*Ex 9*/
SELECT name FROM world
 WHERE name LIKE '%o__o%';

/*Ex 10*/
SELECT name FROM world
 WHERE name LIKE '____';

/*Ex 11*/
SELECT capital
  FROM world
 WHERE name LIKE capital;

/*Ex 12*/
SELECT name
  FROM world
 WHERE capital = concat(name, ' City');

/*Ex 13*/
SELECT capital, name
  FROM world
 WHERE capital LIKE concat(name, '%');

/*Ex 14*/
SELECT capital, name
  FROM world
 WHERE capital LIKE concat(name, '_','%');

/*Ex 15*/
SELECT name, REPLACE(capital, name,'')
  FROM world
 WHERE capital LIKE concat(name, '_','%');
