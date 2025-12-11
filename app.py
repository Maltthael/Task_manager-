import os

task_list = []



def title():
    print("""
███████████████████████████████████████████████████████████▀█████████████
█─▄─▄─██▀▄─██─▄▄▄▄█▄─█─▄███▄─▀█▀─▄██▀▄─██▄─▀█▄─▄██▀▄─██─▄▄▄▄█▄─▄▄─█▄─▄▄▀█
███─████─▀─██▄▄▄▄─██─▄▀█████─█▄█─███─▀─███─█▄▀─███─▀─██─██▄─██─▄█▀██─▄─▄█
▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
          """)


def add_task():
    print("""
█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▄░█ █▀█ █░█ ▄▀█   ▀█▀ ▄▀█ █▀█ █▀▀ █▀▀ ▄▀█
█▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █░▀█ █▄█ ▀▄▀ █▀█   ░█░ █▀█ █▀▄ ██▄ █▀░ █▀█

""")
    
    task_name = input('Digite a tarefa: ')
    description_task = input(f'Escreva brevemente sobre a tarefa {task_name}: ') 
    data_task = {'Nome':task_name, 'Descrição':description_task, 'Ativo':False}
    task_list.append(data_task)
    print(f'A tarefa {task_name} foi criada com sucesso!!!')
    back_menu()
    

def show_task_list():
    print(task_list)

def back_menu():

    print('\n Aperte qualquer tecla para voltar ao menu: ')
    main()

def invalid_option():
    
    print('Opção invalida\n')
    back_menu()
    

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
    except:
        invalid_option()
        
def show_options():
    print('1.Adicionar tarefa')
    print('2.Visualizar tarefa')
    print('3.Remover tarefa')
    print('4.Sair')


def main():
      title()
      show_options()
      chose_option()
         

if __name__ == '__main__':
    main()