import requests

furl = "http://localhost:8005"
fam = "testdb"


def api_call(url, family):
    api_location = "/api/v1/by_location/" + family
    command = url + api_location
    all_devices = []
    payload = {"history": 30, "num_scanners": 1}
    print("Calling: ", command)
    re = requests.get(command, params=payload)
    r = re.json()

    print("Http status code: ", re.status_code)
    print(r["locations"][0])
    if re.status_code == 200 and r["success"] == True:
        i = 0
        t = 0
        while i < len(r["locations"]):

            name = r['locations'][i]["location"]
            lat = r['locations'][i]["gps"]["lat"]
            lon = r['locations'][i]["gps"]["lon"]
            tot = r['locations'][i]["total"]
            all_devices.append({"location": name, "lat": lat, "lon": lon, "tot": tot})
            i += 1
        print("API parsed")
        return all_devices
    else:
        print("External error")
        exit(5)


output = api_call(furl, fam)
print(output)
