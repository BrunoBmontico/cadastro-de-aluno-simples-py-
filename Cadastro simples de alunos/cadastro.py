alunos = ['Breno', 'joão']
idades = [10,14]
notas = [10, 7]
aluno = input('Nome do aluno. ')
idade = int(input('Idade do aluno. '))
nota = int(input('Nota do aluno. '))

#loop roda enquanto nenhum dos inputs estiver vazio.
while aluno or idade or nota != '':
    print('--ALUNO CADASTRADO--')
    alunos.append(aluno.capitalize())
    idades.append(idade)
    notas.append(nota)
#confirmção para acessar a nota de um aluno.
    todosAlunos = input('Digite o nome do aluno para ver sua nota, deixe em branco para ver a lista completa. ').capitalize()
#se deixar colocar qualquer coisa sem ser um nome de aluno irá mostrar a lista de alunos em dict.
    if todosAlunos in alunos:
        alunoPosi = alunos.index(todosAlunos)
        notaAluno = notas[alunoPosi]
        print('Aluno: {}. Nota: {}'.format(todosAlunos, notaAluno))
    else:
        print('-LISTA DE TODOS OS ALUNOS--')
        zipagem = zip(alunos, idades)
        dicio = dict(zipagem)
        print(dicio)
#confirmção se deseja continuar com mais um cadastro
    confirmacao = input('Deseja continuar com outro cadastro? S ou N ').capitalize()
    if 'N' in confirmacao:
        print('--CADASTRO FECHADO--')
        break
    elif 'S':
        pass
#caso diga que S continuar com o código normalmente
    aluno = input('Nome do aluno. ')
    idade = int(input('Idade do aluno. '))
    nota = int(input('Nota do aluno. '))