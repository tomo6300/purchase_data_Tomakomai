from django.shortcuts import render, redirect
from django.utils import timezone
import pytz
import datetime
from .models import PurchaseData,Item
#from .forms import SpendingForm
import matplotlib.pyplot as plt
import calendar
#from .utils import index_utils
from django.views import View
import os
import folium
import pandas as pd
from pathlib import Path
import base64
from io import BytesIO
from folium import FeatureGroup,LayerControl
import matplotlib

BASE_DIR = Path(__file__).resolve().parent.parent
plt.rcParams['font.family'] = 'MS Gothic'    #日本語の文字化け防止
#plt.rcParams['font.family'] = 'IPAPGothic'    #日本語の文字化け防止

def Output_Graph():
	buffer = BytesIO()                   #バイナリI/O(画像や音声データを取り扱う際に利用)
	plt.savefig(buffer, format="png")    #png形式の画像データを取り扱う
	buffer.seek(0)                       #ストリーム先頭のoffset byteに変更
	img   = buffer.getvalue()            #バッファの全内容を含むbytes
	graph = base64.b64encode(img)        #画像ファイルをbase64でエンコード
	graph = graph.decode("utf-8")        #デコードして文字列から画像に変換
	buffer.close()
	return graph

def draw_graph():#year, month):    #追加
    #money = Money.objects.filter(use_date__year=year,use_date__month=month).order_by('use_date')
    purchase = PurchaseData.objects.all()

    last_day = calendar.monthrange(int(2022), int(12))[1] + 1
    #last_day = calendar.monthrange(int(year), int(month))[1] + 1
    day = [i for i in range(1, last_day)]
    cost = [0 for i in range(len(day))]
    for m in purchase:
        for j in m.item.all():    
            #item = Item.objects.filter(name=m.detail)
            cost[int(str(m.date).split('-')[2].split(' ')[0])-1] += int(j.price)
    plt.figure(figsize=(5,5),dpi=50)
    plt.bar(day, cost, color='#00bfff', edgecolor='#0000ff')
    plt.grid(True)
    plt.xlim([0, 31])
    plt.xlabel('日付', fontsize=16)
    plt.ylabel('支出額(円)', fontsize=16)
    plt.tight_layout()
    graph = Output_Graph()
    return graph

def draw_circle(): 
    #money = Money.objects.filter(use_date__year=year,use_date__month=month).order_by('use_date')
    purchase = PurchaseData.objects.all()
    dic_category={}
    for m in purchase:
        for j in m.item.all():
            #item = Item.objects.filter(name=m.detail)
            if j.category in dic_category:
                dic_category[j.category] += int(j.price)
            else:
                dic_category[j.category] = int(j.price)

    #plt.rcParams['font.family'] = 'MS Gothic'    
    plt.figure(figsize=(5,5),dpi=50)
    plt.pie(dic_category.values(), labels=dic_category.keys())
    plt.tight_layout()
    graph = Output_Graph()
    return graph

def draw_circle_tabe(): 
    #money = Money.objects.filter(use_date__year=year,use_date__month=month).order_by('use_date')
    purchase = PurchaseData.objects.all()
    dic_category={}
    for m in purchase:
        for j in m.item.filter(category="食品"):
            #item = Item.objects.filter(name=m.detail)
            if j.name in dic_category:
                dic_category[j.name] += int(j.price)
            else:
                dic_category[j.name] = int(j.price)    
    plt.figure(figsize=(5,5),dpi=50)
    plt.pie(dic_category.values(), labels=dic_category.keys())
    plt.tight_layout()
    graph = Output_Graph()
    return graph 

def draw_circle_age():    #追加
    purchase = PurchaseData.objects.all()
    dic_age={}
    for m in purchase:
        #for j in m.item.all():
        if m.age in dic_age:
            dic_age[m.age] += 1 #int(j.price)
        else:
            dic_age[m.age] = 1 #int(j.price)    
    plt.figure(figsize=(5,5),dpi=50)
    plt.pie(dic_age.values(), labels=dic_age.keys())
    plt.tight_layout()
    graph = Output_Graph()
    return graph 

def draw_circle_gender():    #追加
    purchase = PurchaseData.objects.all()
    dic_gender={}
    for m in purchase:
        #for j in m.item.all():
        if m.gender in dic_gender:
            dic_gender[m.gender] += 1 #int(j.price)
        else:
            dic_gender[m.gender] = 1 #int(j.price)    
    plt.figure(figsize=(5,5),dpi=50)
    plt.pie(dic_gender.values(), labels=dic_gender.keys())
    plt.tight_layout()
    graph = Output_Graph()
    return graph

