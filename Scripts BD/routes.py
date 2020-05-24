#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:04:39 2020
"""

###############################################################################

import psycopg2
import sys
import csv

###############################################################################

try:
    conn = psycopg2.connect(host='localhost', database='airtrafficmanagement',
                            user="carlos", password='carlos')
    sys.stdout.write('Connexion établie...')
except psycopg2.Error:
    sys.stdout.write('connexion échouée...\n')
    sys.exit()

###############################################################################


def data_routes():
    tab = []
    with open("/home/carlos/Djangobdr/Data/Done/data_routes.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            tab.append((line[0].split(',')[0], line[1].split(',')[0], line[2].split(',')[0],
                        line[3].split(',')[0], line[4].split(',')[0], line[5].split(',')[0]))
    return tab

###############################################################################


data = data_routes()
cur = conn.cursor()
for i in range(1, len(data)):
    cur.execute("""
        INSERT INTO  airtrafficmanagement."carlosApp_routes"(routes_id,plane_id_id,airport_id_source_id,airport_id_dest_id,airline_id_id)
        VALUES (%s,%s,%s,%s,%s);
        """,
                (data[i][5], data[i][1], data[i][2], data[i][3], data[i][4]))
sys.stdout.write('Insertion réussie...')

###############################################################################

cur.close()
conn.commit()
conn.close()
sys.stdout.write('Opération terminée avec Succès...')

###############################################################################
