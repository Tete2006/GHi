from db.access_file_user import *
from datetime import  datetime as dt

def login(user: str, password: str) -> bool:
   '''
    Função para verificar se um login é válido.

    Parâmetros: 
        - user (str): nome do usuário
        - password (str): senha do usuário
    
    Retorno: retornará um valor true ou false
    '''
   for k, v in df.items():
        if k == user and v == password:
            return True
        
        df = find_by_user(user)
   if df.iloc[0, 2] == password:
        return True
   
def resetPassword(user: str,password: str, new_password: str) -> str:
    '''
    Função para redefinir a senha do usuário.

    Parâmetros:
        - user (str): nome do usuário
        - password (str): senha do usuário
        - new_password (str): senha atualizada para registrar
    
    Retorno: Uma String confirmando ou recusando a modificação da senha
    '''
    if login(user, password):
        df[user] = new_password
        return 'Senha Alterada!'
    
    return 'Usuário Não Cadastrado!'

def update(user : str, password : str , new_user: str) -> str:
    '''
    Função para modificar o nome do usuário.

    Parâmetros:
        - user (str): nome do usuário
        - password (str): senha do usuário
        - new_user (str): novo nome do usuário
    
    Retorno: Confirmação da modificação do usuário. 
            Caso seja disparado algum erro será gerado um log.
    '''
    try:
        if login(user,password):
            df[new_user] = df.pop(user)
            return 'Usuário Atualizado'
    except:
        print(f'log:[{dt.date}] - [{dt.time}]: Error no servidor')


