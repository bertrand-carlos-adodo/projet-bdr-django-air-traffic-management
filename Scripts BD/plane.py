#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:10:51 2020

@author: carlos
"""

###############################################################################

import  psycopg2
import sys
import  csv

###############################################################################

try :
    conn = psycopg2.connect(host = 'localhost', database = 'airtrafficmanagement',
                            user = "carlos", password = 'carlos')
    sys.stdout.write('Connexion établie...')
except psycopg2.Error:
        sys.stdout.write('connexion échouée...\n')
        sys.exit()

###############################################################################

def data_plane():
    tab=[]
    with open("/home/carlos/Djangobdr/Data/Done/data_plane.csv",'r',encoding='utf-8') as f:
        reader=csv.reader(f)
        for line in reader:
            tab.append((line[0].split(',')[0], line[1].split(',')[0], line[2].split(',')[0]))
    return tab

###############################################################################

data = data_plane()
cur = conn.cursor()
for i in range(1, len(data)):
    cur.execute("""
        INSERT INTO  airtrafficmanagement."carlosApp_plane"(plane_id,plane_name)
        VALUES (%s,%s);
        """,
        (data[i][2], data[i][1]))
sys.stdout.write('Insertion réussie...')

###############################################################################

cur.close()
conn.commit()
conn.close()
sys.stdout.write('Opération terminée avec Succès...')

###############################################################################