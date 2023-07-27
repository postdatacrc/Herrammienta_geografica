import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from plotly.subplots import make_subplots
import glob
import math
import re
import os
from urllib.request import urlopen
import json
from streamlit_folium import folium_static
from st_aggrid import AgGrid
import geopandas as gpd
import folium
from folium.plugins import FloatImage
import urllib
from streamlit_folium import folium_static
from functools import partial, reduce


LogoComision="data:image/png;base64,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"
LogoComision2="https://postdata.gov.co/sites/all/themes/nuboot_radix/logo-crc-blanco.png"

st.set_page_config(
    page_title="Herramienta geográfica TIC", page_icon=LogoComision,layout="wide",initial_sidebar_state="expanded")  

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

Barra_superior="""
<div class="barra-superior">
    <div class="imagen-flotar" style="height: 70px; left: 10px; padding:15px">
        <a class="imagen-flotar" style="float:left;" href="https://www.crcom.gov.co" title="CRC">
            <img src="https://www.postdata.gov.co/sites/all/themes/nuboot_radix/logo-crc-blanco.png" alt="CRC" style="height:40px">
        </a>
        <a class="imagen-flotar" style="padding-left:10px;" href="https://www.postdata.gov.co" title="Postdata">
            <img src="https://www.postdata.gov.co/sites/default/files/postdata-logo.png" alt="Inicio" style="height:40px">
        </a>
    </div>
</div>"""
st.markdown(Barra_superior,unsafe_allow_html=True)

st.markdown("""<h1>Herramienta geográfica Telecomunicaciones</h1>""",unsafe_allow_html=True)
st.sidebar.markdown("""<b>Menú</b>""", unsafe_allow_html=True)

#Función para traer base
@st.cache()
def T13(allow_output_mutation=True):
    url_bases = 'https://raw.githubusercontent.com/postdatacrc/Herrammienta_geografica/main/Bases_T13/'
    dfT13 = []
    for i in range(9):
        file_name = f'T1_3-{i}.csv'
        file_url = os.path.join(url_bases, file_name)
        base = pd.read_csv(file_url, delimiter=';')
        dfT13.append(base)
    FT_13 = pd.concat(dfT13)
    FT_13['CODIGO_DEPARTAMENTO']=FT_13['DEPARTAMENTO']+'-'+FT_13['ID_DEPARTAMENTO'].astype('str')
    FT_13['CODIGO_MUNICIPIO']=FT_13['MUNICIPIO']+'-'+FT_13['ID_MUNICIPIO'].astype('str')
    FT_13['PERIODO']=FT_13['ANNO'].astype('str')+'-T'+FT_13['TRIMESTRE'].astype('str')
    FT_13['CODSEG']=np.where(FT_13['ID_SEGMENTO'].isin([101,102,103,104,105,106]),'Residencial','Corporativo')

    dict_regiones = {
        'REGIÓN ANDINA': [5, 11, 15, 17, 25, 41, 54, 63, 66, 68, 73],
        'REGIÓN AMAZÓNICA': [91, 18, 94, 95, 86, 97],
        'REGIÓN PACÍFICA': [76, 27, 19, 52],
        'REGIÓN CARIBE': [8, 13, 20, 23, 44, 47, 70, 88],
        'REGIÓN ORINOQUÍA': [81, 85, 50, 99]
    }

    def clas_region(value):
        for region, numbers in dict_regiones.items():
            if value in numbers:
                return region
        return 'Error'
    FT_13['REGIÓN'] = FT_13['ID_DEPARTAMENTO'].map(clas_region) 
    FT_13=FT_13[FT_13['ANNO']==2022]   
    
    return FT_13
FT1_3=T13()

MUNICIPIOS=sorted(FT1_3['CODIGO_MUNICIPIO'].unique().tolist())
DEPARTAMENTOS=sorted(FT1_3['CODIGO_DEPARTAMENTO'].unique().tolist())
REGIONES=sorted(FT1_3['REGIÓN'].unique().tolist())

#Hogares para cálculo de la penetración
Hogares=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Herrammienta_geografica/main/HOGARES.csv',delimiter=';')
Hogares=Hogares[Hogares['ANNO']==2022]
Hogares['ID_DEPARTAMENTO']=Hogares['ID_DEPARTAMENTO'].astype('str')
Hogares['ID_MUNICIPIO']=Hogares['ID_MUNICIPIO'].astype('str').str.zfill(5)
HogaresDep=Hogares.groupby(['ID_DEPARTAMENTO'])['HOGARES'].sum().reset_index()

#Centroides departamentos y regiones
def centroid_dep(cod_dep):
    coord_dep=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Herrammienta_geografica/main/centroides_dep.csv',delimiter=';',decimal='.')
    coord_dep=coord_dep.rename(columns={'Código':'ID_DEPARTAMENTO'})
    coord_dep['ID_DEPARTAMENTO']=coord_dep['ID_DEPARTAMENTO'].astype('str').str.zfill(2)
    coord_dep[['LATITUD','LONGITUD']]=coord_dep[['LATITUD','LONGITUD']].replace(',','.',regex=True).astype('float')
    centroid=coord_dep[coord_dep['ID_DEPARTAMENTO']==cod_dep].iloc[0][['LATITUD','LONGITUD']].values.tolist()
    return centroid
def centroid_reg(region):
    coord_dep=pd.read_csv('https://raw.githubusercontent.com/postdatacrc/Herrammienta_geografica/main/centroides_dep.csv',delimiter=';',decimal='.')
    coord_dep=coord_dep.rename(columns={'Código':'ID_DEPARTAMENTO'})
    coord_dep[['LATITUD','LONGITUD']]=coord_dep[['LATITUD','LONGITUD']].replace(',','.',regex=True).astype('float')
    dict_regiones = {
        'REGIÓN ANDINA': [5, 11, 15, 17, 25, 41, 54, 63, 66, 68, 73],
        'REGIÓN AMAZÓNICA': [91, 18, 94, 95, 86, 97],
        'REGIÓN PACÍFICA': [76, 27, 19, 52],
        'REGIÓN CARIBE': [8, 13, 20, 23, 44, 47, 70, 88],
        'REGIÓN ORINOQUÍA': [81, 85, 50, 99]
    }
    def clas_region(value):
        for region, numbers in dict_regiones.items():
            if value in numbers:
                return region
        return 'Error'  
    coord_dep['REGIÓN'] = coord_dep['ID_DEPARTAMENTO'].map(clas_region) 
    coord_dep['ID_DEPARTAMENTO']=coord_dep['ID_DEPARTAMENTO'].astype('str').str.zfill(2)
    coord_depAgg=coord_dep.groupby(['REGIÓN']).agg({'LATITUD':'mean','LONGITUD':'mean'}).reset_index()
    centroid=coord_depAgg[coord_depAgg['REGIÓN']==region].iloc[0][['LATITUD','LONGITUD']].values.tolist()
    return centroid


