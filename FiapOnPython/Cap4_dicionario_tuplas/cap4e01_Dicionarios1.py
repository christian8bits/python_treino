usuarios={}
# FORMA DE ADICIONAR UM DICIONARIO 
usuarios={
    'Chaves':['Chaves Silva','17/06/1975','Recep_01'],
    'Quico':['Enrico Flores','03/06/1976','Raiox_02'],
    'Quico':['Enrico Flores','03/06/1976','Raiox_03']
    }
# OUTRA FORMA DE ADICIONAR DICIONARIO
usuarios['Florinda']=['Florinda Flores', '26/11/2017', 'Recep_01']
# SOBRESCREVER DICIONARIO
usuarios['Florinda']=['Florinda Flores', '26/11/2016', 'Recep_01']

# EXIBINDO OS DADOS
print(usuarios)
print('##############========#########')
print('Dados: ',usuarios.get('Chaves'))
# OBS: caso seja usado uma chave invalida o retorno do get será None   
