// CRIAÇÃO DE JURADOS, GAMES

CREATE(j:Jurado{nome:'Ewel'});
CREATE(j:Jurado{nome:'Gabriel'});
CREATE(j:Jurado{nome:'Davi'});


CREATE(g:Game{titulo:'League of Legends',genero:'MOBA',ano:2009});
CREATE(g:Game{titulo:'Minecraft',genero:'Sandbox',ano:2011});
CREATE(g:Game{titulo:'Phasmophobia',genero:'Terror',ano:2020});
CREATE(g:Game{titulo:'Warzone',genero:'Shooter',ano:2019});

CREATE(l:Loja{nome:'Steam'});
CREATE(l:Loja{nome:'Xbox'});
CREATE(l:Loja{nome:'Battlenet'});

// RELAÇÃO ENTRE JURADOS E GAMES

MATCH(j:Jurado{nome:'Ewel'}),(g:Game{titulo:'Warzone'})
CREATE(j)-[:JOGOU{nota:10, horas:500}]->(g);

MATCH(j:Jurado{nome:'Ewel'}),(g:Game{titulo:'League of Legends'})
CREATE(j)-[:JOGOU{nota:10, horas: 1000}]->(g);

MATCH(j:Jurado{nome:'Gabriel'}),(g:Game{titulo:'Warzone'})
CREATE(j)-[:JOGOU{nota:6, horas: 156}]->(g);

MATCH(j:Jurado{nome:'Gabriel'}),(g:Game{titulo:'Minecraft'})
CREATE(j)-[:JOGOU{nota:10, horas: 200}]->(g);

MATCH(j:Jurado{nome:'Gabriel'}),(g:Game{titulo:'League of Legends'})
CREATE(j)-[:JOGOU{nota:9, horas: 10000}]->(g);

MATCH(j:Jurado{nome:'Davi'}),(g:Game{titulo:'Minecraft'})
CREATE(j)-[:JOGOU{nota:10, horas: 12000}]->(g);

MATCH(j:Jurado{nome:'Davi'}),(g:Game{titulo:'Phasmophobia'})
CREATE(j)-[:JOGOU{nota:5, horas: 2}]->(g);