import phonenumbers
import opencage
import folium

number = input("")

from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print("Country -",location)

from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print("Sim -",carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode
key=r"5eb07102e65048e98c76568600b10fc4"
geocoder = OpenCageGeocode(key)
query = str(location)
results= geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print("Location Coordinates -",lat,lng)
print("Your phone will be Hack soon!!")

# now location on website

myMap= folium.Map(loaction=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")
