import requests
import sys
try:
    cep = sys.argv[2]
    cep = cep.replace("-","").replace(".","")
except:
    print("====Valor Inválido====\nDIGITE NOVAMENTE SEU CEP:")

else:

    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        Logradouro = dic_requisicao['logradouro']
        Complemento = dic_requisicao['complemento']
        Bairro = dic_requisicao['bairro']
        Cidade = dic_requisicao['localidade']
        Estado = dic_requisicao['uf']
        print('='*50)
        print('Resultado da Busca: CEP :',cep)
        print('\nLogradouro:',Logradouro,
             '\nComplemento:',Complemento,
              '\nBairro:',Bairro,
              '\nCidade:',Cidade,
              '\nEstado":',Estado)
        print('='*50)
    else:
        print("CEP não encontrado")

