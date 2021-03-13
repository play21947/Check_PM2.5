import requests

url = "http://api.airvisual.com/v2/nearest_city?key=5785584a-16fb-4b4d-9446-86dababf6250"

res = requests.get(url)
data = res.json()

def result(value):
    if(value >= 0 and value <= 25):
        print("So Good")
    elif(value >= 26 and value <= 50):
        print('Good')
    elif(value >= 51 and value <= 100):
        print('Normal')
    elif(value >= 101 and value <= 200):
        print('Bad')
    else:
        print("So Bad")


def display():
    print("1. Check PM 2.5")
    print("2. Exit")
    choose = int(input())
    if(choose == 1):
        value = data['data']['current']['pollution']['aqius']
        print("State : ",data['data']['state'])
        print("Value : ",value)
        result(value)
    elif(choose == 2):
        quit()

display()
