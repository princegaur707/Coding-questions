#Read the news
#Using NEWS API(newsap.org) extracts the news and speaks it 
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__== "__main__":
    speak("Tina is like fool")