// Questao 1
// a
MATCH (n) 
RETURN n;

// b 
MATCH (g:Game) 
WHERE g.ano > 2012 
RETURN g;

// c 
MATCH (g:Game {genero: 'Terror'}) 
RETURN g;

// d 
MATCH (j:Jurado)-[r:JOGOU]->(g:Game) 
WHERE r.nota >= 7 
RETURN g, r.nota;


// Questao 2
// a 
CREATE (g:Game{titulo:'Valorant', genero:'Shooter', ano:2020});
CREATE (g:Game{titulo:'Elden Ring', genero:'RPG', ano:2022});
CREATE (g:Game{titulo:'Among Us', genero:'Party', ano:2018});
CREATE (g:Game{titulo:'FIFA 23', genero:'Sports', ano:2022});

// b 
CREATE (j:Jurado{nome:'Virginia'});
CREATE (j:Jurado{nome:'Julia'});
CREATE (j:Jurado{nome:'Charleny'});

// c 
MATCH (j:Jurado {nome: 'Virginia'}), (g:Game {titulo: 'Valorant'})
CREATE (j)-[:JOGOU {nota: 9, horas: 300}]->(g);

MATCH (j:Jurado {nome: 'Virginia'}), (g:Game {titulo: 'Among Us'})
CREATE (j)-[:JOGOU {nota: 8, horas: 50}]->(g);

MATCH (j:Jurado {nome: 'Julia'}), (g:Game {titulo: 'Elden Ring'})
CREATE (j)-[:JOGOU {nota: 10, horas: 500}]->(g);

MATCH (j:Jurado {nome: 'Julia'}), (g:Game {titulo: 'FIFA 23'})
CREATE (j)-[:JOGOU {nota: 7, horas: 120}]->(g);

MATCH (j:Jurado {nome: 'Charleny'}), (g:Game {titulo: 'FIFA 23'})
CREATE (j)-[:JOGOU {nota: 9, horas: 200}]->(g);

MATCH (j:Jurado {nome: 'Charleny'}), (g:Game {titulo: 'Phasmophobia'})
CREATE (j)-[:JOGOU {nota: 6, horas: 15}]->(g);
