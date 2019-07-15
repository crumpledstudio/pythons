from gtts import gTTS    
from playsound import playsound

audio = 'Ola , Sou o Ambrosyu, o que vai desejar ?'
def talkToMe(audio, lgg = 'pt-br'):
    #print(audio)
    tts = gTTS(text = audio, lang = lgg)
    tts.save('audio.mp3') #doesn't work
    playsound('audio.mp3')
    return None
talkToMe(audio , lgg ='pt-br')  