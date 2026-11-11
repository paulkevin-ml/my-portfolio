visitor_ids = {101, 102, 103}
print("Starting set: ", visitor_ids)

visitor_ids.add(104)
visitor_ids.add(102)
print("After adding 104 and duplicate 102: ", visitor_ids)

location = (48.8566, 2.3522)
lat, lon = location
print("Latitude: ",lat)
print("Longitude: ",lon)

location[0] = 50.0