#Información geográfica 
##Datos departamentales
gdf = gpd.read_file("colombia2.geo.json")
geoJSON_states = list(gdf.NOMBRE_DPT.values)
denominations_json = []
Id_json = []
Colombian_DPTO=json.load(open("colombia2.geo.json", 'r'))
for index in range(len(Colombian_DPTO['features'])):
    denominations_json.append(Colombian_DPTO['features'][index]['properties']['NOMBRE_DPT'])
    Id_json.append(Colombian_DPTO['features'][index]['properties']['DPTO'])
denominations_json=sorted(denominations_json)
gdf=gdf.rename(columns={"NOMBRE_DPT":'DESC_DEPARTAMENTO','DPTO':'ID_DEPARTAMENTO'})
gdf['ID_DEPARTAMENTO']=gdf['ID_DEPARTAMENTO'].astype('int64')
gdf['DESC_DEPARTAMENTO']=gdf['DESC_DEPARTAMENTO'].replace({'ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA':'SAN ANDRES Y PROVIDENCIA'})
##Datos municipales
Colombian_MUNI=json.load(open("co_2018_MGN_MPIO_POLITICO.geojson", 'r'))
gdf2 = gpd.read_file("co_2018_MGN_MPIO_POLITICO.geojson")
gdf2=gdf2.rename(columns={'MPIO_CNMBR':'DESC_MUNICIPIO','MPIO_CCNCT':'ID_MUNICIPIO'})
gdf2['ID_MUNICIPIO']=gdf2['ID_MUNICIPIO'].astype('int64')

fact_escala={'ACCESOS':1e6,'VALOR FACTURADO':1e9,'NÚMERO EMPRESAS':1}

#Definición Servicios individuales
InternetFijo=FT1_3[FT1_3['SERVICIO_PAQUETE'].isin(['Triple Play (Telefonía fija + Internet fijo + TV por suscripción)',
    'Duo Play 1 (Telefonía fija + Internet fijo)',
    'Duo Play 2 (Internet fijo y TV por suscripción)', 'Internet fijo'])]
TVporSus=FT1_3[FT1_3['SERVICIO_PAQUETE'].isin(['Triple Play (Telefonía fija + Internet fijo + TV por suscripción)',
'Duo Play 2 (Internet fijo y TV por suscripción)','Televisión por suscripción',
    'Duo Play 3 (Telefonía fija y TV por suscripción)'])] 
Telfija=FT1_3[FT1_3['SERVICIO_PAQUETE'].isin(['Triple Play (Telefonía fija + Internet fijo + TV por suscripción)',
    'Duo Play 1 (Telefonía fija + Internet fijo)','Duo Play 3 (Telefonía fija y TV por suscripción)',
    'Telefonía fija'])]   

#Funciones para graficar
def PlotlyBarrasSegmento(df,column):
    fig=make_subplots(rows=1,cols=1)
    mean_val = df[column].mean()
    if mean_val >= 1e9:
        y_title = f"{column} (Miles de Millones)"
        df[column] = round(df[column] / 1e9,2)
    elif mean_val >= 1e6:
        y_title = f"{column} (Millones)"
        df[column] = round(df[column] / 1e6,2)
    else:
        y_title = f"{column}"

    paleta_colores={'Residencial':"#FF7A48","Corporativo":"#0593A2","Total":"#E3371E"}
    if column=='NÚMERO EMPRESAS':
        SEG=["Residencial","Corporativo","Total"]
    else:    
        SEG=["Residencial","Corporativo"]
    for segmento in SEG:
        fig.add_trace(go.Bar(x=df[df['SEGMENTO']==segmento]['PERIODO'],
                            y=df[df['SEGMENTO']==segmento][column],name=segmento,marker_color=paleta_colores[segmento],
                            hovertemplate='%{y:.2f}'))
    fig.update_yaxes(tickfont=dict(family='Tahoma', color='black', size=16),title_font=dict(family="Tahoma"),titlefont_size=16, title_text=y_title, row=1, col=1)                        
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Tahoma', color='black', size=14),title_font=dict(family="Tahoma"),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Tahoma",title_font_color="Black",titlefont_size=20,
    title={
    'text':"<b>"+select_variable.capitalize()+" ("+select_servicio+")</b>",
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)',tickformat=',d')
    fig.update_layout(yaxis_tickformat = '0,.0f')
    if column!='NÚMERO EMPRESAS':       
        fig.update_layout(barmode='stack')   
        fig.add_trace(go.Scatter(x=df[df['SEGMENTO']==segmento]['PERIODO'],y=df[df['SEGMENTO']=='Total'][column].map('{:,.0f}'.format),
                                 mode='text',text=df[df['SEGMENTO']=='Total'][column].map('{:,.2f}'.format),textposition='top center',
                    textfont=dict(color='black', size=14),name=None,showlegend=False))        
    return fig

