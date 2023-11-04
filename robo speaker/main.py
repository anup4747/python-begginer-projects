import os

if __name__=='__main__':

    print("Welcome to my robo project")
    hi="Welcome to my robo project"
    command1 = 'PowerShell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{}\')"'.format(hi)
    os.system(command1) 
    start="Enter any english word what you want to pronounce"
    command2 = 'PowerShell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{}\')"'.format(start)
    os.system(command2)  
    while True:
        # Get user input
        word = input("Enter a any english word what you want to pronounce: ")
        if word == "exit":
            exx="What a fun! Have a nice day !Bye Bye"
            command2 = 'PowerShell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{}\')"'.format(exx)
            os.system(command2)
            break
        # Construct the command
        command3 = 'PowerShell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{}\')"'.format(word)
        # Run the command
        os.system(command3)
