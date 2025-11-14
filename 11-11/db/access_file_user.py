import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).parent.resolve() 
DIR_PATH = BASE_PATH / 'users.json'
df = pd.read_json(DIR_PATH, encoding = 'utf-8')

def insert_user(user, password):
    """
    Insere um novo usuário no DataFrame global `df`.

    Parâmetros:
        user (str): Nome de usuário a ser inserido.
        password (str): Senha do usuário.

    Retorna:
        str: Mensagem informando que o usuário foi cadastrado.

    Comportamento:
        - Verifica se o usuário já existe usando `find_by_user`.
        - Caso não exista, cria uma nova linha com:
            id = (maior id atual + 1)
            user = nome do usuário
            password = senha
        - Concatena essa nova linha ao DataFrame global `df`.
        - Salva o DataFrame atualizado em `users.json`.
    """
    if find_by_user(user).empty:
        global df
        new_id = df['id'].max() + 1  
        df_new = pd.DataFrame({"id": [new_id], "user": [user], "password": [password]})
        df = pd.concat([df, df_new], ignore_index=True)
        df.to_json(DIR_PATH, force_ascii=False, indent=4, orient='records')
    return 'Está Cadastrado'


def update_user(user, new):
    """
    Atualiza a senha de um usuário existente.

    Parâmetros:
        user (str): Nome do usuário cuja senha será atualizada.
        new (str): Nova senha.

    Retorna:
        str: 'Inválido' caso ocorra um erro.

    Comportamento:
        - Localiza a linha onde `user` corresponde ao usuário informado.
        - Atualiza o campo 'password' para o novo valor.
        - Salva o DataFrame atualizado no arquivo JSON.
    """
    try:
        df.loc[df['user'] == user, 'password'] = new
        df.to_json(DIR_PATH, force_ascii=False, indent=4, orient='records')
    except:
        return 'Inválido'


def delete_user(user):
    """
    Exclui um usuário do DataFrame.

    Parâmetros:
        user (str): Nome do usuário a ser removido.

    Retorna:
        str: 'Inválido' caso ocorra algum erro.

    Comportamento:
        - Define como None a linha do usuário informado.
        - Remove linhas com valores nulos (dropna).
        - Converte a coluna 'id' de volta para inteiro.
        - Salva o DataFrame atualizado no arquivo JSON.
    """
    try:
        df.loc[df['user'] == user, :] = None
        df.dropna(inplace=True)
        df['id'] = df['id'].astype(int)
        df.to_json(DIR_PATH, force_ascii=False, indent=4, orient='records')
    except:
        return 'Inválido'


def find_by_user(user: str):
    """
    Busca um usuário no DataFrame global `df`.

    Parâmetros:
        user (str): Nome do usuário procurado.

    Retorna:
        DataFrame: Subconjunto contendo a linha do usuário encontrado.
                   Caso não exista, retorna um DataFrame vazio.
    """
    return df[df['user'] == user]

print(df.loc[df['user'] == 'admin'])

print(delete_user('samuca', '123'))