def PlotlyBarrasEmpaquetados(df,column):
    df2=df.groupby(['PERIODO'])[column].sum().reset_index()
    fig=make_subplots(rows=1,cols=1)
    mean_val = df[column].mean()
    if mean_val >= 1e9:
        y_title = f"{column} (Miles de Millones)"
        df[column] = round(df[column] / 1e9,2)
        df2[column] = round(df2[column] / 1e9,2)
    elif mean_val >= 1e6:
        y_title = f"{column} (Millones)"
        df[column] = round(df[column] / 1e6,2)
        df2[column] = round(df2[column] / 1e6,2)
    else:
        y_title = f"{column}"
    paleta_colores=["#F5D05C", "#230C33","#BF1363","#CAA8F5", "#F39273", "#5FBFAB", "#0E79B2"]
    Servicios=df['SERVICIO_PAQUETE'].unique().tolist()
    colores_empaquetados={'Duo Play 1': '#F5D05C', 'Duo Play 3': '#230C33', 'Internet fijo': '#BF1363', 'Telefonía fija': '#CAA8F5', 'Televisión por suscripción': '#F39273', 'Triple play': '#5FBFAB', 'Duo Play 2': '#0E79B2'}
    
    for servicio in Servicios:
        fig.add_trace(go.Bar(x=df[df['SERVICIO_PAQUETE']==servicio]['PERIODO'],
                            y=df[df['SERVICIO_PAQUETE']==servicio][column],name=servicio,marker_color=colores_empaquetados[servicio],
                            hovertemplate='%{y:.2f}'))
    fig.update_yaxes(tickfont=dict(family='Tahoma', color='black', size=16),title_font=dict(family="Tahoma"),titlefont_size=16, title_text=y_title, row=1, col=1)                        
    fig.update_xaxes(tickangle=0, tickfont=dict(family='Tahoma', color='black', size=14),title_font=dict(family="Tahoma"),title_text=None,row=1, col=1
    ,zeroline=True,linecolor = 'rgba(192, 192, 192, 0.8)',zerolinewidth=2)
    fig.update_layout(height=550,legend_title=None)
    fig.update_layout(font_color="Black",font_family="Tahoma",title_font_color="Black",titlefont_size=20,
    title={
    'text':"<b>"+select_variable.capitalize()+" ("+select_servicio+")</b>",
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})        
    fig.update_layout(legend=dict(orientation="h",xanchor='center',y=1.1,x=0.5,font_size=11),showlegend=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(192, 192, 192, 0.8)')
    fig.update_layout(yaxis_tickformat = '0,.0f')      
    fig.update_layout(barmode='stack')     
    fig.add_trace(go.Scatter(x=df2['PERIODO'],y=df2[column],
                                mode='text',text=df2[column].map('{:,.2f}'.format),textposition='top center',
                textfont=dict(color='black', size=14),name=None,showlegend=False))           
    return fig

def PlotlyTable(df,title):
    for cols in [x for x in df.columns if x!='PERIODO']:
        df[cols]=df[cols].astype(float).map('{:,.0f}'.format)
    table = go.Table(columnwidth=[300,500,500,500],header=dict(values="<b>"+df.columns+"</b>",
                                 fill_color='#2e297b',
                align='center',font=dict(color='white', size=15, family='Tahoma'),height=50),
                 cells=dict(values=[df[col] for col in df.columns],
                            fill_color=[["#fffdf7","Silver"]*4],
               align='center',font=dict(color='black', size=15, family='Tahoma'),height=30))
    fig=go.Figure(data=[table])
    fig.update_layout(height=500)
    fig.update_layout(title =  "<b>"+title+"</b> ", 
                   font_color = 'black', font_family='Tahoma', 
                   title_font_size = 20, title_x = 0.5) 
    return fig

#Funciones para hacer los mapas
def MapaNacional(df,periodo):
    mapaNacional=gdf.merge(df, on=['ID_DEPARTAMENTO'])
    mapaNacional=mapaNacional[mapaNacional['PERIODO']==periodo]
    mapaNacional['ID_DEPARTAMENTO']=mapaNacional['ID_DEPARTAMENTO'].astype('str')
    mapaNacional=mapaNacional.merge(HogaresDep,on=['ID_DEPARTAMENTO'])
    mapaNacional['PENETRACION']=round(100*mapaNacional['CANTIDAD_LINEAS_ACCESOS']/mapaNacional['HOGARES'],2)
    # create a plain world map
    Nac_map = folium.Map(location=[4.570868, -74.297333], zoom_start=5,tiles='cartodbpositron')
    tiles = ['stamenwatercolor', 'cartodbpositron', 'openstreetmap', 'stamenterrain']
    for tile in tiles:
        folium.TileLayer(tile).add_to(Nac_map)
    choropleth=folium.Choropleth(
        geo_data=Colombian_DPTO,
        data=mapaNacional,
        columns=['ID_DEPARTAMENTO', 'PENETRACION'],
        key_on='feature.properties.DPTO',
        fill_color='Reds', 
        fill_opacity=0.9, 
        line_opacity=0.9,
        legend_name='Penetración',
        nan_fill_color = "gray",
        smooth_factor=0).add_to(Nac_map)
    # Adicionar nombres del departamento
    style_function = "font-size: 15px; font-weight: bold"
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['DPTO'], style=style_function, labels=False))
    folium.LayerControl().add_to(Nac_map)

    #Adicionar valores porcentaje
    style_function = lambda x: {'fillColor': '#ffffff', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}
    NIL = folium.features.GeoJson(
        data = mapaNacional,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['DEPARTAMENTO','ID_DEPARTAMENTO','PENETRACION'],
            aliases=['Departamento','ID','Penetración'],
            style=("background-color: white; color: #333333; font-family: helvetica; font-size: 12px; padding: 10px;") 
        )
    )
    Nac_map.add_child(NIL)
    Nac_map.keep_in_front(NIL)
    return Nac_map    

