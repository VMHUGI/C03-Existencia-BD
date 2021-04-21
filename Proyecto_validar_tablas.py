# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:44:57 2021

@author: luiggi Silva
"""


def validar_tabla(nombre):
    import cx_Oracle
    import pandas as pd
    if isinstance(nombre, list):
        print('Nombre aceptado')
    else:
      raise Exception('El objeto ingresado no es una lista') 
    try:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\luigg\OneDrive\Documentos\instantclient_12_2")
    except:
        print('oracle iniciado')
    con = cx_Oracle.connect("USUARIO", "password", "IP:1521/dgpp")
    consulta=  "SELECT DISTINCT TABLE_NAME FROM ALL_TABLES WHERE OWNER = 'ESQUEMA01' UNION ALL SELECT DISTINCT TABLE_NAME FROM ALL_TABLES WHERE OWNER = 'ESQUEMA02' UNION ALL SELECT DISTINCT TABLE_NAME FROM ALL_TABLES WHERE OWNER = 'ESQUEMA03'"
    bd = pd.read_sql_query(consulta, con) 
    if len(bd['TABLE_NAME'][bd['TABLE_NAME'].isin(nombre)])>0:
        print('tabla existe')
        con.close()
        return True
    else:
        print('tabla no existe')
        con.close()
        return False
    
validar_tabla(nombre=['TABLE_TO_VALIDATE'])
