import os 
import time
import os
import shutil
import pandas 


data = pandas.read_json('C:\\Users\\enos.gabriel\\Documents\\copia\\config.json')
path = r""+data.origem[0]
dataUltimaAlteracao = ''

origin = data.origem[0]
destiny = data.destino[0]


def copiaAqruivos(origin, destiny):
    files = os.listdir(origin)
    for fname in files:
        shutil.copy2(os.path.join(origin,fname),destiny)

def indentificaModificao(path,dataUltimaAlteracao,origin,destiny):
    while True:
        ti_c = os.path.getctime(path) 
        ti_m = os.path.getmtime(path) 
        dataCriacao = time.ctime(ti_c) 
        
        if dataUltimaAlteracao != time.ctime(ti_m):
            dataUltimaAlteracao = time.ctime(ti_m)
            copiaAqruivos(origin,destiny)
            print('Arquivos copiados')



indentificaModificao(path, dataUltimaAlteracao,origin,destiny)
