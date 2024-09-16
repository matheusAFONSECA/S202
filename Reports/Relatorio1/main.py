# importação das bibliotecas
from aluno import Aluno
from aula import Aula
from professor import Professor

# código teste do relatório 1
professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())

# Presença(s) na aula sobre Programação Orientada a Objetos, ministrada pelo professor Lucas:
# O(a) aluno(a) Maria está presente.
# O(a) aluno(a) Pedro está presente
