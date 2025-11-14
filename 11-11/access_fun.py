from users.jason import json as find_by_user
from datetime import  datetime as d

def login(user: str, password: str) -> bool:
   
    for k, v in db.items():
        if k == user and v == password:
            return True
    
    df = find_by_user(user)
    if df.loc[0,2] == password:

      return True
    
    return False


def resetPassword(user: str,password: str, new_password: str) -> str:
    
    if login(user, password):
        db[user] = new_password
        return 'Senha Alterada!'
    
    return 'Usuário Não Cadastrado!'

def update(user : str, password : str , new_user: str) -> str:

    try:
        if login(user,password):
            db[new_user] = db.pop(user)
            return 'Usuário Atualizado'
    except:
        print(f'log:[{dt.date}] - [{dt.time}]: Error no servidor')