def MapaMunicipal(df,periodo,codigo_dep):
    mapaporDep=gdf2.merge(df, on=['ID_MUNICIPIO'])
    mapaporDep=mapaporDep[mapaporDep['PERIODO']==periodo]
    mapaporDep['ID_MUNICIPIO']=mapaporDep['ID_MUNICIPIO'].astype('str').str.zfill(5)
    mapaporDep=mapaporDep.merge(Hogares,on=['ID_MUNICIPIO'])
    mapaporDep['PENETRACION']=round(100*mapaporDep['CANTIDAD_LINEAS_ACCESOS']/mapaporDep['HOGARES'],2)
    mapaporDep=mapaporDep[mapaporDep['DPTO_CCDGO']==codigo_dep]
    
    # create a plain world map
    Dep_map = folium.Map(location=centroid_dep(codigo_dep), zoom_start=7,tiles='cartodbpositron')
    tiles = ['stamenwatercolor', 'cartodbpositron', 'openstreetmap', 'stamenterrain']
    for tile in tiles:
        folium.TileLayer(tile).add_to(Dep_map)
    choropleth=folium.Choropleth(
        geo_data=Colombian_MUNI,
        data=mapaporDep,
        columns=['ID_MUNICIPIO', 'PENETRACION'],
        key_on='feature.properties.MPIO_CCNCT',
        fill_color='Reds', 
        fill_opacity=0.9, 
        line_opacity=0.9,
        legend_name='Penetración',
        nan_fill_color = "grey",
        smooth_factor=0).add_to(Dep_map)
    # Adicionar nombres del departamento
    style_function = "font-size: 15px; font-weight: bold"
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['MPIO_CCNCT'], style=style_function, labels=False))
    folium.LayerControl().add_to(Dep_map)

    #Adicionar valores porcentaje
    style_function = lambda x: {'fillColor': '#ffffff', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}
    NIL = folium.features.GeoJson(
        data = mapaporDep,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['MUNICIPIO','ID_MUNICIPIO','PENETRACION'],
            aliases=['Municipio','ID','Penetración'],
            style=("background-color: white; color: #333333; font-family: helvetica; font-size: 12px; padding: 10px;") 
        )
    )
    Dep_map.add_child(NIL)
    Dep_map.keep_in_front(NIL)
    return Dep_map    

def MapaRegional(df,periodo,region):
    mapaporReg=gdf2.merge(df, on=['ID_MUNICIPIO'])
    mapaporReg=mapaporReg[mapaporReg['PERIODO']==periodo]
    mapaporReg['ID_MUNICIPIO']=mapaporReg['ID_MUNICIPIO'].astype('str').str.zfill(5)
    mapaporReg=mapaporReg.merge(Hogares,on=['ID_MUNICIPIO'])
    mapaporReg['PENETRACION']=round(100*mapaporReg['CANTIDAD_LINEAS_ACCESOS']/mapaporReg['HOGARES'],2)
    mapaporReg=mapaporReg[mapaporReg['REGIÓN']==region]
    
    # create a plain world map
    Reg_map = folium.Map(location=centroid_reg(region), zoom_start=6,tiles='cartodbpositron')
    tiles = ['stamenwatercolor', 'cartodbpositron', 'openstreetmap', 'stamenterrain']
    for tile in tiles:
        folium.TileLayer(tile).add_to(Reg_map)
    choropleth=folium.Choropleth(
        geo_data=Colombian_MUNI,
        data=mapaporReg,
        columns=['ID_MUNICIPIO', 'PENETRACION'],
        key_on='feature.properties.MPIO_CCNCT',
        fill_color='Reds', 
        fill_opacity=0.9, 
        line_opacity=0.9,
        legend_name='Penetración',
        nan_fill_color = "grey",
        smooth_factor=0).add_to(Reg_map)
    # Adicionar nombres del departamento
    style_function = "font-size: 15px; font-weight: bold"
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['MPIO_CCNCT'], style=style_function, labels=False))
    folium.LayerControl().add_to(Reg_map)

    #Adicionar valores porcentaje
    style_function = lambda x: {'fillColor': '#ffffff', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}
    NIL = folium.features.GeoJson(
        data = mapaporReg,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=folium.features.GeoJsonTooltip(
            fields=['MUNICIPIO','ID_MUNICIPIO','PENETRACION'],
            aliases=['Municipio','ID','Penetración'],
            style=("background-color: white; color: #333333; font-family: helvetica; font-size: 12px; padding: 10px;") 
        )
    )
    Reg_map.add_child(NIL)
    Reg_map.keep_in_front(NIL)
    return Reg_map

