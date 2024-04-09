import subprocess
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0 Created by Ashish")
    while True:
        x = input("Enter what you want to me speak: ")
        if x == "q":
            break
        else:
            command = (f'echo {x} | PowerShell -Command "Add-Type -AssemblyName System.Speech; '
                    f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())"')
            subprocess.run(command, shell=True)
