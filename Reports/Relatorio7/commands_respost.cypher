// agregacoes
MATCH (a:Airport) RETURN COUNT(a) AS total_airports;

MATCH (a:Airport) RETURN SUM(a.altitude) AS total_altitude;

MATCH (a:Airport) RETURN AVG(a.longest) AS average_runway_length;

MATCH (a:Airport) RETURN MIN(a.altitude) AS min_altitude;

MATCH (a:Airport) RETURN MAX(a.longest) AS max_runway_length;

// funcoes matematicas
MATCH (a:Airport) RETURN a.iata, SQRT(a.altitude) AS sqrt_altitude;

MATCH (a:Airport) RETURN a.iata, EXP(a.altitude / 1000) AS exponential_altitude;

MATCH (a:Airport) RETURN a.iata, ABS(a.altitude - 1500) AS absolute_difference;

MATCH (a:Airport) RETURN a.iata, ROUND(a.altitude / 1000, 2) AS rounded_altitude;

MATCH (a:Airport) RETURN a.iata, CASE WHEN a.altitude < 1500 THEN a.altitude ELSE 1500 END AS min_altitude_threshold;


// funcoes de string
MATCH (a:Airport) RETURN a.iata, TOUPPER(a.city) AS city_uppercase;

MATCH (a:Airport) RETURN a.iata, TOLOWER(a.city) AS city_lowercase;

MATCH (a:Airport) WHERE a.iata STARTS WITH 'A' RETURN a.iata, a.city;

MATCH (a:Airport) WHERE a.city ENDS WITH 'ville' RETURN a.iata, a.city;

MATCH (a:Airport) RETURN a.iata, SUBSTRING(a.city, 0, 3) AS city_prefix;
