# Exercício - Lista de tarefas com desfazer e refazer

# O exercio deve ler comandos de listar, refazer e desfazer. Se nenhum desses comandos for dado ele deve adicionar o que foi digitado a lista de tarefas.

import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('cls')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
      












#chat GPT

# class ListaDeTarefas:
#     def __init__(self):
#         self.todo = []
#         self.undo_stack = []
#         self.redo_stack = []

#     def adicionar_tarefa(self, tarefa):
#         self.todo.append(tarefa)
#         self.undo_stack.append(('adicionar', tarefa))
#         self.redo_stack.clear()

#     def desfazer(self):
#         if not self.undo_stack:
#             print('Nada a desfazer')
#             return
#         acao, tarefa = self.undo_stack.pop()
#         if acao == 'adicionar':
#             self.todo.remove(tarefa)
#             self.redo_stack.append(('adicionar', tarefa))
#         elif acao == 'remover':
#             self.todo.append(tarefa)
#             self.redo_stack.append(('remover', tarefa))

#     def refazer(self):
#         if not self.redo_stack:
#             print('Nada a refazer')
#             return
#         acao, tarefa = self.redo_stack.pop()
#         if acao == 'adicionar':
#             self.todo.append(tarefa)
#             self.undo_stack.append(('adicionar', tarefa))
#         elif acao == 'remover':
#             self.todo.remove(tarefa)
#             self.undo_stack.append(('remover', tarefa))

#     def listar_tarefas(self):
#         if not self.todo:
#             print('Lista de tarefas vazia')
#         else:
#             print('Tarefas:')
#             for tarefa in self.todo:
#                 print('-', tarefa)

#     def executar_comando(self, comando):
#         if comando == 'listar':
#             self.listar_tarefas()
#         elif comando == 'desfazer':
#             self.desfazer()
#         elif comando == 'refazer':
#             self.refazer()
#         elif comando == 'sair':
#             return False
#         else:
#             self.adicionar_tarefa(comando)
#         return True

#     def __str__(self):
#         return str(self.todo)

# lista = ListaDeTarefas()

# while True:
#     comando = input('Digite um comando (listar, desfazer, refazer, sair) ou uma tarefa: ')
#     sucesso = lista.executar_comando(comando)
#     if not sucesso:
#         break
