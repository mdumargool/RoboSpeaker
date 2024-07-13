import win32com.client as wincom
if __name__=='__main__':
    print("Welcome to Robo Speaker. Created by Umar")
    while True:
        x =input("Enter what you want me to speak : ")
        if x=="stop":
            break
        speak =wincom.Dispatch("SAPI.SpVoice")
        speak.Speak(x)


