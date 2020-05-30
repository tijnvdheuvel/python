import requests

furl = "https://cloud.internalpositioning.com"
fam = "testdb"


def api_call(url, family):
    api_location = "/api/v1/by_location/" + family
    command = url + api_location
    all_devices = []
    payload = {"history": 30, "num_scanners": 1}
    print("Calling: ", command)
    r = requests.get(command, params=payload)
    print("Http status code: ", r.status_code)
    if r.status_code == 200 and r.text["success"] == "true":
        i = 0
        t = 0
        if r.text["success"] == "true":
            r.text["success"] = True
        elif r.text["success"] == "false":
            r.text["success"] = False
        while i < len(r.text["locations"]):
            while t < len(r.text["locations"[i["devices"]]]):
                if r.text["locations"[i["devices"[t["randomized"]]]]] == "true":
                    r.text["locations"[i["devices"[t["randomized"]]]]] = True
                elif r.text["locations"[i["devices"[t["randomized"]]]]] == "false":
                    r.text["locations"[i["devices"[t["randomized"]]]]] = False
                t += 1

            name = r.text['locations'[i["location"]]]
            lat = r.text['locations'[i["gps"]["lat"]]]
            lon = r.text['locations'[i["gps"]["lon"]]]
            tot = r.text['locations'[i["total"]]]
            all_devices.append(dict[("location", name), ("lat", lat), ("lon", lon), ("tot", tot)])
            i += 1
        print("API parsed")
        return all_devices
    else:
        print("External error")
        exit(5)

'''
dingetje = {
    "locations": [
        {
            "devices": [
                {
                    "device": "wifi-88:d7:f6:a7:2a:48",
                    "vendor": "ASUSTek Computer Inc.",
                    "timestamp": "2018-03-10T11:29:33.063Z",
                    "probability": 0.89,
                    "randomized": "true",
                    "num_scanners": 3,
                    "active_mins": 1295,
                    "first_seen": "2018-03-09T06:58:21.327Z"
                },
                {
                    "device": "wifi-40:4e:36:89:63:a5",
                    "vendor": "HTC Corporation",
                    "timestamp": "2018-03-10T11:25:34.469Z",
                    "probability": 0.83,
                    "randomized":  "true",
                    "num_scanners": 3,
                    "active_mins": 815,
                    "first_seen": "2018-03-09T07:16:49.934Z"
                }
            ],
            "location": "desk",
            "gps": {
                "lat": 47.5675768678,
                "lon": -122.79879696595,
            },
            "total": 2
        },
        {
            "devices": [
                {
                    "device": "wifi-20:df:b9:49:1c:61",
                    "vendor": "Google, Inc.",
                    "timestamp": "2018-03-10T11:29:33.043Z",
                    "probability": 0.88,
                    "randomized": False,
                    "num_scanners": 3,
                    "active_mins": 1123,
                    "first_seen": "2018-03-09T06:59:34.364Z"
                }
            ],
            "location": "kitchen",
            "gps": {
                "lat": 47.5675768678,
                "lon": -122.79879696595,
            },
            "total": 1
        }
    ],
    "message": "got locations",
    "success": True
}
j = 0
alles = []
if j < len(dingetje["locations"]):
    wow = dingetje['locations'[j]]
    #name = dingetje['locations'[j["location"]]]
    #lat = dingetje['locations'[j["gps"]["lat"]]]
   # lon = dingetje['locations'[j["gps"]["lon"]]]
   # tot = dingetje['locations'[j["total"]]]
   # alles.append(dict[("location", name), ("lat", lat), ("lon", lon), ("tot", tot)])
    j = j + 1


test = api_call(furl, fam)

'''
#  def __init__(self, location, lon, lat, total):
#      self.location = location
   ##     self.lon = lon
    ##    self.lat = lat
     ##   self. total = total
      ##  Device.all_devices.append(self)
