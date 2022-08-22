import win32serviceutil
import win32service
import win32event
import servicemanager

import socket
import logging
import psutil
import sys

logging.basicConfig(filename="service.log", level=logging.DEBUG)



import os 
import time
import os
import shutil
import pandas 


data = pandas.read_json('C:\\Users\\enos.gabriel\\Documents\\copia\\config.json')
path = r""+data.origem[0]
dataUltimaAlteracao = ''

origin = data.origem[0]
#origin = 'C:\\Users\\enos.gabriel\\Documents\copia\\backup'
destiny = data.destino[0]
#destiny = 'C:\\Users\\enos.gabriel\\Documents\copia\\destiny'

# COPIA DE ARQUIVOS
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
        time.sleep(0.2)    


# SERVICO
class ExampleService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonCopy"
    _svc_display_name_ = "PythonCopyService"
    _svc_description_ = "Controplan dev"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def main(self):
        """DO THE RUN STUFF HERE"""
        logging.info("SERVICE MAIN ENTERED !!")
        indentificaModificao(path, dataUltimaAlteracao,origin,destiny)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(ExampleService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(ExampleService)