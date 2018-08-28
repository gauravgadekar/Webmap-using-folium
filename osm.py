import folium
import pandas

data=pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
vname=list(data["NAME"])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09],zoom_start=6,tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="Volcanoes") #feature group

for lt,ln,el,nam in zip(lat,lon,elev,vname): #use zip function to iterate through 2 lists
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup("Name: "+str(nam)+", Elevation: "+str(el)+"m",parse_html=True),radius=10,color='grey',fill_color=color_producer(el),fill=1,fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population") #feature group


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green'if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())



map.save("Map1.html")
