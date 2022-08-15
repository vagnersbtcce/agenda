'''
Rotina de teste de inclusão e listagem de tarefas via API
A entrada e saída das rotinas de inclusão e listagem estão via terminal, imprimindo
em formato JSON mesmo.
'''

import requests
import pprint

if __name__ == '__main__':

    url_root =  "http://127.0.0.1:8000/api/"
    url_api = url_root + "tarefas/"
    auth = ('************', '************')
    response = requests.get(url_api, auth=auth)

    resposta_usuario = '0'
    while resposta_usuario != '1' and resposta_usuario != '2':
        resposta_usuario = input("O que deseja fazer? (1 - listar / 2 - incluir)")
    if resposta_usuario == '1':
        resposta = response.json()
        pprint.pprint(resposta)
    else:
        descricao = input("Tarefa: ")
        categoria = input("Categoria (Rotina / Eventual / Importante): ")
        status = input("Status (Pendente / Urgente / Atrasado): ")

        tarefa = {'descricao': descricao,
                  'categoria': categoria,
                  'status': status,
                  }
        response = requests.post(url_api, auth=auth, data=tarefa)
        print("Tarefa incluída com sucesso!")