#Extracción de información por ámbito
def Nac_info(df):
    dfNac=pd.concat([df.groupby(['PERIODO', 'CODSEG']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
    df.groupby(['PERIODO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
    dfNac=dfNac.rename(columns=dict_variables)
    dfNac2=pd.pivot(dfNac[['PERIODO','SEGMENTO',select_variable]], index=['PERIODO'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)
    dfNac2_html = f'<div class="styled-table">{dfNac2.to_html(index=False)}</div>'
    return dfNac, dfNac2

def Reg_info(df):
    dfReg=pd.concat([df.groupby(['PERIODO', 'CODSEG','REGIÓN']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
    df.groupby(['PERIODO','REGIÓN']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
    dfReg=dfReg.rename(columns=dict_variables)
    dfReg=dfReg[dfReg['REGIÓN']==select_reg]
    dfReg2=pd.pivot(dfReg[['PERIODO','SEGMENTO',select_variable]], index=['PERIODO'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)
    dfDep2_html = f'<div class="styled-table">{dfReg2.to_html(index=False)}</div>'
    return dfReg,dfReg2

def Dep_info(df):
    dfDep=pd.concat([df.groupby(['PERIODO', 'CODSEG','CODIGO_DEPARTAMENTO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
    df.groupby(['PERIODO','CODIGO_DEPARTAMENTO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
    dfDep=dfDep.rename(columns=dict_variables)
    dfDep=dfDep[dfDep['CODIGO_DEPARTAMENTO']==select_dpto]
    dfDep2=pd.pivot(dfDep[['PERIODO','SEGMENTO',select_variable]], index=['PERIODO'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)
    dfDep2_html = f'<div class="styled-table">{dfDep2.to_html(index=False)}</div>'
    return dfDep,dfDep2

def Muni_info(df):
    dfMUNI=pd.concat([df.groupby(['PERIODO', 'CODSEG','CODIGO_MUNICIPIO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
    df.groupby(['PERIODO','CODIGO_MUNICIPIO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
    dfMUNI=dfMUNI.rename(columns=dict_variables)
    dfMUNI=dfMUNI[dfMUNI['CODIGO_MUNICIPIO']==select_muni]
    dfMUNI2=pd.pivot(dfMUNI[['PERIODO','SEGMENTO',select_variable]], index=['PERIODO'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)
    dfMUNI2_html = f'<div class="styled-table">{dfMUNI2.to_html(index=False)}</div>' 
    return dfMUNI, dfMUNI2

#Botón ámbito
select_ambito=st.sidebar.selectbox('Ámbito',['Nacional','Regional','Departamental','Municipal'])
if select_ambito=='Regional':
    select_reg=st.sidebar.selectbox('Región',REGIONES)
if select_ambito=='Departamental':
    select_dpto=st.sidebar.selectbox('Departamento',DEPARTAMENTOS)
if select_ambito=='Municipal':
    select_muni=st.sidebar.selectbox('Municipio',MUNICIPIOS) 
#Botón variables    
dict_variables={'CANTIDAD_LINEAS_ACCESOS': 'ACCESOS', 'VALOR_FACTURADO_O_COBRADO': 'VALOR FACTURADO', 'ID_EMPRESA': 'NÚMERO EMPRESAS','CODSEG': 'SEGMENTO'}
dict_variables_inverse={v: k for k, v in dict_variables.items()}
select_variable=st.sidebar.selectbox('Variable',['ACCESOS','VALOR FACTURADO', 'NÚMERO EMPRESAS']) 

#Función para calcular métricas del último periodo
def metricServ(df, amb, var):
    if var == 'NÚMERO EMPRESAS':
        agg_func = 'nunique'
    else:
        agg_func = 'sum'
        
    if amb == 'Nacional':
        filter_condition = (df['PERIODO']=='2022-T4')
    elif amb == 'Departamental':
        filter_condition = (df['PERIODO']=='2022-T4')&(df['CODIGO_DEPARTAMENTO'] == select_dpto)
    elif amb == 'Municipal':
        filter_condition = (df['PERIODO']=='2022-T4')&(df['CODIGO_MUNICIPIO'] == select_muni)
    elif amb == 'Regional':
        filter_condition = (df['PERIODO']=='2022-T4')&(df['REGIÓN'] == select_reg)
    else:
        return "Invalido"
    Data = df[filter_condition].groupby(['PERIODO']).agg({dict_variables_inverse[var]: agg_func}).reset_index()
    x = Data[dict_variables_inverse[var]].values[0]   
    if x >= 1e9:
        y_title = f"{round(x/1e9, 2)} (MM)"
    elif x >= 1e6:
        y_title = f"{round(x/1e6, 2)} (M)"
    else:
        y_title = f"{x}" 
    return y_title
    
#Estructura con métricas del último periodo
with st.container():
    col1,col2,col3,col4,col5,col6=st.columns([0.5,1]*3)
    with col2:
        st.markdown(r"""<div><img height="130px" src='https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Iconos/internet-fijo.png'/></div>""",unsafe_allow_html=True) 
    with col4:
        st.markdown(r"""<div><img height="130px" src='https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Iconos/telefonia-fija.png'/></div>""",unsafe_allow_html=True) 
    with col6:
        st.markdown(r"""<div><img height="130px" src='https://raw.githubusercontent.com/postdatacrc/Reporte-de-industria/main/Iconos/tv-por-suscripcion.png'/></div>""",unsafe_allow_html=True) 
        
    col2.metric("Internet fijo", metricServ(InternetFijo,select_ambito,select_variable))
    col4.metric("Telefonía fija", metricServ(Telfija,select_ambito,select_variable))
    col6.metric("TV por suscripción", metricServ(TVporSus,select_ambito,select_variable))
    
    st.markdown("<b>Nota</b>: Información para el periodo 2022-T4. Tomada del formato T.1.3 de la resolución CRC 5050 de 2016",unsafe_allow_html=True)
st.markdown('<hr>',unsafe_allow_html=True)

#Botón servicio
select_servicio=st.radio('Servicio',['Internet Fijo','TV por suscripción','Telefonía fija', 'Empaquetados'],horizontal=True)

#Internet Fijo
if select_servicio=='Internet Fijo':
    st.markdown(r"""<div class="titulo"><h2>Internet fijo</h2></div>""",unsafe_allow_html=True)
    if select_ambito=='Nacional':
        tab1,tab2,tab3 = st.tabs(['Gráfica','Tabla con datos','Mapa'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Nac_info(InternetFijo)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Nac_info(InternetFijo)[1],select_variable.capitalize()),use_container_width=True)
        with tab3:
            if select_variable!='ACCESOS':
                st.warning(f'El mapa representa la penetración (Accesos por 100 hogares), no la variable {select_variable}')  
            else:
                pass
            InternetFijoDep=InternetFijo.groupby(['PERIODO','ID_DEPARTAMENTO','DEPARTAMENTO'])['CANTIDAD_LINEAS_ACCESOS'].sum().reset_index()
            col1,col2,col3=st.columns([1,1.5,1])
            with col2:
                periodo=st.selectbox('Escoja el periodo',['2022-T1','2022-T2','2022-T3','2022-T4'],index=3)
                folium_static(MapaNacional(InternetFijoDep,periodo),width=450)        
                
    if select_ambito=='Regional':
        st.markdown(r"""<div><center><h3>"""+select_reg+"""</h3></center></div>""",unsafe_allow_html=True)        
        tab1,tab2,tab3 = st.tabs(['Gráfica','Tabla con datos','Mapa'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Reg_info(InternetFijo)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Reg_info(InternetFijo)[1],select_variable.capitalize()),use_container_width=True)
        with tab3:
            if select_variable!='ACCESOS':
                st.warning(f'El mapa representa la penetración (Accesos por 100 hogares), no la variable {select_variable}')  
            else:
                pass
            InternetFijoReg=InternetFijo.groupby(['PERIODO','REGIÓN','ID_MUNICIPIO','MUNICIPIO'])['CANTIDAD_LINEAS_ACCESOS'].sum().reset_index()            
            col1,col2,col3=st.columns([1,1.5,1])
            with col2:
                periodo=st.selectbox('Escoja el periodo',['2022-T1','2022-T2','2022-T3','2022-T4'],index=3)
                folium_static(MapaRegional(InternetFijoReg,periodo,select_reg),width=450) 
                     
    if select_ambito=='Departamental':
        st.markdown(r"""<div><center><h3>"""+select_dpto.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        tab1,tab2,tab3 = st.tabs(['Gráfica','Tabla con datos','Mapa'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Dep_info(InternetFijo)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Dep_info(InternetFijo)[1],select_variable.capitalize()),use_container_width=True)
        with tab3:
            if select_variable!='ACCESOS':
                st.warning(f'El mapa representa la penetración (Accesos por 100 hogares), no la variable {select_variable}')  
            else:
                pass
            InternetFijoMuni=InternetFijo.groupby(['PERIODO','ID_MUNICIPIO','MUNICIPIO'])['CANTIDAD_LINEAS_ACCESOS'].sum().reset_index()
            col1,col2,col3=st.columns([1,1.5,1])
            with col2:
                periodo=st.selectbox('Escoja el periodo',['2022-T1','2022-T2','2022-T3','2022-T4'],index=3)
                folium_static(MapaMunicipal(InternetFijoMuni,periodo,select_dpto.split('-')[1].zfill(2)),width=450) 
        
    if select_ambito=='Municipal':
        st.markdown(r"""<div><center><h3>"""+select_muni.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        tab1,tab2 = st.tabs(['Gráfica','Tabla con datos'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Muni_info(InternetFijo)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:            
                st.plotly_chart(PlotlyTable(Muni_info(InternetFijo)[1],select_variable.capitalize()),use_container_width=True)

#Televisión por suscripción        
if select_servicio=='TV por suscripción':
    st.markdown(r"""<div class="titulo"><h2>Televisión por suscripción</h2></div>""",unsafe_allow_html=True)
    if select_ambito=='Nacional':
        tab1,tab2,tab3 = st.tabs(['Gráfica','Tabla con datos','Mapa'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Nac_info(TVporSus)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Nac_info(TVporSus)[1],select_variable.capitalize()),use_container_width=True)
        with tab3:
            if select_variable!='ACCESOS':
                st.warning(f'El mapa representa la penetración (Accesos por 100 hogares), no la variable {select_variable}')  
            else:
                pass
            TVporSusDep=TVporSus.groupby(['PERIODO','ID_DEPARTAMENTO','DEPARTAMENTO'])['CANTIDAD_LINEAS_ACCESOS'].sum().reset_index()
            col1,col2,col3=st.columns([1,1.5,1])
            with col2:
                periodo=st.selectbox('Escoja el periodo',['2022-T1','2022-T2','2022-T3','2022-T4'],index=3)
                folium_static(MapaNacional(TVporSusDep,periodo),width=450)   

    if select_ambito=='Regional':
        st.markdown(r"""<div><center><h3>"""+select_reg+"""</h3></center></div>""",unsafe_allow_html=True)        
        tab1,tab2,tab3 = st.tabs(['Gráfica','Tabla con datos','Mapa'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Reg_info(TVporSus)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Reg_info(TVporSus)[1],select_variable.capitalize()),use_container_width=True)
        with tab3:
            if select_variable!='ACCESOS':
                st.warning(f'El mapa representa la penetración (Accesos por 100 hogares), no la variable {select_variable}')  
            else:
                pass
            TVporSusReg=TVporSus.groupby(['PERIODO','REGIÓN','ID_MUNICIPIO','MUNICIPIO'])['CANTIDAD_LINEAS_ACCESOS'].sum().reset_index()            
            col1,col2,col3=st.columns([1,1.5,1])
            with col2:
                periodo=st.selectbox('Escoja el periodo',['2022-T1','2022-T2','2022-T3','2022-T4'],index=3)
                folium_static(MapaRegional(TVporSusReg,periodo,select_reg),width=450) 

    if select_ambito=='Departamental':
        
        st.markdown(r"""<div><center><h3>"""+select_dpto.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        tab1,tab2,tab3 = st.tabs(['Gráfica','Tabla con datos','Mapa'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Dep_info(TVporSus)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Dep_info(TVporSus)[1],select_variable.capitalize()),use_container_width=True)
        with tab3:
            if select_variable!='ACCESOS':
                st.warning(f'El mapa representa la penetración (Accesos por 100 hogares), no la variable {select_variable}')  
            else:
                pass 
            TVporSusMuni=TVporSus.groupby(['PERIODO','ID_MUNICIPIO','MUNICIPIO'])['CANTIDAD_LINEAS_ACCESOS'].sum().reset_index()
            col1,col2,col3=st.columns([1,1.5,1])
            with col2:
                periodo=st.selectbox('Escoja el periodo',['2022-T1','2022-T2','2022-T3','2022-T4'],index=3)
                folium_static(MapaMunicipal(TVporSusMuni,periodo,select_dpto.split('-')[1].zfill(2)),width=450) 

    if select_ambito=='Municipal':
        st.markdown(r"""<div><center><h3>"""+select_muni.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        tab1,tab2 = st.tabs(['Gráfica','Tabla con datos'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Muni_info(TVporSus)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Muni_info(TVporSus)[1],select_variable.capitalize()),use_container_width=True)

#Telefonía fija       
if select_servicio=='Telefonía fija':
    st.markdown(r"""<div class="titulo"><h2>Telefonía fija</h2></div>""",unsafe_allow_html=True)    
   
    if select_ambito=='Nacional':
        tab1,tab2,tab3 = st.tabs(['Gráfica','Tabla con datos','Mapa'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Nac_info(Telfija)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Nac_info(Telfija)[1],select_variable.capitalize()),use_container_width=True)
        with tab3:
            if select_variable!='ACCESOS':
                st.warning(f'El mapa representa la penetración (Accesos por 100 hogares), no la variable {select_variable}')  
            else:
                pass
            TelfijaDep=Telfija.groupby(['PERIODO','ID_DEPARTAMENTO','DEPARTAMENTO'])['CANTIDAD_LINEAS_ACCESOS'].sum().reset_index()
            col1,col2,col3=st.columns([1,1.5,1])
            with col2:
                periodo=st.selectbox('Escoja el periodo',['2022-T1','2022-T2','2022-T3','2022-T4'],index=3)
                folium_static(MapaNacional(TelfijaDep,periodo),width=450) 
                    
    if select_ambito=='Regional':
        st.markdown(r"""<div><center><h3>"""+select_reg+"""</h3></center></div>""",unsafe_allow_html=True)        
        tab1,tab2,tab3 = st.tabs(['Gráfica','Tabla con datos','Mapa'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Reg_info(Telfija)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Reg_info(Telfija)[1],select_variable.capitalize()),use_container_width=True)
        with tab3:
            if select_variable!='ACCESOS':
                st.warning(f'El mapa representa la penetración (Accesos por 100 hogares), no la variable {select_variable}')  
            else:
                pass
            TelfijaReg=Telfija.groupby(['PERIODO','REGIÓN','ID_MUNICIPIO','MUNICIPIO'])['CANTIDAD_LINEAS_ACCESOS'].sum().reset_index()            
            col1,col2,col3=st.columns([1,1.5,1])
            with col2:
                periodo=st.selectbox('Escoja el periodo',['2022-T1','2022-T2','2022-T3','2022-T4'],index=3)
                folium_static(MapaRegional(TelfijaReg,periodo,select_reg),width=450) 

    if select_ambito=='Departamental':
        st.markdown(r"""<div><center><h3>"""+select_dpto.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)

        tab1,tab2,tab3 = st.tabs(['Gráfica','Tabla con datos','Mapa'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Dep_info(Telfija)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Dep_info(Telfija)[1],select_variable.capitalize()),use_container_width=True)           
        with tab3:
            if select_variable!='ACCESOS':
                st.warning(f'El mapa representa la penetración (Accesos por 100 hogares), no la variable {select_variable}')  
            else:
                pass
            TelfijaMuni=Telfija.groupby(['PERIODO','ID_MUNICIPIO','MUNICIPIO'])['CANTIDAD_LINEAS_ACCESOS'].sum().reset_index()
            col1,col2,col3=st.columns([1,1.5,1])
            with col2:
                periodo=st.selectbox('Escoja el periodo',['2022-T1','2022-T2','2022-T3','2022-T4'],index=3)
                folium_static(MapaMunicipal(TelfijaMuni,periodo,select_dpto.split('-')[1].zfill(2)),width=450) 
                                
    if select_ambito=='Municipal':
        st.markdown(r"""<div><center><h3>"""+select_muni.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)        
        tab1,tab2 = st.tabs(['Gráfica','Tabla con datos'])
        with tab1:
            st.plotly_chart(PlotlyBarrasSegmento(Muni_info(Telfija)[0],select_variable), use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:
                st.plotly_chart(PlotlyTable(Muni_info(Telfija)[1],select_variable.capitalize()),use_container_width=True) 

#Servicios empaquetados                
if select_servicio=='Empaquetados':
    st.markdown(r"""<div class="titulo"><h2>Empaquetados fijos</h2></div>""",unsafe_allow_html=True)
    with st.expander("Clasificaciones empaquetados fijos"):
        st.markdown("<b>Clasificaciones</b>",unsafe_allow_html=True)
        st.markdown("<p>Triple play: Internet fijo + Televisión por suscripción +Telefonía fija</p>",unsafe_allow_html=True)
        st.markdown("<p>Duo play 1: Internet fijo + Telefonía fija</p>",unsafe_allow_html=True)
        st.markdown("<p>Duo play 2: Internet fijo + Televisión por suscripción</p>",unsafe_allow_html=True)
        st.markdown("<p>Duo play 3: Televisión por suscripción + Telefonía fija</p>",unsafe_allow_html=True)
    
    dict_serv_empaq={'Duo Play 1 (Telefonía fija + Internet fijo)':'Duo Play 1','Duo Play 2 (Internet fijo y TV por suscripción)':'Duo Play 2', 'Duo Play 3 (Telefonía fija y TV por suscripción)':'Duo Play 3', 'Triple Play (Telefonía fija + Internet fijo + TV por suscripción)':'Triple play'}    
    if select_ambito=='Nacional':
        Empaquetados_Nac=FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index()   
        Empaquetados_Nac=Empaquetados_Nac.rename(columns=dict_variables)
        Empaquetados_Nac['SERVICIO_PAQUETE']=Empaquetados_Nac['SERVICIO_PAQUETE'].replace(dict_serv_empaq)
        Empaquetados_Nac2=pd.concat([FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','CODSEG']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
        FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
        Empaquetados_Nac2=Empaquetados_Nac2.rename(columns=dict_variables)
        Empaquetados_Nac2=pd.pivot(Empaquetados_Nac2[['PERIODO','SEGMENTO','SERVICIO_PAQUETE',select_variable]], index=['PERIODO','SERVICIO_PAQUETE'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)

        tab1,tab2 = st.tabs(['Gráfica','Tabla con datos'])
        with tab1:
            st.plotly_chart(PlotlyBarrasEmpaquetados(Empaquetados_Nac,select_variable),use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:              
                select_servpaquete=st.selectbox('',Empaquetados_Nac2['SERVICIO_PAQUETE'].unique().tolist())
                Empaquetados_Nac2=Empaquetados_Nac2[Empaquetados_Nac2['SERVICIO_PAQUETE']==select_servpaquete].drop(columns=['SERVICIO_PAQUETE'],axis=1)
                Empaquetados_Nac2_html = f'<div class="styled-table">{Empaquetados_Nac2.to_html(index=False)}</div>'  
                st.plotly_chart(PlotlyTable(Empaquetados_Nac2,select_variable.capitalize()),use_container_width=True) 

    if select_ambito=='Regional':
        st.markdown(r"""<div><center><h3>"""+select_reg+"""</h3></center></div>""",unsafe_allow_html=True)
        Empaquetados_Reg=FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','REGIÓN']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index()   
        Empaquetados_Reg=Empaquetados_Reg.rename(columns=dict_variables)
        Empaquetados_Reg['SERVICIO_PAQUETE']=Empaquetados_Reg['SERVICIO_PAQUETE'].replace(dict_serv_empaq)
        Empaquetados_Reg=Empaquetados_Reg[Empaquetados_Reg['REGIÓN']==select_reg]
        Empaquetados_Reg2=pd.concat([FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','REGIÓN','CODSEG']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
        FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','REGIÓN']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
        Empaquetados_Reg2=Empaquetados_Reg2.rename(columns=dict_variables)
        Empaquetados_Reg2=Empaquetados_Reg2[Empaquetados_Reg2['REGIÓN']==select_reg]
        Empaquetados_Reg2=pd.pivot(Empaquetados_Reg2[['PERIODO','SEGMENTO','SERVICIO_PAQUETE',select_variable]], index=['PERIODO','SERVICIO_PAQUETE'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)

        tab1,tab2 = st.tabs(['Gráfica','Tabla con datos'])
        with tab1:
            st.plotly_chart(PlotlyBarrasEmpaquetados(Empaquetados_Reg,select_variable),use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:               
                select_servpaquete=st.selectbox('',Empaquetados_Reg2['SERVICIO_PAQUETE'].unique().tolist())
                Empaquetados_Reg2=Empaquetados_Reg2[Empaquetados_Reg2['SERVICIO_PAQUETE']==select_servpaquete].drop(columns=['SERVICIO_PAQUETE'],axis=1)
                Empaquetados_Reg2_html = f'<div class="styled-table">{Empaquetados_Reg2.to_html(index=False)}</div>'  
                st.plotly_chart(PlotlyTable(Empaquetados_Reg2,select_variable.capitalize()),use_container_width=True)                 
            
    if select_ambito=='Departamental':
        st.markdown(r"""<div><center><h3>"""+select_dpto.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)
        Empaquetados_Dep=FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','CODIGO_DEPARTAMENTO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index()   
        Empaquetados_Dep=Empaquetados_Dep.rename(columns=dict_variables)
        Empaquetados_Dep['SERVICIO_PAQUETE']=Empaquetados_Dep['SERVICIO_PAQUETE'].replace(dict_serv_empaq)
        Empaquetados_Dep=Empaquetados_Dep[Empaquetados_Dep['CODIGO_DEPARTAMENTO']==select_dpto]
        Empaquetados_Dep2=pd.concat([FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','CODIGO_DEPARTAMENTO','CODSEG']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
        FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','CODIGO_DEPARTAMENTO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
        Empaquetados_Dep2=Empaquetados_Dep2.rename(columns=dict_variables)
        Empaquetados_Dep2=Empaquetados_Dep2[Empaquetados_Dep2['CODIGO_DEPARTAMENTO']==select_dpto]
        Empaquetados_Dep2=pd.pivot(Empaquetados_Dep2[['PERIODO','SEGMENTO','SERVICIO_PAQUETE',select_variable]], index=['PERIODO','SERVICIO_PAQUETE'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)

        tab1,tab2 = st.tabs(['Gráfica','Tabla con datos'])
        with tab1:
            st.plotly_chart(PlotlyBarrasEmpaquetados(Empaquetados_Dep,select_variable),use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:               
                select_servpaquete=st.selectbox('',Empaquetados_Dep2['SERVICIO_PAQUETE'].unique().tolist())
                Empaquetados_Dep2=Empaquetados_Dep2[Empaquetados_Dep2['SERVICIO_PAQUETE']==select_servpaquete].drop(columns=['SERVICIO_PAQUETE'],axis=1)
                Empaquetados_Dep2_html = f'<div class="styled-table">{Empaquetados_Dep2.to_html(index=False)}</div>'  
                st.plotly_chart(PlotlyTable(Empaquetados_Dep2,select_variable.capitalize()),use_container_width=True)
                            
            
    if select_ambito=='Municipal':
        st.markdown(r"""<div><center><h3>"""+select_muni.split('-')[0]+"""</h3></center></div>""",unsafe_allow_html=True)
        Empaquetados_Mun=FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','CODIGO_MUNICIPIO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index()   
        Empaquetados_Mun=Empaquetados_Mun.rename(columns=dict_variables)
        Empaquetados_Mun['SERVICIO_PAQUETE']=Empaquetados_Mun['SERVICIO_PAQUETE'].replace(dict_serv_empaq)
        Empaquetados_Mun=Empaquetados_Mun[Empaquetados_Mun['CODIGO_MUNICIPIO']==select_muni]
        Empaquetados_Mun2=pd.concat([FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','CODIGO_MUNICIPIO','CODSEG']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).reset_index(),
        FT1_3.groupby(['PERIODO','SERVICIO_PAQUETE','CODIGO_MUNICIPIO']).agg({'CANTIDAD_LINEAS_ACCESOS': 'sum', 'VALOR_FACTURADO_O_COBRADO': 'sum', 'ID_EMPRESA': 'nunique'}).assign(CODSEG='Total').reset_index()]).sort_values(by=['PERIODO'])
        Empaquetados_Mun2=Empaquetados_Mun2.rename(columns=dict_variables)
        Empaquetados_Mun2=Empaquetados_Mun2[Empaquetados_Mun2['CODIGO_MUNICIPIO']==select_muni]
        Empaquetados_Mun2=pd.pivot(Empaquetados_Mun2[['PERIODO','SEGMENTO','SERVICIO_PAQUETE',select_variable]], index=['PERIODO','SERVICIO_PAQUETE'], columns=['SEGMENTO'], values=select_variable).reset_index().fillna(0)

        tab1,tab2 = st.tabs(['Gráfica','Tabla con datos'])
        with tab1:
            st.plotly_chart(PlotlyBarrasEmpaquetados(Empaquetados_Mun,select_variable),use_container_width=True)
        with tab2:
            col1,col2,col3=st.columns([0.1,1,0.1])
            with col2:            
                select_servpaquete=st.selectbox('',Empaquetados_Mun2['SERVICIO_PAQUETE'].unique().tolist())
                Empaquetados_Mun2=Empaquetados_Mun2[Empaquetados_Mun2['SERVICIO_PAQUETE']==select_servpaquete].drop(columns=['SERVICIO_PAQUETE'],axis=1)
                Empaquetados_Mun2_html = f'<div class="styled-table">{Empaquetados_Mun2.to_html(index=False)}</div>'  
                st.plotly_chart(PlotlyTable(Empaquetados_Mun2,select_variable.capitalize()),use_container_width=True)
                                               