def visualize_locations(zoom=11):
    """日本を拡大した地図に、pandasデータフレームのlatitudeおよびlongitudeカラムをプロットする。
    """
    filepath=os.path.join(BASE_DIR,'purchase_data/geoip/Tomakomaiv20401.csv')
    df=pd.read_csv(filepath)    	
    # 図の大きさを指定する。
    f = folium.Figure(width=1000, height=500)

    # 初期表示の中心の座標を指定して地図を作成する。
    center_lat=42.63408
    center_lon=141.606
    m = folium.Map([center_lat,center_lon], zoom_start=zoom).add_to(f)
        
    # データフレームの全ての行のマーカーを作成する。
    for i in range(0,len(df)):
        folium.Circle(location=[df["緯度"][i],df["経度"][i]],
                      #radius = 0,
                      radius = int(df["合計"][i].replace(',',''))*0.17,
                      #popup=df["町名"][i],
                      color  ="blue",
                      #opacity=0.2,
                      weight=0.3,
                      fill=True,
                      popup="""
                      <i>町名: </i><b>{}　　　　　　</b>
                      <i>人口: </i><b>{}　　　</b>
                      <i>男性: </i><b>{}　　　</b>
                      <i>女性: </i><b>{}　　　</b>
                      <i>世帯: </i><b>{}　　　</b>""".format(df["町名"][i],df["合計"][i],df["男"][i],df["女"][i],df["世帯"][i])
                      ).add_to(m)
    m = m._repr_html_()
    return m

def visualize_locations2():
    #money = Money.objects.filter(use_date__year=year,use_date__month=month).order_by('use_date')
    purchase = PurchaseData.objects.all()
    dic_location={}
    for m in purchase:
        for j in m.item.all():
            #item = Item.objects.filter(name=m.detail)
            if m.place in dic_location:
                dic_location[m.place] += int(j.price)
            else:
                dic_location[m.place] = int(j.price)        

    filepath=os.path.join(BASE_DIR,'purchase_data/geoip/Tomakomaiv20401.csv')
    df=pd.read_csv(filepath)  
    #df=pd.read_csv('money/geoip/Tomakomaiv20401.csv')    	
    
    f = folium.Figure(width=1000, height=500)

    # 初期表示の中心の座標を指定して地図を作成する。
    center_lat=42.63408
    center_lon=141.606
    m = folium.Map([center_lat,center_lon], zoom_start=11).add_to(f)

    for k,v in dic_location.items():
        try:
            folium.Circle(location=[float(df.loc[df['町名']==k,'緯度'].values),float(df.loc[df['町名']==k,'経度'].values)],
                      radius = v*0.2,
                      #radius = int(df.loc[df['町名']==k,'合計'].values.replace(',',''))/6,
                      #popup=df["町名"][i],
                      color  ="red",
                      #opacity=0.2,
                      weight=0.3,
                      fill=True,
                      popup="""
                      <i>町名: </i><b>{}　　　　　　　</b>
                      <i>人口: </i><b>{}　　　</b>
                      <i>取引金額: </i><b>{}　円</b>
                      """.format(k,int(df.loc[df['町名']==k,'合計'].values.tolist()[0].replace(',','')),v)
                      ).add_to(m)
        except TypeError as e:
            print(e)
    m = m._repr_html_()
    return m

def visualize_locations3():#カテゴリー別
    #money = Money.objects.filter(use_date__year=year,use_date__month=month).order_by('use_date')
    purchase = PurchaseData.objects.all()
    dic_location={}
    for m in purchase:
        for j in m.item.all():
            if j.category in dic_location:
            #item = Item.objects.filter(name=m.detail)
                if m.place in dic_location[j.category]:
                    dic_location[j.category][m.place] += int(j.price)
                else:
                    dic_location[j.category][m.place] = int(j.price)
            else:
                dic_location[j.category]={}
                dic_location[j.category][m.place] = int(j.price)


    filepath=os.path.join(BASE_DIR,'purchase_data/geoip/Tomakomaiv20401.csv')
    df=pd.read_csv(filepath)  
    #df=pd.read_csv('money/geoip/Tomakomaiv20401.csv')    	
    
    f = folium.Figure(width=1000, height=500)

    # 初期表示の中心の座標を指定して地図を作成する。
    center_lat=42.63408
    center_lon=141.606
    m = folium.Map([center_lat,center_lon], zoom_start=11).add_to(f)
    cm = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
        'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
         'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
          'gray', 'black', 'lightgray']#matplotlib.cm.tab20
    i=0
    for c,d in dic_location.items():
        group=FeatureGroup(name='{}'.format(c))
        colors=cm[i]
        i += 1 
        for k,v in d.items():
            folium.Circle(location=[float(df.loc[df['町名']==k,'緯度'].values),float(df.loc[df['町名']==k,'経度'].values)],
                        radius = v*0.2,
                        #radius = int(df.loc[df['町名']==k,'合計'].values.replace(',',''))/6,
                        #popup=df["町名"][i],
                        color  =colors,
                        #opacity=0.2,
                        weight=0.3,
                        fill=True,
                        popup="""
                        <i>町名: </i><b>{}　　　　　　　</b>
                        <i>人口: </i><b>{}　　　　</b>
                        <i>取引金額: </i><b>{}　円</b>
                        """.format(k,int(df.loc[df['町名']==k,'合計'].values.tolist()[0].replace(',','')),v),
                        #name='{}'.format(c)
                        ).add_to(group)
        group.add_to(m)
    LayerControl(collapsed=False).add_to(m)
    m = m._repr_html_()
    return m