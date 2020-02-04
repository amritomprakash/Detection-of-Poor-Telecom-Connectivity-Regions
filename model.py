# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:40:18 2020

@author: Amrit
"""

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from geopy.geocoders import Nominatim
from random import randint
from pickle import dump

geolocator = Nominatim(user_agent="Signal_Issues")


#Web Scraping the dummy data
df_places=pd.read_csv("chennai_places_spread.csv",encoding="ISO-8859-1")

list_places=df_places['Manali new town']
lat=[]
long=[]
for i in list_places:
    if(str(i)=="Siruser"):
        i="Siruseri"
    location = geolocator.geocode(str(i))
    if(location==None):
        lat.append(0)
        long.append(0)
    else:
        lat.append(location.latitude)
        long.append(location.longitude)

sav_lat=lat
sav_long=long

fin_lat=[]
fin_long=[]
for k in range(0,len(lat)):
    if((int(lat[k]) in range(10,15)) and (int(long[k]) in range(77,82))):
        fin_lat.append(lat[k])
        fin_long.append(long[k])
    

dec_vals=[]
for f in range(0,154):
    dec_vals.append(randint(-112,-84))
dec_vals
fin_lat.append(12.8913)
fin_long.append((80.0810))
dec_vals.append(-104)

fin_lat.append(12.8439)
fin_long.append((80.0597))
dec_vals.append(-103)

fin_lat.append(12.8513)
fin_long.append((80.1470))
dec_vals.append(-108)
cars = {'Lat': fin_lat,
        'Long': fin_long,
        'Signal':dec_vals
        }

df = pd.DataFrame(cars, columns = ['Lat', 'Long','Signal'])
X=df[['Lat','Long']]
y=df[['Signal']]
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc1=StandardScaler()
X=sc.fit_transform(X)
y=sc1.fit_transform(y)



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=42)




from sklearn.neighbors import KNeighborsRegressor
knn_reg=KNeighborsRegressor(n_neighbors=10)
knn_reg.fit(X_train,y_train)

from sklearn.metrics import r2_score
r2_score(y_test,knn_reg.predict(X_test))



dump(knn_reg, open('model_signal.pkl', 'wb'))
dump(sc, open('model_signal_sc_X.pkl', 'wb'))
dump(sc1, open('model_signal_sc_y.pkl', 'wb'))





