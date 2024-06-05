import os
import json


def show_list(tasks):
    print()
    if not tasks:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas: ')
    for task in tasks:
        print(f'{task}')
    print()

def task_undo(tasks, tasks_redo):
    print()
    if not tasks:
        print('Nenhuma tarefa para desfazer')
        return

    task = tasks.pop()
    print(f'{task=} removida')
    tasks_redo.append(task)
    print()

def task_redo(tasks, tasks_redo):
    print()
    if not tasks_redo:
        print('Nenhuma tarefa para refazer')
        return

    task = tasks_redo.pop()
    print(f'{task=} adicionada a lista')
    tasks.append(task)
    print()

def task_add(task, tasks):
    print()
    task = task.strip()
    if not task:
        print('Você não digitou nada')
        return
    print(f'{task=} adicionada a lista')
    tasks.append(task)
    print()

def read_task(file_path):
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Arquivo não existe')
        save([], file_path)
        return []
    except json.JSONDecodeError:
        print('Arquivo vazio ou corrompido')
        return []

def save(tasks, file_path):
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)
    


FILE_PATH = 'aula84.json'
tasks = read_task(FILE_PATH)
tasks_redo = []

while True:
    print('Comandos: listar, desfazer ou refazer')
    task = input('Digite uma tarefa ou comando: ')
    
    if task =='listar':
        show_list(tasks)
        continue
    elif task =='desfazer':
        task_undo(tasks, tasks_redo)
        show_list(tasks)
        continue
    elif task =='refazer':
        task_redo(tasks, tasks_redo)
        show_list(tasks)
        continue
    elif task == 'clear':
        os.system('cls')
        continue
    else:
        task_add(task, tasks)
        show_list(tasks)
           
    save(tasks, FILE_PATH)