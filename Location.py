import phonenumbers as ph
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from geopy.geocoders import Nominatim
from opencage.geocoder import OpenCageGeocode

number = "+923226256445"
ch_num = ph.parse(number)
key = "30348a8c332a424088e0ed8f2792cc89"

geoloc = geocoder.description_for_number(ch_num, "en")
print("Country: ", geoloc)
serviceProv = carrier.name_for_number(ch_num, "en")
print("Service Provider: ", serviceProv)

geocoder = OpenCageGeocode(key)
query = str(geoloc)
res = geocoder.geocode(query)
lat = res[0]["geometry"]["lat"]
lng = res[0]["geometry"]["lng"]
print("Location: ", lat, lng)


def get_location(latitude, longitude):
    geolocator = Nominatim(user_agent="my_app")  # Set a custom user agent

    # Reverse geocode the coordinates
    location = geolocator.reverse(f"{latitude}, {longitude}")

    return location.address


locate = get_location(lat, lng)
print(locate)
