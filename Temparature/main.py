import requests
import json
import os

print("Welcome to my Weather project")
hi="Welcome to my Weather project"
command1 = 'PowerShell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{}\')"'.format(hi)
os.system(command1)
while True:
    print("Enter the name of city :")
    inp="enter the name of city"
    command2 = 'PowerShell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{}\')"'.format(inp)
    os.system(command2)
    city = input()
    if city == "exit":
            exx="See you soon ,, bye bye"
            command3 = 'PowerShell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{}\')"'.format(exx)
            os.system(command3)
            break
    url=f"http://api.weatherapi.com/v1/current.json?key=4adbc8466a7f4c4890f112754230605&q={city}=no"
    r=requests.get(url)
#     print(r.text)
    wdic=json.loads(r.text)
    w=wdic["current"]["temp_c"]
    print(f"The temperature of the {city} is {w} C")
    out=f"The temperature of the {city} is {w} degree celsius"
    command4 = 'PowerShell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{}\')"'.format(out)
    os.system(command4)