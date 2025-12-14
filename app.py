import os

task_list = [
            {'Nome':'Aprender Java', 'Descrição': 'Estudar 2h por dia', 'Status':'Em progresso '},
             
             {'Nome':'Aprender a nadar', 'Descrição': 'Treinar 1h por dia', 'Status':'Concluido'},

]


def title():
    print("""
███████████████████████████████████████████████████████████▀█████████████
█─▄─▄─██▀▄─██─▄▄▄▄█▄─█─▄███▄─▀█▀─▄██▀▄─██▄─▀█▄─▄██▀▄─██─▄▄▄▄█▄─▄▄─█▄─▄▄▀█
███─████─▀─██▄▄▄▄─██─▄▀█████─█▄█─███─▀─███─█▄▀─███─▀─██─██▄─██─▄█▀██─▄─▄█
▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
          """)


def show_subtitle(texto):
    os.system('cls')
    
    line = '*' * (len(texto))
    print(line)
    print(texto)
    print(line)

def leave():
    print('Saindo...')
    exit

def add_task():
    
    show_subtitle(("""
█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▄░█ █▀█ █░█ ▄▀█   ▀█▀ ▄▀█ █▀█ █▀▀ █▀▀ ▄▀█
█▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █░▀█ █▄█ ▀▄▀ █▀█   ░█░ █▀█ █▀▄ ██▄ █▀░ █▀█

"""))
    
    task_name = input('Digite a tarefa: ')
    description_task = input(f'Escreva brevemente sobre a tarefa {task_name}: ') 
    status = input(f'Escreva o status da atividade {task_name} (Em progesso ou concluida): ')
    data_task = {'Nome':task_name, 'Descrição':description_task, 'Status':status}
    task_list.append(data_task)
    print(f'A tarefa {task_name} foi criada com sucesso!!!')
    back_menu()
    
def remove_task():
    print('')
    

def show_task_list():
    
    show_subtitle( """
█░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   ▀█▀ ▄▀█ █▀█ █▀▀ █▀▀ ▄▀█ █▀
█▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   ░█░ █▀█ █▀▄ ██▄ █▀░ █▀█ ▄█

                  """)
    print(f'{'Nome da tarefa'.ljust(22)} | {'Descrição'.ljust(20)} | {'Status'}')
    print('______________________|||____________________|||___________')
    for task in task_list:
        task_name = task['Nome']
        description_task = task['Descrição']
        status = task['Status']
        print(f'- {task_name.ljust(20)} | {description_task.ljust(20)} | {status}')
    back_menu()
    

def back_menu():

    input('\n Aperte qualquer tecla para voltar ao menu: ')
    main()

def invalid_option():
    
    print('Opção invalida\n')
    back_menu()
    

   
def show_options():
    print('1.Adicionar tarefa')
    print('2.Visualizar tarefa')
    print('3.Remover tarefa')
    print('4.Sair')


def chose_option():
    try:
        op_ch = int(input("Escolha uma opção: "))
        print(f'Você escolheu a opção {op_ch}')
        match op_ch:
            case 1:
                add_task()
            case 2:
                show_task_list()
            case 3:
                remove_task()
            case 4:
                leave()
            case _:
                invalid_option()
    except:
        invalid_option()

def main():
      os.system('cls')
      title()
      show_options()
      chose_option()
         

if __name__ == '__main__':
    main()