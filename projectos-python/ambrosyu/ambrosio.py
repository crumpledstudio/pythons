import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def cria_audio(frase):
    tts = gTTS(frase, lang='pt-pt', slow=False)

    tts.save('audios/hello.mp3')

    print("Estou a aprender o que me dizem...")

    playsound('audios/hello.mp3')


def ouvir_microfone():

    microfone = sr.Recognizer()
    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa: ")

        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Voce disse: " + frase)
        

    except Exception as e:
        print(e)
        print("Nao percebi, pode repetir?")

    return frase

frase = ouvir_microfone()
cria_audio(frase)



