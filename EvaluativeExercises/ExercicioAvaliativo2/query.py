from database import Database

# Create an instance of the Database class, passing in the connection details for the Neo4j database
db = Database("bolt://44.203.212.164:7687", "neo4j", "sewers-vine-forms")

print("***************************************************************************")
print("Questão 1")

print("\nAno de nascimento e CPF do Renzo:")
result1 = db.execute_query("MATCH(t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf")
for record in result1:
    print(f"- Ano de Nascimento: {record['t.ano_nasc']}\n- CPF: {record['t.cpf']}")


print("\nNome e CPF dos professores que começam com a letra M:")
result2 = db.execute_query(
    "MATCH(t:Teacher) WHERE t.name STARTS WITH $letter RETURN t.name, t.cpf",
    parameters={"letter": "M"},
)
for record in result2:
    print(f"- {record['t.name']} : {record['t.cpf']}")


print("\nNomes das cidades:")
result3 = db.execute_query("MATCH(c:City) RETURN c.name")
for record in result3:
    print(f"- {record['c.name']}")


print("\nNome das escolas que tem o número maior que 150 e menor que 550:")
result4 = db.execute_query(
    "MATCH(s:School) WHERE s.number >= $min_number AND s.number <= $max_number RETURN s.name, s.address, s.number",
    parameters={"min_number": 150, "max_number": 550},
)
for record in result4:
    print(f"- Nome: {record['s.name']} - Endereço: {record['s.address']} - Número: {record['s.number']}")


print("\n***************************************************************************")
print("Questão 2")


print("\nAno de nascimento do professor mais velho e do mais jovem:")
result5 = db.execute_query(
    "MATCH(t:Teacher) RETURN min(t.ano_nasc) as min_year, max(t.ano_nasc) as max_year"
)
for record in result5:
    print(f"- Mais velho: {record['min_year']}\n- Mais jovem: {record['max_year']}")


print("\nMédia aritmética dos habitantes das cidades:")
result6 = db.execute_query("MATCH(c:City) RETURN avg(c.population)")
for record in result6:
    print(f"- Média: {record[0]}")


print("\nCidade com o CEP 37540-000 com as letras 'a' em caixa alta:")
result7 = db.execute_query(
    "MATCH(c:City{cep:'37540-000'}) RETURN replace(c.name, 'a', 'A')"
)
for record in result7:
    print(f"- {record[0]}")


print("\nNomes dos professores a partir do terceiro caractere:") 
result8 = db.execute_query("MATCH(t:Teacher) RETURN substring(t.name, 2)")
for record in result8:
    print(f"- {record[0]}")
