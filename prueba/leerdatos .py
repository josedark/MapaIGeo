import pandas as pd
import folium

archivo_csv='prueba.csv'
datos=pd.read_csv(archivo_csv,delimiter=',', encoding='iso-8859-1')
print(datos.head())


from folium.plugins import HeatMap
m = folium.Map([14.4133, -87.7567], zoom_start=7)


folium.TileLayer(tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', attr = 'Google', name = 'Google Maps', overlay = True, control = True ).add_to(m)
folium.TileLayer('openstreetmap').add_to(m)
#folium.TileLayer('cartodbdark_matter').add_to(m)


Tipologia=datos['Incidente'].unique()

grupos=[]
for row in Tipologia:
    df=datos[ datos['Incidente'] == row]
    lats_longs = []
    marker_Tipologia = folium.FeatureGroup(row).add_to(m)
    for index, rowdf in df.iterrows():
        #print(rowdf['Marca_temporal'])
        #print(rowdf['Longitud'],rowdf['latitud'])
        #print(float(rowdf['Longitud']),float(rowdf['latitud']))
        folium.Marker([float(rowdf['Latitud']) , float(rowdf['Longitud'])], icon=folium.Icon("red"),popup=rowdf['SubIncidente']).add_to(marker_Tipologia)
        lats_longs.append([float(rowdf['Latitud']) , float(rowdf['Longitud'])])
    grupos.append(marker_Tipologia)
    HeatMap(lats_longs).add_to(folium.FeatureGroup(name='Mapa de Calor :'+row).add_to(m))


for row in grupos:
    m.add_child(row)


folium.LayerControl().add_to(m)

m.save('mapa de calor CECOP SRC.html')
