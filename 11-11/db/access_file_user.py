import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).parent.resolve() 
DIR_PATH = BASE_PATH / 'users.json'
df = pd.read_json(DIR_PATH, encoding = 'utf-8')

def insert_user(user,password):
     if find_by_user(user).empty:
         global df
         df['id'].max()
         df_new = pd.DataFrame({"id": df['id'].max + 1,"user":[user],
                           "password":[password]})
     df = pd.concat([df,df_new], ignore_index= True)
     df.to_json('./users.json', force_ascii=False,indent=4,orient='records')
     return 'Está Cadastrado'
def update_user(user, new):
    try:
        df.loc[df[df['user'] == user], 'password'] = new
        df.to_json(DIR_PATH, force_ascii=False,indent=4,orient='records')
    except:
     return 'Inválido'
def delete_user(user):
        try:
            df.loc[df['user'] == user, :] = None
            df.dropna(inplace= True)
            df['id']= df['id'].astype(int)
            df.to_json(DIR_PATH, force_ascii=False,indent=4,orient='records')
        except:
          return 'Inválido'

def find_by_user(user : str):
    return df[df['user'] == user]


print(df.loc[df['user'] == 'admin'])


print(delete_user('samuca', '123'))