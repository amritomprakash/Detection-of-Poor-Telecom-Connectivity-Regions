# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:25:11 2020

@author: Amrit
"""

from flask import Flask, request, render_template, json, jsonify
import folium
import requests
import time
import pickle
from geopy.geocoders import Nominatim


urlget='http://customwebdb-216816.appspot.com/getvalue'
data={'tag':'tex_export'}

app = Flask(__name__,template_folder="C:\\Users\\Amrit\\Desktop\\SIH2020\\Signal_Issues") 

#/ggs
@app.route("/final",methods=["GET"])
def mains():
    r=requests.post(url=urlget,data=data)
    tt=r.text[26:-4].split("]")
    lat_arr=[]
    long_arr=[]
    sig_arr=[]
    for i in tt:
        j=i[1:]
        tmp_j=j.split(",")
        lat_arr.append(float(tmp_j[0].strip(",").strip("[")))
        long_arr.append(float(tmp_j[1]))
        sig_arr.append(int(tmp_j[2]))
    ind_map=folium.Map(zoom_start=8,location=[13.0827,80.2707])
    for lat,lon,sig in zip(lat_arr, long_arr,sig_arr):
        if(sig>-84):
            colo="green"
        elif(sig>=-102 and sig<=-85):
            colo="yellow"
        else:
            colo="red"
        folium.CircleMarker(
            [lat, lon],
            radius=5,
            #popup=label,
            color=colo,
            fill=True,
            #fill_color=rainbow[cluster],
            fill_opacity=0.8,).add_to(ind_map)
    ind_map.save("map.html")
    return render_template("map.html")
gg_cnt=0
@app.route("/enter",methods=["POST"])
def enter():
    global gg_cnt
    gg_cnt+=1
    fin_lat=[]
    fin_long=[]
    r=requests.post(url=urlget,data=data)
    tt=r.text[26:-4].split("]")
    lat_arr=[]
    long_arr=[]
    sig_arr=[]
    for i in tt:
        j=i[1:]
        tmp_j=j.split(",")
        lat_arr.append(float(tmp_j[0].strip(",").strip("[")))
        long_arr.append(float(tmp_j[1]))
        sig_arr.append(int(tmp_j[2]))
    ind_map=folium.Map(zoom_start=8,location=[13.0827,80.2707])
    for lat,lon,sig in zip(lat_arr, long_arr,sig_arr):
        if(sig>-84):
            colo="green"
        elif(sig>=-102 and sig<=-85):
            colo="yellow"
        else:
            colo="red"
        folium.CircleMarker(
            [lat, lon],
            radius=5,
            #popup=label,
            color=colo,
            fill=True,
            #fill_color=rainbow[cluster],
            fill_opacity=0.8,).add_to(ind_map)
    text=" "
    text = request.form['a']
    print(text)
    geolocator = Nominatim(user_agent="Signal_Issues")
    location = geolocator.geocode(text)
    knn_reg=pickle.load(open("model_signal.pkl", 'rb'))
    sc=pickle.load(open("model_signal_sc_X.pkl", 'rb'))
    sc1=pickle.load(open("model_signal_sc_y.pkl", 'rb'))
    print(location.latitude,location.longitude)
    fin_lat.append(location.latitude)
    fin_long.append(location.longitude)
    inp=[[location.latitude,location.longitude]]
    sc.transform(inp)
    val=knn_reg.predict(inp)
    add=sc1.inverse_transform(val)[0][0]
    print("val:"+str(add))
    if(add>-84):
        colo="Excellent"
    elif(add>=-102 and add<=-85):
        colo="Fair"
    else:
        colo="Poor"
    folium.CircleMarker(
            [fin_lat[-1],fin_long[-1]],
            radius=5,
            popup=colo,
            color="blue",
            fill=True,
            #fill_color=rainbow[cluster],
            fill_opacity=0.8,).add_to(ind_map)
    filename="map_req"+str(gg_cnt)+".html"
    ind_map.save(filename)
    ind_map
    return render_template(filename)
    




if __name__ == '__main__': 
   app.run() 