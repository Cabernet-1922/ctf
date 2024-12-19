# Mr-Worldwide [Medium] (by Danny) - picoCTF 2019
> A musician left us a <a href='//jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt'>message</a>. What's it mean?


```text
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```
With `geopy` to find the city of these location:
```python
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='my-geocoding-app')
coordinates = [
    (35.028309, 135.753082),
    (46.469391, 30.740883),
    (39.758949, -84.191605),
    (41.015137, 28.979530),
    (24.466667, 54.366669),
    (3.140853, 101.693207),
    (9.005401, 38.763611),
    (-3.989038, -79.203560),
    (52.377956, 4.897070),
    (41.085651, -73.858467),
    (57.790001, -152.407227),
    (31.205753, 29.924526)
]
res = ""
for lat, lon in coordinates:
    location = geolocator.reverse((lat, lon), exactly_one=True, language='en')
    address = location.raw.get('address', {})
    city = address.get('city') or address.get('town') or address.get('village') or address.get('state')
    print(f"Coordinates: ({lat}, {lon}) -> {city}")
```

Then we get:
```text
Coordinates: (35.028309, 135.753082) -> Kyoto
Coordinates: (46.469391, 30.740883) -> Odesa
Coordinates: (39.758949, -84.191605) -> Dayton
Coordinates: (41.015137, 28.97953) -> Istanbul
Coordinates: (24.466667, 54.366669) -> Abu Dhabi
Coordinates: (3.140853, 101.693207) -> Kuala Lumpur
Coordinates: (9.005401, 38.763611) -> Addis Ababa
Coordinates: (-3.989038, -79.20356) -> Loja
Coordinates: (52.377956, 4.89707) -> Amsterdam
Coordinates: (41.085651, -73.858467) -> Village of Sleepy Hollow
Coordinates: (57.790001, -152.407227) -> Kodiak
Coordinates: (31.205753, 29.924526) -> Alexandria
```
Concatenate the first letter of each of these locations to form a flag (remember `_` in the middle).

flag: `picoCTF{KODIAK_ALASKA}`
