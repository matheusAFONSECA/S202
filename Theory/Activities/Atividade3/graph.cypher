CREATE (matheus:Person {name: "Matheus Fonseca", gender: "Male", age: 21, profession: "Engineer"});
CREATE (julia:Person {name: "Julia Fonseca", gender: "Female", age: 17, profession: "Student"});
CREATE (charleny:Person {name: "Charleny Fonseca", gender: "Female", age: 40, profession: "Polvilheira"});
CREATE (ze_galinha:Person {name: "Zé Galinha", gender: "Male", age: 65, profession: "Polvilheiro"});
CREATE (cida:Person {name: "Cida", gender: "Female", age: 66, profession: "Teacher"});
CREATE (paulo:Person {name: "Paulo Fonseca", gender: "Male", age: 39, profession: "Truck Driver"});
CREATE (elismara:Person {name: "Elismara Fonseca", gender: "Female", age: 42, profession: "Seller"});
CREATE (zeus:Pet {name: "Zeus", breed: "Lhasa Apso", age: 6, type: "Dog"});
CREATE (lua:Pet {name: "Lua", breed: "Red Heeler", age: 14, type: "Dog"});
CREATE (estrela:Pet {name: "Estrela", breed: "Ragdoll", age: 3, type: "Cat"});

MATCH (ze_galinha:Person {name: "Zé Galinha"}), (matheus:Person {name: "Matheus Fonseca"}), (julia:Person {name: "Julia Fonseca"})
CREATE (ze_galinha)-[:GRANDFATHER_OF]->(matheus),
       (ze_galinha)-[:GRANDFATHER_OF]->(julia);

MATCH (cida:Person {name: "Cida"}), (matheus:Person {name: "Matheus Fonseca"}), (julia:Person {name: "Julia Fonseca"})
CREATE (cida)-[:GRANDMOTHER_OF]->(matheus),
       (cida)-[:GRANDMOTHER_OF]->(julia);

MATCH (ze_galinha:Person {name: "Zé Galinha"}), (charleny:Person {name: "Charleny Fonseca"}), (elismara:Person {name: "Elismara Fonseca"}), (paulo:Person {name: "Paulo Fonseca"})
CREATE (ze_galinha)-[:FATHER_OF]->(charleny),
       (ze_galinha)-[:FATHER_OF]->(elismara),
       (ze_galinha)-[:FATHER_OF]->(paulo);

MATCH (cida:Person {name: "Cida"}), (charleny:Person {name: "Charleny Fonseca"}), (elismara:Person {name: "Elismara Fonseca"}), (paulo:Person {name: "Paulo Fonseca"})
CREATE (cida)-[:MOTHER_OF]->(charleny),
       (cida)-[:MOTHER_OF]->(elismara),
       (cida)-[:MOTHER_OF]->(paulo);

MATCH (ze_galinha:Person {name: "Zé Galinha"}), (cida:Person {name: "Cida"})
CREATE (ze_galinha)-[:MARRIED_TO {since: 1980}]->(cida),
       (cida)-[:MARRIED_TO {since: 1980}]->(ze_galinha);

MATCH (charleny:Person {name: "Charleny Fonseca"}), (matheus:Person {name: "Matheus Fonseca"}), (julia:Person {name: "Julia Fonseca"})
CREATE (charleny)-[:MOTHER_OF]->(matheus),
       (charleny)-[:MOTHER_OF]->(julia);

MATCH (matheus:Person {name: "Matheus Fonseca"}), (julia:Person {name: "Julia Fonseca"})
CREATE (matheus)-[:SIBLING_OF {older: true}]->(julia),
       (julia)-[:SIBLING_OF {older: false}]->(matheus);

MATCH (charleny:Person {name: "Charleny Fonseca"}), (elismara:Person {name: "Elismara Fonseca"}), (paulo:Person {name: "Paulo Fonseca"})
CREATE (elismara)-[:SIBLING_OF {older: true}]->(charleny),
       (charleny)-[:SIBLING_OF {older: false}]->(elismara),
       (elismara)-[:SIBLING_OF {older: true}]->(paulo),
       (paulo)-[:SIBLING_OF {older: false}]->(elismara),
       (charleny)-[:SIBLING_OF {older: true}]->(paulo),
       (paulo)-[:SIBLING_OF {older: false}]->(charleny);

MATCH (julia:Person {name: "Julia Fonseca"}), (zeus:Pet {name: "Zeus"})
CREATE (julia)-[:OWNER_OF {since: 2018, nickname: "Gordinho"}]->(zeus);

MATCH (paulo:Person {name: "Paulo Fonseca"}), (lua:Pet {name: "Lua"})
CREATE (paulo)-[:OWNER_OF {since: 2010, nickname: "Sem Vergonha"}]->(lua);

MATCH (elismara:Person {name: "Elismara Fonseca"}), (estrela:Pet {name: "Estrela"})
CREATE (elismara)-[:OWNER_OF]->(estrela);
