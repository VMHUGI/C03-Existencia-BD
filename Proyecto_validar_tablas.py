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
    con = cx_Oracle.connect("SCH_UNIVERSAL", "un1v4rs4l20", "10.5.112.35:1521/dgpp")
    consulta=  "SELECT DISTINCT TABLE_NAME FROM ALL_TABLES WHERE OWNER = 'SCH_UNIVERSAL' UNION ALL SELECT DISTINCT TABLE_NAME FROM ALL_TABLES WHERE OWNER = 'SCH_ANALYST' UNION ALL SELECT DISTINCT TABLE_NAME FROM ALL_TABLES WHERE OWNER = 'SCH_SCIENTIST'"
    bd = pd.read_sql_query(consulta, con) 
    if len(bd['TABLE_NAME'][bd['TABLE_NAME'].isin(nombre)])>0:
        print('tabla existe')
        con.close()
        return True
    else:
        print('tabla no existe')
        con.close()
        return False
    
validar_tabla(nombre=['SIAF_CERTIFICADO_2018'])
