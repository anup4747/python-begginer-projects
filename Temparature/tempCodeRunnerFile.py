w=wdic["current"]["temp_c"]
    print(f"The temperature of the {city} is {w} C")
    out=f"The temperature of the {city} is {w} degree celsius"
    command4 = 'PowerShell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{}\')"'.format(out)
    os.system(command4)