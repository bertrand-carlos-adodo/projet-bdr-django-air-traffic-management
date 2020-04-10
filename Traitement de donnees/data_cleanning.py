#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 05:40:08 2020

@author: carlos
"""
###############################################################################

import pandas as pd
import numpy as np

###############################################################################

header_country = ['country_name', 'iso_code', 'dafif_code']
data_country = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/countries.dat',
                   sep = ',', names = header_country)

header_airport = ['airport_id', 'airport_name', 'city_name', 'country_name', 'iata', 'icao','latitude', 'longitude',
                  'altitude', 'timezone1', 'dst', 'timezone2', 'type', 'source']
data_airport = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat',
                   sep = ',', names = header_airport)

header_airline = ['airline_id', 'airline_name', 'alias', 'iata', 'icao', 'callsign', 'country_name', 'active']
data_airline = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat',
                   sep = ',', names = header_airline)

header_plane = ['plane_name', 'iata', 'icao']
data_plane = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/planes.dat',
                   sep = ',', names = header_plane)

header_routes = ['airline', 'airline_id', 'src_airport', 'src_airport_id', 'des_airport', 'des_airport_id',
                 'codeshare', 'stops', 'equipement']
data_routes = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat',
                   sep = ',', names = header_routes)

###############################################################################

country = data_country.iloc[:,0]
country = pd.DataFrame(country)
nv_country = pd.DataFrame([["Democratic People's Republic of Korea"]],columns = country.columns)
country = country.append(nv_country)
country['country_id'] = (np.arange(1, len(country)+1))
country.to_csv('data_country.csv', sep = ',', encoding = 'utf-8')

###############################################################################

city_and_country = data_airport.iloc[:,[2,3]]
city_and_country = pd.DataFrame(city_and_country)
city_and_country['city_name'].replace('', np.nan, inplace = True)
city_and_country.dropna(inplace = True)
city_and_country = pd.merge(city_and_country, country)
city_and_country.drop_duplicates(keep = 'last', inplace = True)
city_and_country['city_id'] = (np.arange(1, len(city_and_country)+1))
city = city_and_country.drop('country_name', axis = 1)
city.to_csv('data_city.csv', sep = ',', encoding = 'utf-8')

###############################################################################

airport = data_airport.iloc[:,[0,1,2,6,7,8,9,11]]
airport = pd.DataFrame(airport)
airport['city_name'].replace('', np.nan, inplace = True)
airport.dropna(inplace = True)
airport['timezone1'].replace('\\N', '0', inplace = True)
airport['timezone2'].replace('\\N', 'Inconnu', inplace = True)
airport = pd.merge(airport, city)
airport.drop_duplicates(keep = 'last', inplace = True)
airport = airport.drop('country_id', axis = 1)
airport = airport.drop('city_name', axis = 1)
airport['airport_id_new'] = (np.arange(1, len(airport)+1))
airport_last = airport.drop('airport_id', axis = 1)
airport_last.to_csv('data_airport.csv', sep = ',', encoding = 'utf-8')

###############################################################################

plane = data_plane.iloc[:,0]
plane = pd.DataFrame(plane)
plane['plane_id'] = (np.arange(1, len(plane)+1))
plane.to_csv('data_plane.csv', sep = ',', encoding = 'utf-8')

###############################################################################

airline = data_airline.iloc[:,[0,1,6,7]]
airline = pd.DataFrame(airline)
airline['active'].replace('Y', '1', inplace = True)
airline['active'].replace('N', '0', inplace = True)
airline = pd.merge(airline,country)
airline.drop_duplicates(keep = 'last', inplace = True)
airline = airline.drop('country_name', axis = 1)
airline['airline_id_new'] = (np.arange(1, len(airline)+1))
airline_last = airline.drop('airline_id', axis = 1)
airline_last.to_csv('data_airline.csv', sep = ',', encoding = 'utf-8')

###############################################################################

routes = data_routes.iloc[:,[1,3,5,8]]
routes = pd.DataFrame(routes)
equipement = routes['equipement'].str.split(expand = True)
routes = pd.concat([routes, equipement], axis = 1)
routes = routes.drop('equipement', axis = 1)
df0 = routes.iloc[:,[0,1,2,3]]
df0.columns = ['airline_id', 'src_airport_id', 'des_airport_id', 'iata']
df0.dropna(inplace = True)
df1 = routes.iloc[:,[0,1,2,4]]
df1.columns = ['airline_id', 'src_airport_id', 'des_airport_id', 'iata']
df1.dropna(inplace = True)
df2 = routes.iloc[:,[0,1,2,5]]
df2.columns = ['airline_id', 'src_airport_id', 'des_airport_id', 'iata']
df2.dropna(inplace = True)
df3 = routes.iloc[:,[0,1,2,6]]
df3.columns = ['airline_id', 'src_airport_id', 'des_airport_id', 'iata']
df3.dropna(inplace = True)
df4 = routes.iloc[:,[0,1,2,7]]
df4.columns = ['airline_id', 'src_airport_id', 'des_airport_id', 'iata']
df4.dropna(inplace = True)
df5 = routes.iloc[:,[0,1,2,8]]
df5.columns = ['airline_id', 'src_airport_id', 'des_airport_id', 'iata']
df5.dropna(inplace = True)
df6 = routes.iloc[:,[0,1,2,9]]
df6.columns = ['airline_id', 'src_airport_id', 'des_airport_id', 'iata']
df6.dropna(inplace = True)
df7 = routes.iloc[:,[0,1,2,10]]
df7.columns = ['airline_id', 'src_airport_id', 'des_airport_id', 'iata']
df7.dropna(inplace = True)
df8 = routes.iloc[:,[0,1,2,11]]
df8.columns = ['airline_id', 'src_airport_id', 'des_airport_id', 'iata']
df8.dropna(inplace = True)
routes = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7,df8], axis = 0)
routes['airline_id'].replace('\\N', np.nan, inplace = True)
routes['src_airport_id'].replace('\\N', np.nan, inplace = True)
routes['des_airport_id'].replace('\\N', np.nan, inplace = True)
routes.dropna(inplace = True)
plane_iata = data_plane.iloc[:,[0,1]]
plane_iata = pd.DataFrame(plane_iata)
plane_iata['iata'].replace('\\N', np.nan, inplace = True)
plane_iata.dropna(inplace = True)
plane_new = pd.merge(plane,plane_iata)
routes = pd.merge(routes, plane_new)
routes = routes.drop('iata', axis = 1)
routes = routes.drop('plane_name', axis = 1)
manip1 = airport.iloc[:,[0,8]]
manip1.columns = ['src_airport_id', 'airport_id_new_src']
manip2 = airport.iloc[:,[0,8]]
manip2.columns = ['des_airport_id', 'airport_id_new_des']
manip3 = airline.iloc[:,[0,4]]
routes = routes.astype({'src_airport_id':'int64'})
routes = routes.astype({'des_airport_id':'int64'})
routes = routes.astype({'airline_id':'int64'})
routes_new = pd.merge(routes,manip1)
routes_new = routes_new.drop('src_airport_id', axis = 1)
routes_new = pd.merge(routes_new,manip2)
routes_new = routes_new.drop('des_airport_id', axis = 1)
routes_new = pd.merge(routes_new,manip3)
routes_new = routes_new.drop('airline_id', axis = 1)
routes_new.drop_duplicates(keep = 'last', inplace = True)
routes_new['routes_id'] = (np.arange(1, len(routes_new)+1))
routes_new.to_csv('data_routes.csv', sep = ',', encoding = 'utf-8')

###############################################################################