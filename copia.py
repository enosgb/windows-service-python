
import os 
import time
import shutil
import pandas 
import glob


data = pandas.read_json('C:\\Users\\enos.gabriel\\Documents\\copia\\config.json')
path = r""+data.origem[0]
dataUltimaAlteracao = ''
latest_file = ''

origin = data.origem[0]
destiny = data.destino[0]



def copiaArquivos(origin, destiny):
    files = os.listdir(origin)
    for fname in files:
        shutil.copy2(os.path.join(origin,fname),destiny)

def indentificaModificao(path,origin,destiny,latest_file,dataUltimaAlteracao):
    while True:
        ti_c = os.path.getctime(path) 
        ti_m = os.path.getmtime(path) 
        dataCriacao = time.ctime(ti_c) 

        list_of_files = glob.glob(origin+'\*') # * means all if need specific format then *.csv
        if len(list_of_files) > 0:
            latest_file_update = max(list_of_files, key=os.path.getmtime)       
            latest_file_create = max(list_of_files, key=os.path.getctime)   
            print('create',latest_file_create)      
            print('update',latest_file_update)
            if latest_file != latest_file_update:
                latest_file = latest_file_update
                dataUltimaAlteracao = time.ctime(ti_m)
                copiaArquivos(origin,destiny)
                print('arquivos copiados')
            elif dataUltimaAlteracao != time.ctime(ti_m):
                dataUltimaAlteracao = time.ctime(ti_m)
                copiaArquivos(origin,destiny)
                print('Arquivos copiados')
            elif latest_file_create == latest_file:
                copiaArquivos(origin,destiny)
                print('Arquivos copiados')
        
        time.sleep(0.2) 


indentificaModificao(path,origin,destiny,latest_file,dataUltimaAlteracao)



