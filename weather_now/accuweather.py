import requests
import json

def get_weather():

    lat = 1.371661
    lon = 103.823306
    API_key = 'mtPjpsrWZZXFco9TtddtQAv0PVtvql3s'
    loc_key = 300597

    url = f'http://dataservice.accuweather.com/currentconditions/v1/{loc_key}?apikey={API_key}&details=true'


    response = requests.get(url).json()
    #print(response.text)
    # print(json.dumps(response, indent = 1))
    # open('accuweather.json', 'w').write(json.dumps(response, indent = 1))
    # with open('json_data.json', 'w') as outfile:
    #     outfile.write(json.dumps(response))

    temp = response[0]["Temperature"]["Metric"]["Value"]
    hum = response[0]["RelativeHumidity"]

    return temp,hum

if __name__ == "__main__":
    temp,hum = get_weather()
    print(f"The temperature now is {temp}°C and the RH is {hum}%")
