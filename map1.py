import folium
import pandas

na_vals = ['Missing']   #NaN values are assigned a string of 'Missing'
data = pandas.read_csv('C:/Users/LENOVO/Desktop/CountryDataN.csv', encoding = "UTF-8", na_values=na_vals) #Reading from CSV file
#Assigning data from CSV to our local variables 
country = list(data['Country'])
lat = list(data['Lat'])
lon = list(data['Lon'])
capital = list(data['Capital_City'])
code = list(data['Country_Code'])
currency = list(data['Currency'])
population = list(data['Population'])
image = list(data['Image_name'])
image_link = list(data['Image_URL'])

map = folium.Map(location = [22.66, 79.37], zoom_start = 4,tiles= "Stamen Terrain") #Create a Map object
fg = folium.FeatureGroup(name = "My Map")  # Create Feature Group

#The format in which we want our pop-up to be rendered is defined inside the html variable
html = """<b>Country Name: </b> %s 
 <br> <b> Capital: </b> %s
<br> <b>Country Code: </b> %s
<br> <b>Currency: </b> %s 
<br> <b>Population: </b> %s
<br><b> Flag: </b> <br><img src = %s height=100  width=235 alt="Sorry! Map not available">
"""

tooltip = "Click for more Info"  #Global tooltip

#Make the iframe for pop-up and add Marker to each of the locations defined in csv using for loop
for count,lt,ln,cap,cod,curr,pop,img,img_link in zip(country,lat,lon,capital,code,currency,population,image,image_link):
    iframe = folium.IFrame(html=html % (count,cap, cod, curr,pop,img_link), width = 250, height = 235)
    fg.add_child(folium.Marker(location=[lt,ln], popup= folium.Popup(iframe),icon= folium.Icon(color= 'blue'), tooltip = tooltip))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function= lambda x: {'fillColor' : 'yellow' if x['properties']['POP2005'] < 10000000})) 

map.add_child(fg) #Add the feature group to Map object
map.save('Map1.html')