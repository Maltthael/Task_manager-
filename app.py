import os

def title():
    print("""
███████████████████████████████████████████████████████████▀█████████████
█─▄─▄─██▀▄─██─▄▄▄▄█▄─█─▄███▄─▀█▀─▄██▀▄─██▄─▀█▄─▄██▀▄─██─▄▄▄▄█▄─▄▄─█▄─▄▄▀█
███─████─▀─██▄▄▄▄─██─▄▀█████─█▄█─███─▀─███─█▄▀─███─▀─██─██▄─██─▄█▀██─▄─▄█
▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
          """)

def invalid_option():
    
    print('Opção invalida\n')
    
    

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
    print('Adicionar tarefa')
    print('Visualizar tarefa')
    print('Remover tarefa')
    print('Sair')


def main():
      title()
      show_options()
      chose_option()
      
        
     
     
     

if __name__ == '__main__':
    main()